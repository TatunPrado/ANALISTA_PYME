class SessionManager:

    PHASES = [
        "discovery",
        "assessment",
        "validation",
        "report",
        "conversion"
    ]

    def __init__(self, session):

        self.session = session

    def next_phase(self):

        current_index = self.PHASES.index(
            self.session.current_phase
        )

        if current_index < len(self.PHASES) - 1:

            self.session.current_phase = self.PHASES[
                current_index + 1
            ]

        return self.session.current_phase

    def get_phase(self):

        return self.session.current_phase