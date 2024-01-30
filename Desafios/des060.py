    #Utilizando for
#from os import system
#import math
#s = '*'
#f = ''
#system('cls')
#print('''
#\033[1mDESCUBRA O FATORIAL 
#         DE         
#  QUALQUER NÚMERO     \033[m''')
#print()
#n = int(input('\033[0;36mDigite um número: \033[m'))
#p = math.factorial(n)
#for c in range(n, 0, -1):
#    if c == 1:
#        s = ('= {}'.format(p))
#    if c == n:
#        f = '! ='
#    print(c,'{}'.format(f), end=' {} '.format(s))
#    f = ''
#    print(end='')


    #utilizando while
from os import system
import math
system('cls')
print('''
\033[1mDESCUBRA O FATORIAL 
         DE         
  QUALQUER NÚMERO     \033[m''')
print()
n = int(input('\033[0;36mDigite um número: \033[m'))
p = math.factorial(n)
s = '*'
c = n
f = ''
while c != 0:
    if c == n:
        f = '!'
        s = '= '
    if c == 1:
        s = '= {}'.format(p)
    print(c, f, end=' {} '.format(s))
    s = '*'
    f = ''
    c = c - 1