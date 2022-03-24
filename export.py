import pandas as pd
import numpy as np
def calculateTax(income):
    tax = 0.0
    mpf=np.clip(income*0.05,0,18000)
    income_mpf = income - mpf
    Chargeable_Income = income_mpf - 132000
    if Chargeable_Income <= 50000:
        tax = Chargeable_Income*0.02
        if tax<0: tax=0
        case=1
    elif Chargeable_Income>50000 and Chargeable_Income <= 100000: 
        tax=(Chargeable_Income-50000)*.06 + 1000
        case=2
    elif Chargeable_Income > 100000 and Chargeable_Income <= 150000:  
        tax=(Chargeable_Income-100000)*.1 + 4000
        case=3
    elif  Chargeable_Income > 150000 and Chargeable_Income <= 200000:  
        tax=(Chargeable_Income-150000)*.14 + 9000
        case=4
    elif  Chargeable_Income > 200000:
        tax=(Chargeable_Income-200000)*.17 + 16000
        case=5
        if Chargeable_Income*.15+16000<tax:
            case=6
            return [round(Chargeable_Income*.15,2),6]
    return [round(tax,2),case]
df = pd.DataFrame()
for x in range(0,2000100,10000):
    [tax,case]=calculateTax(x)
    df = df.append([[x,tax,case]],ignore_index=True)
print(df)
df.to_csv('export.csv',sep=',',header=False, index=False)

