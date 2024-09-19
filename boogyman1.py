intrest = float(input('annual intrest rate:'))
month =  float(input('no.month:'))
amount = float(input('lone amount:'))
date =float(input('added date:'))
persentage = intrest/100
m =persentage/12
date_intrest = persentage/365 
T = (m*amount*month) + (date_intrest*amount*date)
print(T)
