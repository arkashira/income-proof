from support import SupportSystem, SupportTicket

def test_submit_ticket():
    system = SupportSystem()
    ticket_id = system.submit_ticket("John Doe", "john@example.com", "Issue with the product")
    assert ticket_id == 1
    assert len(system.get_tickets()) == 1

def test_get_tickets():
    system = SupportSystem()
    system.submit_ticket("John Doe", "john@example.com", "Issue with the product")
    system.submit_ticket("Jane Doe", "jane@example.com", "Another issue")
    tickets = system.get_tickets()
    assert len(tickets) == 2
    assert tickets[0].id == 1
    assert tickets[1].id == 2

def test_save_and_load_tickets():
    system = SupportSystem()
    system.submit_ticket("John Doe", "john@example.com", "Issue with the product")
    system.save_tickets("tickets.json")
    system = SupportSystem()
    system.load_tickets("tickets.json")
    tickets = system.get_tickets()
    assert len(tickets) == 1
    assert tickets[0].id == 1
