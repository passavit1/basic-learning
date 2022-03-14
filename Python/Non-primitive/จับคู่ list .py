#การจับคู่สินค้าและราคา

fruit = ['apple', 'banana' , 'mango', 'orange']
price = [10,20,30,40]

for x,y in zip(fruit,price[::-1]):
  print('สินค้า' , x , 'ราคา' ,y)



#จับคู่คำ

say = ['hi' , 'hello', 'good morning' , 'good bye']
name = ['gun' , 'mark', 'sam' ]
result=[]
#ปกติ
'''
for i in say:
  for y in name:
    result.append(i+y)
print(result)
'''
#ลดรูป

result=[x+y for x in say for y in name]
print(result)


#ค้นหาจำนวนตัวอักษรใน list 

mass = ['aa' , 'bab' , 'cabcc', 'dad']
result=[]

for i in mass : 
  result.append(i.count('a'))
print(result)