import argparse
import json
import dataclasses
from typing import Dict

@dataclasses.dataclass
class SupportTicket:
    id: int
    user_name: str
    issue: str

class SupportSystem:
    def __init__(self):
        self.tickets = []

    def submit_ticket(self, user_name: str, issue: str) -> int:
        ticket = SupportTicket(len(self.tickets) + 1, user_name, issue)
        self.tickets.append(ticket)
        return ticket.id

    def get_ticket(self, ticket_id: int) -> SupportTicket:
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        return None

def main():
    parser = argparse.ArgumentParser(description='Submit a support ticket')
    parser.add_argument('--user_name', type=str, required=True, help='User name')
    parser.add_argument('--issue', type=str, required=True, help='Issue description')
    args = parser.parse_args()

    support_system = SupportSystem()
    ticket_id = support_system.submit_ticket(args.user_name, args.issue)
    print(f'Ticket submitted successfully. Ticket number: {ticket_id}')

if __name__ == '__main__':
    main()
