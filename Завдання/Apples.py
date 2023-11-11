pupils = int(input("Введіть кількість учнів: "))
apple = int(input("Ведіть скільки яблук у кошику: "))


#Розділення яблук порівно
ApplesForAll = apple // pupils
#Залишок яблук у кошику
ApplesInABasket = apple % pupils

print(f"Учні отримали по {ApplesForAll} яблук(а)")
print(f"У кошику лишилося {ApplesInABasket} яблук(а)")
