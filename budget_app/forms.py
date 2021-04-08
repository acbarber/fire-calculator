from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField, FloatField
from wtforms.validators import DataRequired, Length
#
class Form(FlaskForm):
    states=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]
    tax_years = [('2020','2020'),('2019','2019')]
    statuses = [('single','single'),('married','married')]

    income = IntegerField('Annual Income ($)',default=65000)
    year = SelectField(label='Tax Year',choices=tax_years,default=2020)
    filing_status = SelectField(label='Filing Status',choices=statuses,default=statuses[0])
    state = SelectField(label='State',choices = states,default=states[0])

    net_income = IntegerField('Income after taxes ($)')

    age = IntegerField('Current Age',validators= [DataRequired()],default=30)
    expenses = IntegerField('Annual expenses ($)',default=30000)
    net_worth = IntegerField('Current Net Worth ($)',default=100000)
    withdrawal_rate = FloatField('Expected Rate of Withdrawal (%)',default=4.0)

    investment_percent = IntegerField('Investment Allocation (%)',default=80)
    cash_percent = IntegerField('Cash Allocation (%)',default=20)

    investment_rate = IntegerField('Investment Return Rate (%)',default=10)
    cash_rate = IntegerField('Rate of return for cash (%)',default=2)


    submit = SubmitField('Submit')
