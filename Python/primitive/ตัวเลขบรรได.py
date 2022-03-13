#ตัวเลขขั้นบรรได

'''
Ex

input = 3 

output 

1
12
123

'''

number = int(input('what is your number ? '))

for row in range(1,number+1):
  for colume in range (1,row+1):
    print(colume,end='')
  print( ' ' )
  
  