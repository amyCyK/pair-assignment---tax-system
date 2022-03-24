#Group members:
#Law Hong Chun Zachary (56237888)
#Chan Yik Kit Amy (56237852)
#Martinez Kiel Marc (57162491)
#Prentation Time: 1300-13:10

from calculateTax import *
if input("Are you single?: (Y/N) ").lower() in ['Y','Yes','yes','y']:
    print('The tax is: '+str(calculateTax(float(input("Enter the annual income: ")))))
else:
    income_husband = float(input("Enter the husband annual income: "))
    income_wife = float(input("Enter the wife annual income: "))
    income = income_husband + income_wife
    tax_total=calculateTax(income,True)
    tax_husband=calculateTax(income_husband,True)
    tax_wife=calculateTax(income_wife,True)
    print('Joint Tax Payable: '+str(tax_total))
    print('Husband Tax Payable: '+str(tax_husband))
    print('Wife Tax Payable: '+str(tax_wife))
    if tax_husband+tax_wife>tax_total: print('Recommend Joint Payment')
    else:print('Recommend Seperate Payment')