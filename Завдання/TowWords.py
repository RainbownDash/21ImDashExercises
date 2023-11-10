str1 = list(input("Введіть перше слово: "))
str2 = list(input("Введіть друге слово: "))
lenght_str = len(str2)

if str1[0] == str2[lenght_str-1]:
  print("Перша буква першого слова та остання буква другого слова - співпадають")
else: 
  print("Співпадінь немає!")