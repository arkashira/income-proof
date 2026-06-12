from xero_integration import XeroIntegration, FinancialData
import json
import pytest

def test_authenticate():
    xero = XeroIntegration("mock_api_key", "mock_api_secret")
    xero.authenticate()
    assert xero.access_token == "mock_access_token"

def test_import_financial_data():
    xero = XeroIntegration("mock_api_key", "mock_api_secret")
    xero.authenticate()
    financial_data = xero.import_financial_data("2022-01-01", "2022-01-31")
    assert len(financial_data) == 2
    assert financial_data[0].date == "2022-01-01"
    assert financial_data[0].amount == 100.0
    assert financial_data[0].description == "Mock transaction 1"

def test_store_financial_data():
    xero = XeroIntegration("mock_api_key", "mock_api_secret")
    xero.authenticate()
    financial_data = xero.import_financial_data("2022-01-01", "2022-01-31")
    xero.store_financial_data(financial_data)
    with open("financial_data.json", "r") as f:
        stored_data = json.load(f)
    assert len(stored_data) == 2
    assert stored_data[0]["date"] == "2022-01-01"
    assert stored_data[0]["amount"] == 100.0
    assert stored_data[0]["description"] == "Mock transaction 1"
