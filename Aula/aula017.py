#num = [2, 5, 9, 1]
#num[2] = 3
#num.append(7)
#num.sort(reverse = True)
#num.insert(2, 2)
# remove o primeiro que aparecer na lista
#num.remove(2)
#print(num)
#print(f'Essa lista tem {len(num)} elementos')

valores = []
for c in range(0,5):
    valores.append(int(input('Digite um número:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')