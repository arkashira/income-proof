from income_summary import IncomeSummary, ReportSection, generate_report

def test_income_summary():
    summary = IncomeSummary(
        sections=[ReportSection.INCOME, ReportSection.EXPENSES],
        income=1000.0,
        expenses=500.0,
        savings=200.0,
    )
    report = generate_report(summary)
    assert "Income: 1000.0" in report
    assert "Expenses: 500.0" in report
    assert "Savings: 200.0" not in report

def test_customized_report():
    summary = IncomeSummary(
        sections=[ReportSection.INCOME, ReportSection.SAVINGS],
        income=1000.0,
        expenses=500.0,
        savings=200.0,
    )
    report = generate_report(summary)
    assert "Income: 1000.0" in report
    assert "Expenses: 500.0" not in report
    assert "Savings: 200.0" in report

def test_to_json():
    summary = IncomeSummary(
        sections=[ReportSection.INCOME, ReportSection.EXPENSES],
        income=1000.0,
        expenses=500.0,
        savings=200.0,
    )
    json_report = summary.to_json()
    assert "income" in json_report
    assert "expenses" in json_report
    assert "savings" in json_report
