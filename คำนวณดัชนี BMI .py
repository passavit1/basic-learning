#คำนวณดัชนี BMI 

'''
BMI = น้ำหนัก (KG) / ส่วนสูง (m)^2

BMI < 18.5 ต่ำกว่าเกณฑ์
BMI 18.5 - 22.90 ปกติ
BMI 23 - 24.90 น้ำหนักเกิน
BMI 25 - 29.90 อ้วนระดับ 1
BMI > 30  อ้วนระดับ 2

'''

weight = int(input('ใส่น้ำหนักของคุณ (KG) = '))
height = int(input('ใส่ส่วนสูงของคุณ (CM) = '))

BMI = weight / ((height/100)**2)

print('ค่า BMI ของคุณเท่ากับ' , BMI)

result = 'ไม่ทราบค่า'
if BMI<18.5:
  result='คุณอยู่ในเกณฑ์น้ำหนักน้อย'
elif BMI>18.5 and BMI<=22.90:
  result='คุณอยู่ในเกณฑ์ปกติ'
elif BMI>=23 and BMI<=24.90:
  result='คุณน้ำหนักเกิน'
elif BMI>=25 and BMI<=29.90:
  result='คุณอ้วนระดับ 1'
else:
  result='คุณอ้วนระดับ 2'

print(result)