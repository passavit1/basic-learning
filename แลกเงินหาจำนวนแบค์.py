#แลกเงินหาจำนวนแบค์

money = int(input('how much money do you have ? = '))

if money>1000:
  print('แลกแบงค์ 1000 ได้ ' , int(money/1000) , 'ใบ')
  money=money%1000
if money>500:
  print('แลกแบงค์ 500 ได้ ' , int(money/500) , 'ใบ')
  money=money%500
if money>100:
  print('แลกแบงค์ 100 ได้ ' , int(money/100) , 'ใบ')
  money=money%100
if money<100:
  print ('คุณเหลือเงินจำนวน' , money , 'บาท')
