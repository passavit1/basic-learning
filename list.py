#list

#primitive
'''
a=1
b=2
c=3
d=4
'''

#non-primitive : list 

number = [] #list เปล่า 
number = [1,2,3,4,5,6,7] #list มีสมาชิก 1-4
name=['a','b','c','d','e']

#construtor

#name=list(['a','b','c','d'])

#การเข้าถึงข้อมูล

print(name[1:4])
print(name[-4:-2])
print(len(number))
print('done \n')

#การแก้ไขข้อมูล

print('before' , number)
number[2]=9
print('after' , number)
print('done \n')

#loop

sum=0 
for x in number :
  sum+=x
print(sum)
print('done \n')

#check

print(name)
if 'a' in name:
  print('have a in name')
else:
  print('no a in name')
print('done \n')

#loop in range by len

for i in range(len(name)): #นับจำนวนสมาชิก
  print(name[i])

for z in name: #ปริ้นทั้งหมด
  print(z)
print('done \n')

#การเพิ่มข้อมูล (ต่อท้าย)

print('before' , name)
name.append('f')
print('after' , name)
print('done \n')

#insert (แทรก)

print('before' , name)
name.insert(1,'k') #แทรกที่ index ที่ 1 
print('after' , name)
print('done \n')

#ลบสบมาชิกออกจาก list

#ลบข้อมูลออกจาก list remove ระบุข้อมูลที่จะลบ

print('before' , name)
name.remove('k')
print('after' , name)
print('done \n')

#POP เอาสมาชิกหลังสุดออก

print('before' , name)
name.pop()
print('after', name)
print('done \n')

#Del ลบจากตำแหน่งสมาชิก

print('before' , name)
del name[2]
#del name สามารถลบทั้ง list ได้เลย
print('after', name)
print('done \n')

#clear ล้างสมาชิกออกจาก list กลายเป็น list เปล่า

print('before' , name)
name.clear()
print('after', name)
print('done \n')

#การคัดลอกข้อมูล

name=number.copy()
print('before' , name)
print('done \n')

#การรวมข้อมูล

merge = number + name 
print(merge)
print('done \n')

#แสดงจำนวนสมาชิก count 

j = merge.count(5)
print('จำนวนเลข 5 ใน merge มีทั้งหมด ' , j , 'ตัว')
print('done \n')

#extend นำข้อมูลจาก list หนึ่งไปอีก list โดยไม่ต้องสร้างตัวแปรใหม่

name.clear()
name.append('a')
name.append('b')
name.append('c')
print('before name' , name)
print('before number ' , number)

name.extend(number)

print('after extend ' , name)