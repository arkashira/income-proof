from income_analytics import IncomeAnalytics, IncomeData

def test_view_trends():
    analytics = IncomeAnalytics()
    analytics.add_income('2022-01-01', 1000)
    analytics.add_income('2022-01-15', 1200)
    analytics.add_income('2022-02-01', 1100)
    trends = analytics.view_trends()
    assert trends[2022][1] == [1000, 1200]
    assert trends[2022][2] == [1100]

def test_view_summary():
    analytics = IncomeAnalytics()
    analytics.add_income('2022-01-01', 1000)
    analytics.add_income('2022-01-15', 1200)
    total_income, average_income = analytics.view_summary()
    assert total_income == 2200
    assert average_income == 1100

def test_update_analytics():
    analytics = IncomeAnalytics()
    new_data = [IncomeData('2022-01-01', 1000), IncomeData('2022-01-15', 1200)]
    analytics.update_analytics(new_data)
    assert len(analytics.income_data) == 2
