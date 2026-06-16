"""
Parsers for Klar Analytics knowledge documents.

Each parser takes raw Markdown text and returns a structured dict
with metadata, sections, and typed content extracted from the file.
All parsers follow the same signature: parse(text: str, filepath: str) -> dict
"""

import os
import re
from typing import List, Dict, Optional


# ─── Shared utilities ───

def _extract_h1(text: str) -> Optional[str]:
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    return m.group(1).strip() if m else None


def _extract_h2_sections(text: str) -> Dict[str, str]:
    sections = {}
    pattern = r'^##\s+(.+?)$'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections[heading] = body
    return sections


def _extract_h3_sections(text: str) -> Dict[str, str]:
    sections = {}
    pattern = r'^###\s+(.+?)$'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections[heading] = body
    return sections


def _extract_bullets(text: str) -> List[str]:
    return [i.strip() for i in re.findall(r'^[*-]\s+(.+)$', text, re.MULTILINE)]


def _extract_ordered_items(text: str) -> List[str]:
    return [i.strip() for i in re.findall(r'^\d+[.)]\s+(.+)$', text, re.MULTILINE)]


def _extract_bold_key_values(text: str) -> Dict[str, str]:
    pairs = {}
    for m in re.finditer(r'\*\*(.+?)\*\*:\s*(.*)', text):
        pairs[m.group(1).strip()] = m.group(2).strip()
    return pairs


def _extract_tables(text: str) -> List[Dict]:
    table_pattern = r'^\|(.+)\|\n\|[-| ]+\|\n((?:\|.+\|\n?)*)'
    tables = []
    for m in re.finditer(table_pattern, text, re.MULTILINE):
        headers = [h.strip() for h in m.group(1).split('|') if h.strip()]
        rows = []
        for line in m.group(2).strip().split('\n'):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if cells:
                rows.append(cells)
        if headers:
            tables.append({'headers': headers, 'rows': rows})
    return tables


def _extract_blockquote_meta(text: str) -> Dict[str, str]:
    meta = {}
    for m in re.finditer(r'>\s+\*\*(.+?)\*\*:?\s*(.*)', text):
        meta[m.group(1).strip()] = m.group(2).strip()
    return meta


def _extract_checklist(text: str) -> List[Dict]:
    items = []
    for m in re.finditer(r'^[-*]\s+\[([ xX])\]\s+(.+)$', text, re.MULTILINE):
        items.append({
            'checked': m.group(1).lower() == 'x',
            'text': m.group(2).strip()
        })
    return items


def _extract_tags(text: str) -> List[str]:
    tags = re.findall(r'#(\w+)', text)
    tags += re.findall(r'\[([^\]]+)\]', text)
    return list(set(tags))


def _count_tokens(text: str) -> int:
    return len(text) // 4


# ─── Parser: Agent ───

