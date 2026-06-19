class BandRoom:
    def __init__(self):
        self.logs = []

    def send(self, sender, message):
        log = f"[{sender}] {message}"
        self.logs.append(log)

    def get_logs(self):
        return self.logs