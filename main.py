#Draft from Amy 25.02.2022
#Sample: https://www.ird.gov.hk/eng/ese/st_comp_2020_21_budget/stcfrm.htm
#MPF GOrv:https://www.gov.hk/en/residents/taxes/salaries/allowances/deductions/mpf.htm
#240000 480000 13000 38950
#288000 mpf=14400 result=8160
import numpy as np
def calculateTax(income):
    tax = 0.0
    mpf=np.clip(income*0.05,0,18000)
    income_mpf = income - mpf
    Chargeable_Income = income_mpf - 132000
    if Chargeable_Income <= 50000:
        tax = Chargeable_Income*0.02
        if tax<0: tax=0
    elif Chargeable_Income>50000 and Chargeable_Income <= 100000: 
        tax=(Chargeable_Income-50000)*.06 + 1000
    elif Chargeable_Income > 100000 and Chargeable_Income <= 150000:  
        tax=(Chargeable_Income-100000)*.1 + 4000
    elif  Chargeable_Income > 150000 and Chargeable_Income <= 200000:  
        tax=(Chargeable_Income-150000)*.14 + 9000
    elif  Chargeable_Income > 200000:
        tax=(Chargeable_Income-200000)*.17 + 16000
        if Chargeable_Income*.15+16000<tax:
            print('Extreme case')
            return round(Chargeable_Income*.15,0)
    return round(tax,0)

if input("Are you single?: (Y/N) ").lower() in ['Y','Yes','yes','y']:
    print('The tax is: '+str(calculateTax(float(input("Enter the annual income: ")))))
else:
    income_husband = float(input("Enter the husband annual income: "))
    income_wife = float(input("Enter the wife annual income: "))
    individual_allowance=132000
    joint_allowance=264000
    income = income_husband + income_wife
    tax_total=calculateTax(income-joint_allowance)
    tax_husband=calculateTax(income_husband-individual_allowance)
    tax_wife=calculateTax(income_wife-individual_allowance)
    print('Joint Tax Payable: '+str(tax_total))
    print('Husband Tax Payable: '+str(tax_husband))
    print('Wife Tax Payable: '+str(tax_wife))
    if tax_husband+tax_wife>tax_total: print('Recommend Joint Payment')
    else:print('Recommend Seperate Payment')


