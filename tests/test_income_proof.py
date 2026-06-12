import pytest
from income_proof import IncomeProofManager, Report

@pytest.fixture
def manager(tmp_path):
    """
    Fixture to create a manager instance using a temporary file path.
    This ensures tests don't pollute the local filesystem.
    """
    db_file = tmp_path / "test_reports.json"
    return IncomeProofManager(storage_path=str(db_file))

def test_list_empty_reports(manager):
    """Test that listing reports returns an empty list initially."""
    reports = manager.list_reports()
    assert isinstance(reports, list)
    assert len(reports) == 0

def test_create_and_list_reports(manager):
    """Test creating a report and viewing it in the list."""
    manager.create_report("October Income", "Total: $5000")
    
    reports = manager.list_reports()
    assert len(reports) == 1
    assert reports[0].title == "October Income"
    assert reports[0].content == "Total: $5000"

def test_download_report(manager):
    """Test retrieving/downloading a specific report content."""
    created = manager.create_report("November Income", "Total: $6000")
    
    # Simulate download by fetching the object
    downloaded = manager.get_report(created.id)
    
    assert downloaded is not None
    assert downloaded.id == created.id
    assert downloaded.content == "Total: $6000"

def test_download_non_existent_report(manager):
    """Test downloading a report that doesn't exist."""
    result = manager.get_report("fake-id-123")
    assert result is None

def test_delete_report(manager):
    """Test deleting an existing report."""
    created = manager.create_report("December Income", "Total: $7000")
    
    # Verify it exists
    assert len(manager.list_reports()) == 1
    
    # Delete it
    success = manager.delete_report(created.id)
    assert success is True
    
    # Verify it's gone
    assert len(manager.list_reports()) == 0

def test_delete_non_existent_report(manager):
    """Test deleting a report that doesn't exist."""
    success = manager.delete_report("fake-id-123")
    assert success is False
