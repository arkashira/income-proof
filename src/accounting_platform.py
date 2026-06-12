import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class FinancialData:
    date: str
    amount: float

class QuickBooksAuthenticator:
    def authenticate(self, username: str, password: str) -> bool:
        # Simulate authentication for demonstration purposes
        return username == "test" and password == "test"

class QuickBooksImporter:
    def __init__(self, authenticator: QuickBooksAuthenticator):
        self.authenticator = authenticator

    def import_data(self, start_date: str, end_date: str) -> List[FinancialData]:
        # Simulate data import for demonstration purposes
        return [
            FinancialData("2022-01-01", 100.0),
            FinancialData("2022-01-02", 200.0),
            FinancialData("2022-01-03", 300.0),
        ]

class AccountingPlatform:
    def __init__(self, importer: QuickBooksImporter):
        self.importer = importer

    def connect_quickbooks(self, username: str, password: str) -> bool:
        return self.importer.authenticator.authenticate(username, password)

    def import_financial_data(self, start_date: str, end_date: str) -> List[FinancialData]:
        return self.importer.import_data(start_date, end_date)

    def store_financial_data(self, data: List[FinancialData]) -> None:
        # Simulate data storage for demonstration purposes
        with open("financial_data.json", "w") as f:
            json.dump([{"date": d.date, "amount": d.amount} for d in data], f)
