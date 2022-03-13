#ป้อนตัวเลขหาผลรวม

'''
รับตัวเลขหาผลรวมเท่าไหร่

'''

#หาผลรวม เงื่อนไข กำหนดจำนวนรอบตอนแรก

'''
start , stop = 1,5
sum,avg=0,0

while start<=stop:
  number=int(input('what is your number ? = '))
  sum+=number #รวมผล sum ในแต่ละรอบ
  start+=1 #ให้โปรแกรมรับค่าทั้งหมด 5 ค่า 

avg = sum/stop

print('your sum ' , sum)
print('your avg ' , avg)
'''

#หาผลรวม เงื่อนไข ผลรวมไม่เกิน 100

sum = 0

while True :
  number = int(input('input your number = '))
  sum+=number
  print('sum now = ' , sum )
  if sum>100 :
    break #จบการทำงานทันที
