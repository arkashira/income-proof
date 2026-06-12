import json
import uuid
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

@dataclass
class Report:
    id: str
    title: str
    date: str
    content: str

class IncomeProofManager:
    """
    Manages income reports for the user dashboard.
    Handles persistence to a local JSON file.
    """
    def __init__(self, storage_path: str = "reports.json"):
        self.storage_path = Path(storage_path)
        self._ensure_storage()

    def _ensure_storage(self):
        """Creates the storage file if it does not exist."""
        if not self.storage_path.exists():
            self.storage_path.write_text("[]")

    def _load_reports(self) -> List[dict]:
        """Loads raw report data from storage."""
        try:
            return json.loads(self.storage_path.read_text())
        except json.JSONDecodeError:
            # Handle corrupted file by resetting
            return []

    def _save_reports(self, reports: List[dict]):
        """Saves raw report data to storage."""
        self.storage_path.write_text(json.dumps(reports, indent=2))

    def list_reports(self) -> List[Report]:
        """
        Returns a list of all generated reports.
        Acceptance Criteria: User can view a list of generated reports.
        """
        data = self._load_reports()
        return [Report(**item) for item in data]

    def get_report(self, report_id: str) -> Optional[Report]:
        """
        Retrieves a specific report by ID.
        Acceptance Criteria: User can download previous reports (simulated retrieval).
        """
        for r in self.list_reports():
            if r.id == report_id:
                return r
        return None

    def delete_report(self, report_id: str) -> bool:
        """
        Deletes a report by ID.
        Acceptance Criteria: User can delete reports.
        """
        reports = self._load_reports()
        original_len = len(reports)
        reports = [r for r in reports if r['id'] != report_id]
        
        if len(reports) < original_len:
            self._save_reports(reports)
            return True
        return False

    def create_report(self, title: str, content: str) -> Report:
        """
        Helper method to generate a new report.
        (Not explicitly requested in AC, but necessary to populate data for testing).
        """
        new_report = Report(
            id=str(uuid.uuid4()),
            title=title,
            content=content,
            date="2023-10-27" # Simplified date for demo
        )
        reports = self._load_reports()
        reports.append(asdict(new_report))
        self._save_reports(reports)
        return new_report
