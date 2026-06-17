from APP.Session.DiagnosisSession import DiagnosisSession
from APP.Session.SessionManager import SessionManager


session = DiagnosisSession()

manager = SessionManager(session)

print(manager.get_phase())

print(manager.next_phase())

print(manager.next_phase())

print(manager.next_phase())