def parse_agent(text: str, filepath: str) -> Dict:
    result = {
        "type": "agent",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "sections": {},
        "frameworks": [],
        "skills": [],
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        section_data = {
            "body": body,
            "bullets": _extract_bullets(body),
            "tables": _extract_tables(body),
        }

        if "framework" in heading.lower():
            fw_from_bullets = _extract_bullets(body)
            fw_from_regex = [f"Framework_{m}" for m in re.findall(r'Framework_(\w+)', body)]
            # Normalize: strip "Framework_" prefix from all, use canonical dash-case
            all_fw = set()
            for fw in fw_from_bullets + fw_from_regex:
                clean = fw.replace("Framework_", "").replace("_", "-").replace(" ", "-").lower()
                all_fw.add(clean)
            result["frameworks"] = sorted(all_fw)

        if "skill" in heading.lower():
            sk_from_bullets = _extract_bullets(body)
            sk_from_regex = re.findall(r'(\w+_Assessment)', body)
            all_sk = set()
            for sk in sk_from_bullets + sk_from_regex:
                clean = sk.replace("_", "-").replace(" ", "-").replace("assessment", "Assessment")
                clean = clean.lower()
                all_sk.add(clean)
            result["skills"] = sorted(all_sk)

        if heading.lower() in ("rol", "objetivo", "responsabilidades"):
            section_data["key_values"] = _extract_bold_key_values(body)

        result["sections"][heading] = section_data

    return result


# ─── Parser: Skill ───

def parse_skill(text: str, filepath: str) -> Dict:
    result = {
        "type": "skill",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "sections": {},
        "framework_refs": re.findall(r'Framework_(\w+)', text),
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        section_data = {
            "body": body,
            "ordered_items": _extract_ordered_items(body),
            "bullets": _extract_bullets(body),
            "tables": _extract_tables(body),
        }
        result["sections"][heading] = section_data

    return result


# ─── Parser: Knowledge Framework ───

def parse_framework(text: str, filepath: str) -> Dict:
    result = {
        "type": "framework",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "sections": {},
        "subsections": {},
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        h3_sections = _extract_h3_sections(body)
        section_data = {
            "body": body,
            "bullets": _extract_bullets(body),
            "tables": _extract_tables(body),
            "h3_sections": h3_sections,
        }
        result["sections"][heading] = section_data
        result["subsections"].update({f"{heading} > {k}": v for k, v in h3_sections.items()})

    return result


# ─── Parser: CORE Pattern ───

def parse_pattern(text: str, filepath: str) -> Dict:
    result = {
        "type": "pattern",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "categories": {},
        "patterns": [],
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for category, body in sections.items():
        h3_sections = _extract_h3_sections(body)
        patterns_in_category = []

        for pattern_id, pattern_body in h3_sections.items():
            key_values = _extract_bold_key_values(pattern_body)
            pattern_entry = {
                "pattern_id": pattern_id,
                "category": category,
                "fields": key_values,
                "raw": pattern_body,
            }
            patterns_in_category.append(pattern_entry)

        result["categories"][category] = {
            "body": body,
            "pattern_count": len(patterns_in_category),
            "patterns": patterns_in_category,
        }
        result["patterns"].extend(patterns_in_category)

    return result


# ─── Parser: Playbook ───

def parse_playbook(text: str, filepath: str) -> Dict:
    result = {
        "type": "playbook",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "metadata": _extract_blockquote_meta(text),
        "sections": {},
        "tables": _extract_tables(text),
        "checklists": _extract_checklist(text),
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        h3_sections = _extract_h3_sections(body)
        section_data = {
            "body": body,
            "h3_sections": h3_sections,
            "bullets": _extract_bullets(body),
            "ordered_items": _extract_ordered_items(body),
            "tables": _extract_tables(body),
            "checklists": _extract_checklist(body),
        }
        result["sections"][heading] = section_data

    return result


# ─── Parser: Operations Process ───

def parse_process(text: str, filepath: str) -> Dict:
    return parse_playbook(text, filepath)


# ─── Parser registry ───

def detect_type(filepath: str) -> str:
    path = filepath.replace("\\", "/")
    if "/Agents/" in path:
        return "agent"
    if "/Skills/" in path:
        return "skill"
    if "/Knowledge/" in path:
        if "_Patterns." in path or "/CORE/" in path:
            return "pattern"
        if "Framework_" in path:
            return "framework"
        return "knowledge"
    if "/Playbooks/" in path:
        return "playbook"
    if "/Operations/" in path:
        return "process"
    return "unknown"


PARSER_REGISTRY = {
    "agent": parse_agent,
    "skill": parse_skill,
    "framework": parse_framework,
    "pattern": parse_pattern,
    "playbook": parse_playbook,
    "process": parse_process,
}


def parse_file(text: str, filepath: str) -> Dict:
    doc_type = detect_type(filepath)
    parser = PARSER_REGISTRY.get(doc_type)
    if parser:
        result = parser(text, filepath)
        result["doc_type"] = doc_type
        return result
    return {
        "type": "unknown",
        "filepath": filepath,
        "title": _extract_h1(text) or os.path.basename(filepath),
        "body": text[:200],
        "tokens": _count_tokens(text),
    }
