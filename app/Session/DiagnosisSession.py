from datetime import datetime


class DiagnosisSession:

    def __init__(self):

        self.created_at = datetime.now()

        self.company_name = None

        self.objective = None

        self.current_phase = "discovery"

        self.findings = []

        self.risks = []

        self.opportunities = []

        self.answers = []

        self.confidence = 0

    def add_answer(self, question, answer):

        self.answers.append(
            {
                "question": question,
                "answer": answer
            }
        )

    def add_finding(self, finding):

        self.findings.append(finding)

    def add_risk(self, risk):

        self.risks.append(risk)

    def add_opportunity(self, opportunity):

        self.opportunities.append(opportunity)

    def update_confidence(self, value):

        self.confidence = value