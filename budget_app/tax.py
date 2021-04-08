import json
from datetime import datetime


class tax:
    def __init__(self, state, income, filing_status, year=datetime.today().year):
        self.state = state
        self.income = income
        self.filing_status = filing_status
        self.year = year

    def get_state_brackets(self):
        path = f'/home/genymoneyguy/budget_app/state_tax/{self.year}/{self.state}.json'
        with open(path) as f:
            return dict(json.load(f))

    def get_fed_brackets(self):
        path = f'/home/genymoneyguy/budget_app/federal_tax/{self.year}/fed.json'
        with open(path) as f:
            return dict(json.load(f))

    def tax(self,tax_dict):
        income = self.income
        filing_status = self.filing_status
        data = tax_dict[filing_status]
        try:
            deduction = data['deductions'][0]['deduction_amount']
        except:
            deduction = 0
        brackets = [i['bracket'] for i in data['income_tax_brackets']]
        brackets.reverse()
        tax = [i['marginal_rate']/100 for i in data['income_tax_brackets']]
        tax.reverse()
        taxable_income = income - deduction

        tax_out = 0
        inc_remain = taxable_income
        for b,t in zip(brackets,tax):
            if inc_remain > b:
                taxable = inc_remain - b
                to = taxable * t
                tax_out += to
                inc_remain = b


        return tax_out

    def fica_tax(self):
        with open(f'/home/genymoneyguy/budget_app/fica_tax/{self.year}/fica.json') as f:
            d=json.load(f)
        rate = d['rate']
        wage_limit = d['wage_limit']
        if self.income > wage_limit:
            return wage_limit * rate
        else:
            return self.income * rate

    def state_tax(self):
        tax_dict = self.get_state_brackets()
        return self.tax(tax_dict)

    def fed_tax(self):
        tax_dict = self.get_fed_brackets()
        return self.tax(tax_dict)
