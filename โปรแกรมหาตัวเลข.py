"""
เขียนโปรแกรมหาตัวเลข มาก / น้อย
"""

#หาเลขมากกว่า น้อยกว่า
'''
a = int(input('what is your first number ? = '))
b = int(input('what is your second number ? = '))


if a>b:
  print('a มากกว่า b อยู่ ', a-b )
else :
  print('b มากกว่า a อยู่ ', b-a)

'''

#หาเลขคู่คี่

a = int(input('what is your number ? = '))


if a%2>0:
  print('เลขคี่')
else :
  print('เลขคู่')