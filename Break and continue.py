#break , continue

#break 
'''
i=1

while i<=10:
  print('round' , i)
  if i==5:
    break #จบโปรแกรมเลยไม่ไปทำ else ต่อ 
  i+=1
else : 
  print('done')

'''

#continue

'''
i=0

while i<=10:
  i+=1
  if (i%2 != 0):
    continue #จะไม่ปริ้นรอบที่ 5 
  print('round' , i)
else : 
  print('done')
'''

for i in range (1,11):
  if i == 5:
    continue
  print('number' , i)
else :
  print('done')