from accounting_platform import AccountingPlatform, QuickBooksAuthenticator, FinancialData
import pytest
import json

def test_authenticate():
    authenticator = QuickBooksAuthenticator("client_id", "client_secret")
    assert authenticator.authenticate() == "auth_token"

def test_import_financial_data():
    authenticator = QuickBooksAuthenticator("client_id", "client_secret")
    platform = AccountingPlatform(authenticator)
    financial_data = platform.import_financial_data("2022-01-01", "2022-01-31")
    assert len(financial_data) == 2
    assert financial_data[0].date == "2022-01-01"
    assert financial_data[0].amount == 100.0
    assert financial_data[1].date == "2022-01-02"
    assert financial_data[1].amount == 200.0

def test_store_financial_data():
    authenticator = QuickBooksAuthenticator("client_id", "client_secret")
    platform = AccountingPlatform(authenticator)
    financial_data = [
        FinancialData("2022-01-01", 100.0),
        FinancialData("2022-01-02", 200.0),
    ]
    platform.store_financial_data(financial_data)
    with open("financial_data.json", "r") as f:
        stored_data = json.load(f)
    assert len(stored_data) == 2
    assert stored_data[0]["date"] == "2022-01-01"
    assert stored_data[0]["amount"] == 100.0
    assert stored_data[1]["date"] == "2022-01-02"
    assert stored_data[1]["amount"] == 200.0
