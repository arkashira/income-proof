import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class ReportSection(Enum):
    INCOME = "income"
    EXPENSES = "expenses"
    SAVINGS = "savings"

@dataclass
class IncomeSummary:
    sections: List[ReportSection]
    income: float
    expenses: float
    savings: float

    def to_dict(self):
        return {
            "sections": [section.value for section in self.sections],
            "income": self.income,
            "expenses": self.expenses,
            "savings": self.savings,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

def generate_report(summary: IncomeSummary) -> str:
    report = ""
    if ReportSection.INCOME in summary.sections:
        report += f"Income: {summary.income}\n"
    if ReportSection.EXPENSES in summary.sections:
        report += f"Expenses: {summary.expenses}\n"
    if ReportSection.SAVINGS in summary.sections:
        report += f"Savings: {summary.savings}\n"
    return report
