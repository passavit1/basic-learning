#index

name = '  Passavit.  ' #index => 0
print(name[2:6]) #ตำแหน่งเริ่มต้น = 0 : ตำแหน่งสุดท้าย = ตำแหน่งนั้นๆ
print(name[-6:-3]) #นับตำแหน่งสลับ กับ อันบน

print(len(name)) #นับความยาว String 

name = name.strip() #ลบช่องว่างซ้ายขวา #lstrip #rstrip

print(len(name))
print(name)

name = name.upper() #ทำเป็นพิมพ์ใหญ่
print(name)

name = name.lower() #ทำให้เป็นตัวพิมพ์เล็ก
print(name)

name = name.capitalize() #ตัวแรกเป็นตัวพิมพ์ใหญ่
print(name)

print(name.replace('Pass','Jazz')) #แทนที่คำ
print(name.replace('s','k',1)) #แทนที่คำ จำนวน 1 คำ

print(name)

name = 'i going to the market'
x = input('ใส่คำที่ต้องการค้นหา = ') in name # เช็คว่ามีคำว่า vit อยู่ในคำรึเปล่า
print(x)

if x:
  name = name.replace('market','home')

print(name)

