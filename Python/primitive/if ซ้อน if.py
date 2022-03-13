#if ซ้อน if 

"""
จัดระดับชั้น
อายุ 13 = m1
    14 = m2
    15 = m3
    16 = mp
    <= 13 = p
"""

age = int(input('How old are you ? = '))

if age<=15:
  if age==15:
    pass #กรณีใช้ pass เผื่อเวลายังไม่สามารถระบุการทำงานด้านในได้
  elif age==14:
    print('m2')
  elif age==13:
    print('m1')
  else:
    print('p')
else :
  print('mp')
