#Draft from Amy 25.02.2022
#Sample: https://www.ird.gov.hk/eng/ese/st_comp_2020_21_budget/stcfrm.htm
#MPF GOrv:https://www.gov.hk/en/residents/taxes/salaries/allowances/deductions/mpf.htm
#240000 480000 13000 38950
#288000 mpf=14400 result=8160
import numpy as np
is_singleperson = input("Are you single?: (Y/N) ")
if is_singleperson.lower() in ['Y','Yes','yes','y']:
    income = float(input("Enter the annual income: "))
else:
    income_husband = float(input("Enter the husband annual income: "))
    income_wife = float(input("Enter the wife annual income: "))
    income = income_husband + income_wife

tax = 0.0
#income - MPF Deduction = income_mpf
mpf=np.clip(income*0.05,0,18000)
print(mpf)
income_mpf = income - mpf
#income_mpf - allowance deduction
income_allowance = income_mpf - 132000
if income_allowance <= 50000:
    tax = income_allowance*0.02
    if tax<0: tax=0
else:
    tax=(income_allowance-50000)*.02 + 1000
if income_allowance < 100000:    
    tax=(income_allowance-50000)*.06 + 1000
elif income_allowance > 100000 and income_allowance < 150000:
    tax=(income_allowance-100000)*.1 + 4000
elif  income_allowance > 150000 and income_allowance < 200000:
    tax=(income_allowance-200000)*.14 + 9000
else :
    tax=(income_allowance-200000)*.17 + 16000
tax = round(tax,0)
print("The tax is:", tax)