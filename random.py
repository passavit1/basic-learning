#Random


import random 

myrandom = random.randrange(1,7) #1-4
round = 0

while True :
  number = int(input('what is your number ? '))
  correct = number==myrandom 

  if correct :
    print('correct you won')
    break
  else :
    if number > myrandom :
      print('higher')
    else :
      print('lower')
  if round == 2 :
    break
  round+=1

if not correct : 
  print ('you lose')  
  print ('the answer is ' , myrandom)

  