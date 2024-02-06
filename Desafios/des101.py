def vote(a):
    from datetime import date
    i = date.today().year - a
    if i < 16: 
        return f'Com {i} anos: NÃO VOTA.'
    elif 16 <= i < 18:
        return f'Com {i} anos: VOTO OPCIONAL.'
    elif 18 <= i < 65:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {i} anos: VOTO OPCIONAL.'
    
    
print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(vote(ano))