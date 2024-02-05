#def soma(a, b):
    #print(f'A = {a} n = {b}')
    #s = a + b
    #print(s)
#soma(b=4,a=5)
#soma(8, 9)
#soma(2, 1)
#soma(4, 1)

#def contador(*num):
    #tam = len(num)
    #print(f'Recebi os valores {num} e são ao todo {tam} números')
#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

def dobra(lst):
    for c in range(0, len(valores)):
        lst[c] *= 2
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)