from income_summary import IncomeSummary, ReportSection, generate_report, customize_report

def test_generate_report():
    summary = IncomeSummary([ReportSection.INCOME, ReportSection.EXPENSES], 1000, 500, 500)
    report = generate_report(summary)
    assert "Income: 1000" in report
    assert "Expenses: 500" in report
    assert "Savings: 500" not in report

def test_customize_report():
    summary = customize_report(1000, 500, 500, [ReportSection.INCOME, ReportSection.SAVINGS])
    assert summary.sections == [ReportSection.INCOME, ReportSection.SAVINGS]
    assert summary.income == 1000
    assert summary.expenses == 500
    assert summary.savings == 500

def test_to_json():
    summary = IncomeSummary([ReportSection.INCOME, ReportSection.EXPENSES], 1000, 500, 500)
    json_report = summary.to_json()
    assert "income" in json_report
    assert "expenses" in json_report
    assert "savings" in json_report
