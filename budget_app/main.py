from flask import Flask, render_template, redirect, request, send_file, make_response, url_for
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import io
from forms import Form
from tax import tax
import locale


app = Flask(__name__)
# app.config.from_object('config.Config')

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )


def compound_interest(investment, percent_contrib,interest_rate, num_years, annual_contrib):
    l = [investment*(percent_contrib*.01)]
    annual_contrib = annual_contrib * (percent_contrib*.01)
    rate = 1+(interest_rate*.01)
    for i in range(num_years):
        l.append(round((l[i]*rate)+annual_contrib,2))
    return l

def x_axis(time_span):
    current_year = int(datetime.today().strftime('%Y'))
    l = [current_year]
    for i in range(time_span):
        l.append(l[-1]+1)
    return l


@app.route("/", methods =['POST','GET'])
def index():
    form = Form()

    if request.method == 'POST':

        income = form.income.data
        year = form.year.data
        filing_status = form.filing_status.data
        state = form.state.data

        t =  tax(state = state, income = income, filing_status = filing_status, year = year)
        state_tax_raw = t.state_tax()
        state_tax = locale.currency(state_tax_raw, grouping=True)
        fed_tax_raw = t.fed_tax()
        fed_tax = locale.currency(fed_tax_raw, grouping=True)
        fica_tax_raw = t.fica_tax()
        fica_tax = locale.currency(fica_tax_raw, grouping = True)
        income_tax = state_tax_raw + fed_tax_raw + fica_tax_raw
        if form.net_income.data:
            net_income_raw = form.net_income.data
            net_income = locale.currency(net_income_raw, grouping=True)
        else:
            net_income_raw = income-income_tax
            net_income = locale.currency(income - income_tax, grouping=True)

        age = form.age.data
        expenses = form.expenses.data
        net_worth = form.net_worth.data
        withdrawal_rate = float(form.withdrawal_rate.data)
        withdrawal_rate_str = str(form.withdrawal_rate.data)
        investment_percent = form.investment_percent.data
        investment_rate = form.investment_rate.data
        cash_percent = form.cash_percent.data
        cash_rate = form.cash_rate.data

        annual_contrib = net_income_raw - expenses
        time_span = 30

        inv = compound_interest(net_worth, investment_percent, investment_rate, time_span, annual_contrib)
        cash =compound_interest(net_worth,cash_percent,cash_rate,time_span,annual_contrib)

        y = np.sum(np.array([inv,cash]),axis=0)
        x = x_axis(time_span)

        legend = "Net Worth"
        expense_array = [expenses*(100/withdrawal_rate)]*(time_span+1)

        for i in zip(range(time_span),y):
            if i[1]>expense_array[0]:
                fi = i[0]
                nw=locale.currency(i[1], grouping=True)
                break
        # fi = fi-1
        fi_age = age + fi

        return render_template('index.html',
            form = form,
            state_tax = state_tax,
            fed_tax = fed_tax,
            fica_tax = fica_tax,
            net_income = net_income,
            expenses= expense_array,
            withdrawal_rate_str=withdrawal_rate_str,
            fi = fi,
            nw=nw,
            fi_age= fi_age,
            x=x,
            y=y,
            legend = legend)

    return render_template('index.html',
    form=form)



if __name__ == "__main__":
        app.run(debug=True)

