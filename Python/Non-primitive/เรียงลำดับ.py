#รับและเรียงข้อมูลตัวเลข


number =[]

'''
while True :
  x=int(input('what is your number ? = '))
  if x<0:
    break
  number.append(x)
    
  print('before' , number)
  number.sort() #เป็นคำสั่งเรียงจากน้อยไปมาก
  print('after' , number)
  number.reverse() #เรียงจากมากไปน้อย
  print('after reverse' , number)
  print('done\n')
'''

#หาตัวเลขต่ำสุดน้อยสุด min , max , sum

number.append(1)
number.append(2)
number.append(3)
number.append(4)
number.append(5)
number.append(6)
print('list number = ' , number )
print('min' , min(number))
print('max' , max(number))
print('sum' , sum(number))

#แยกเลขคู่เลขตี่ 

odd = [] #เลขคี่
even = [] #เลขคู่
number.clear()
while True :
  x=int(input('what is your number ? = '))
  if x<0:
    break
  if x%2==0:
    even.append(x)
  else:
    odd.append(x)
  number.append(x)
even.sort()
odd.sort()
print('all number', number)
print('เลขคู่มีเลข' , even)
print('เลขคี่มีเลข' , odd)
    
#เรียงลำดับชื่อ

name=['red','black','white','pink']
name.sort()
print(name)

#เรียงจากหลังสุด มาหน้าสุด

fruit = ['apple', 'banana' , 'mango', 'orange']
print('before' , fruit)
fruit=fruit[::-1]
print('After' , fruit)