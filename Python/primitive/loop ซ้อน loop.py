#loop ซ้อน loop

'''
i=1
while i<=3:
  j=1 #ตัวนับ 
  while j<=5:
    print('round' , i ,'point' , j)
    j+=1
  i+=1
'''

#i

for i in range(1,4):
  print('round' , i)
  for j in range (1,6):
    print ('round' , i , 'task', j) 