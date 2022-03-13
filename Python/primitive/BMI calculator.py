# BMI Calculate 
'''
สมการ 
BMI = น้ำหนัก (KG) / ส่วนสูง(m) ยกกำลังสอง
'''

'''
weight = int(input('ใส่น้ำหนัก (กิโลกรัม) = '  ))
tall = float(input('ใส่ส่วนสูง (เมตร) = '  ))

BMI = weight/(tall**2)
print('ค่า BMI ของคุณเท่ากับ = ' , BMI)
'''

weight = int(input('ใส่น้ำหนัก (กิโลกรัม) = '  ))
tall = float(input('ใส่ส่วนสูง (เซ็นติเมตร) = '  ))

BMI = weight/((tall/100)**2)
print('ค่า BMI ของคุณเท่ากับ = ' , BMI)