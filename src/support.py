import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SupportTicket:
    id: int
    name: str
    email: str
    issue: str
    timestamp: str

class SupportSystem:
    def __init__(self):
        self.tickets = []
        self.id_counter = 1

    def submit_ticket(self, name, email, issue):
        ticket = SupportTicket(
            id=self.id_counter,
            name=name,
            email=email,
            issue=issue,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.tickets.append(ticket)
        self.id_counter += 1
        return ticket.id

    def get_tickets(self):
        return self.tickets

    def save_tickets(self, filename):
        data = []
        for ticket in self.tickets:
            data.append({
                "id": ticket.id,
                "name": ticket.name,
                "email": ticket.email,
                "issue": ticket.issue,
                "timestamp": ticket.timestamp
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_tickets(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tickets = []
                self.id_counter = 1
                for ticket_data in data:
                    ticket = SupportTicket(
                        id=ticket_data["id"],
                        name=ticket_data["name"],
                        email=ticket_data["email"],
                        issue=ticket_data["issue"],
                        timestamp=ticket_data["timestamp"]
                    )
                    self.tickets.append(ticket)
                    self.id_counter = max(self.id_counter, ticket.id + 1)
        except FileNotFoundError:
            pass
