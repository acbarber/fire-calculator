from tax import tax

p1 = tax(state = 'ID', income = 155000, filing_status = 'single', year = '2019')

print('state tax: ', p1.state_tax())
print('federal tax ', p1.fed_tax())
print('fica_tax ', p1.fica_tax())
