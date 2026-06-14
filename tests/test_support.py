import pytest
from src.support import SupportTicket, SupportSystem

def test_submit_ticket():
    support_system = SupportSystem()
    ticket_id = support_system.submit_ticket('John Doe', 'Test issue')
    assert isinstance(ticket_id, int)
    assert ticket_id > 0

def test_get_ticket():
    support_system = SupportSystem()
    ticket_id = support_system.submit_ticket('John Doe', 'Test issue')
    ticket = support_system.get_ticket(ticket_id)
    assert isinstance(ticket, SupportTicket)
    assert ticket.id == ticket_id
    assert ticket.user_name == 'John Doe'
    assert ticket.issue == 'Test issue'

def test_get_nonexistent_ticket():
    support_system = SupportSystem()
    ticket = support_system.get_ticket(1)
    assert ticket is None
