apple = int(input("Кількість яблук було: "))
pupils = int(input("Кількість учнів що беруть по одному яблуку:"))

if apple < pupils:
  print("Яблук менше ніж учнів. Спробуй раз.")

  not_enought = pupils - apple
  
  if not_enought == 1:      
    print(f"{not_enought} учень лишивмя без одного яблука!")
  else:
    print(f"{not_enought} учнів зовсім не отримали яблук")
    
else:
  rest = apple - pupils

  print(f"Лишилося {rest} яблук(а, о)")