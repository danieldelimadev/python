print('\033[1;36m+=+TABUADA+=+\033[m')
ch = int(input('Você quer saber a tabuada de qual número? '))
res = 0
print('-' * 15)
for c in range(1, 11):
    res = c * ch 
    print('{} X {} = {}'.format(ch, c, res))
print('-' * 15)