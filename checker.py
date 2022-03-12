#checkers


number = int(input('what is your number ? '))

for a in range(1,number+1) :
  for b in range (1,number+1):
    if (a+b)%2 == 0:
      print('x',end='')
    else :
      print('o',end='')
  print('')