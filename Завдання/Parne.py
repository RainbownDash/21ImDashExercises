for i in range(10):
  num = int(input("Введіть ціле число: "))


  if num%2 == 0 and num >= 0: 
    num += 2
  elif num%2 == 1 and num >= 0: 
    num += 1
  elif num%2 == 0 and num < 0: 
    num -= 2
  else: 
    num -= 1

  print(f"{num} наступне парне число")