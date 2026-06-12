from accounting_platform import AccountingPlatform, QuickBooksAuthenticator, QuickBooksImporter
import json
from datetime import datetime

def test_connect_quickbooks():
    authenticator = QuickBooksAuthenticator()
    importer = QuickBooksImporter(authenticator)
    platform = AccountingPlatform(importer)
    assert platform.connect_quickbooks("test", "test") == True
    assert platform.connect_quickbooks("wrong", "wrong") == False

def test_import_financial_data():
    authenticator = QuickBooksAuthenticator()
    importer = QuickBooksImporter(authenticator)
    platform = AccountingPlatform(importer)
    data = platform.import_financial_data("2022-01-01", "2022-01-03")
    assert len(data) == 3
    assert data[0].date == "2022-01-01"
    assert data[0].amount == 100.0

def test_store_financial_data():
    authenticator = QuickBooksAuthenticator()
    importer = QuickBooksImporter(authenticator)
    platform = AccountingPlatform(importer)
    data = platform.import_financial_data("2022-01-01", "2022-01-03")
    platform.store_financial_data(data)
    with open("financial_data.json", "r") as f:
        stored_data = json.load(f)
    assert len(stored_data) == 3
    assert stored_data[0]["date"] == "2022-01-01"
    assert stored_data[0]["amount"] == 100.0
