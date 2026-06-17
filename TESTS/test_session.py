from APP.Session.DiagnosisSession import DiagnosisSession


session = DiagnosisSession()

session.company_name = "Empresa Demo"

session.objective = "crecer"

session.add_answer(
    "¿Cuántos empleados tiene?",
    "20"
)

session.add_finding(
    "Dependencia alta del fundador"
)

session.add_risk(
    "Falta de indicadores"
)

session.update_confidence(25)

print(session.company_name)
print(session.objective)

print(session.answers)

print(session.findings)

print(session.risks)

print(session.confidence)