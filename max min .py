#ค้นหาตัวเลข มากสุด น้อยสุด

max , min = 0,9999

while True :
  number = int(input('what is your number ? '))
  if number < 0 :
    break
  if number > max  :
    max=number 
  if number < min :
    min = number 

  
  print('your max number is ' , max)
  print('your min number is ' , min)
