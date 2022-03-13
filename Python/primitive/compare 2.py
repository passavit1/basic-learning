#and = และ
#or = หรือ 
#not = ไม่

#คำตอบที่ได้ = True / false

a=int(input('Number A = '))
b=int(input('Number B = '))

x=a>3 and b>2
y=a>3 or b>2
z=a>3 or b>5

print(x)
print(y)
print(z) 
print(not z) #print ค่าตรงข้ามค่า Z