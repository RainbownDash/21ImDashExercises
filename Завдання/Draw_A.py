n = input("Введіть ")
A =[[" ", n, n, n, " ","\n"], [n, " ", " "," ", n,"\n"], [n, n, n, n, n,"\n"], [n, " ", " "," ", n,"\n"], [n, " ", " "," ", n,"\n"]]

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=" ")
      
    print()