'''

โครงสร้างควบคุม (control structure)
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซ้ำ

'''

# 2.แบบเลือก

'''
if boolean expression: #ถูกต้องให้ทำอะไร
  statement
elif : #เงื่อนไขเพิ่มเติมกรณี if ไม่ถูกต้อง
  statement
else:
  statement
'''

#CODE

'''
age = int(input('How old are you ? = '))

if age >= 15: #ระบุเงื่อนไข 
  print('Yor are a man')
else: #กรณีที่ไม่เป็นจริง
  print('You are a BOY')
'''

#Exam

'''
age = 1-10 = Child
age = 11-20 = teen
age = 21+ = adult
'''

age = int(input('How old are you ? = '))

'''
if age>=21:
  print('You are a adult')
elif age>=11 :
  print('You are a teen')
else:
  print('You are a child')
'''

#Ternary Operator
#ใช้ if else ในบรรทัดเดียว

print('motherfucker') if age>21 else print('surprice')