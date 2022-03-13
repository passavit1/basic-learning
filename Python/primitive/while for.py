#LOOP โครงสร้างควบคุมแบบทำซ้ำ 

#while

'''

while expression :
  statement

i=1
sum=0
average=0
round= int(input('ใส่จำนวนรอบ = '))

while i<=round:
  sum+=i
  i+=1

print('ผมรวมเท่ากับ' ,sum)
print('ค่าเฉลี่ยเท่ากับ' , sum/round)

'''

#for

'''

for i in range(start , stop , step):
  statement
  
'''

sum=0
round=int(input('round = '))

for i in range (1,round+1):
  sum+=i
  print('ผลรวมรอบที่' , i , 'เท่ากับ' , sum)

print('ผมรวมทั้งหมด =' , sum)
print('ค่าเฉลี่ย', round , 'รอบ เท่ากับ =' , sum/round)