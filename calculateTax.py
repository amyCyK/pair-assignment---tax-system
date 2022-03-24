#Group members:
#Law Hong Chun Zachary (56237888)
#Chan Yik Kit Amy (56237852)
#Martinez Kiel Marc (57162491)
#Prentation Time: 1300-13:10

import numpy as np
def calculateTax(income,married=False):
    tax = 0.0
    mpf=np.clip(income*0.05,0,18000)
    income_mpf = income - mpf
    if married:Chargeable_Income= income_mpf - 264000
    else: Chargeable_Income = income_mpf - 132000
    if Chargeable_Income <= 50000:
        tax = Chargeable_Income*0.02
        if tax<0: tax=0
    elif Chargeable_Income <= 100000:tax=(Chargeable_Income-50000)*.06 + 1000
    elif Chargeable_Income <= 150000:tax=(Chargeable_Income-100000)*.1 + 4000
    elif Chargeable_Income <= 200000:tax=(Chargeable_Income-150000)*.14 + 9000
    elif Chargeable_Income > 200000:
        tax=(Chargeable_Income-200000)*.17 + 16000
        if Chargeable_Income*.15+16000<tax:return round(Chargeable_Income*.15,0)
    return int(tax)