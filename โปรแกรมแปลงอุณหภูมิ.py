#โปรแกรมแปลงอุณหภูมิ

'''
C = (f - 32) * (5/9)
F = (C * (9/5)) + 32 
'''

#แปลง เซลเซี่ยสเป็ฟาเรนไฮน
'''
C=float(input('what is your C ? ='))
F=(C * (9/5)) + 32 
print(F)
'''

#แปลง F เป็น C

temp = input('ป้อนอุณหภูมิ (องศา) : ')

degree= float(temp[:-1])
unit=temp[-1]

unit=unit.upper()


if unit=='F':
  print('อุณหภูมิ ', temp[:-1] , unit , '=', (degree - 32) * (5/9) , 'C')
elif unit=='C':
  print('อุณหภูมิ ' , temp[:-1] , unit , '=' , (degree * (9/5)) + 32 , 'F')