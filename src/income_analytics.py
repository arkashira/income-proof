import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class IncomeData:
    date: str
    income: float

class IncomeAnalytics:
    def __init__(self):
        self.income_data = []

    def add_income(self, date, income):
        self.income_data.append(IncomeData(date, income))

    def view_trends(self):
        trends = {}
        for data in self.income_data:
            date = datetime.strptime(data.date, '%Y-%m-%d')
            year = date.year
            month = date.month
            if year not in trends:
                trends[year] = {}
            if month not in trends[year]:
                trends[year][month] = []
            trends[year][month].append(data.income)
        return trends

    def view_summary(self):
        total_income = sum(data.income for data in self.income_data)
        average_income = total_income / len(self.income_data) if self.income_data else 0
        return total_income, average_income

    def update_analytics(self, new_data):
        self.income_data = new_data
