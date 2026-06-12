import json
from dataclasses import dataclass
from typing import List

@dataclass
class Feedback:
    id: int
    message: str

class FeedbackSystem:
    def __init__(self):
        self.feedback = []
        self.id_counter = 0

    def submit_feedback(self, message: str) -> Feedback:
        self.id_counter += 1
        feedback = Feedback(self.id_counter, message)
        self.feedback.append(feedback)
        return feedback

    def get_feedback(self) -> List[Feedback]:
        return self.feedback

    def save_to_file(self, filename: str):
        data = [{"id": f.id, "message": f.message} for f in self.feedback]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename: str):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.feedback = [Feedback(f["id"], f["message"]) for f in data]
                self.id_counter = max(f.id for f in self.feedback) + 1
        except FileNotFoundError:
            pass
