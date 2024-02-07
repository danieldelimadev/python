def grade(*a, sit = False):
    """Calcula a média de um aluno"""
    Dict = {}
    Dict['total'] = len(a)
    Dict['maior'] = max(a)
    Dict['menor'] = min(a)
    Dict['média'] = sum(a) / len(a)  
    if sit == True:
        if Dict['média'] < 5:
            Dict['situação'] = 'RUIM' 
        elif Dict['média'] >= 5 and Dict['média'] < 7:
            Dict['situação'] = 'RAZOAVEL'
        else:
            Dict['situação'] = 'BOA'
    return Dict


a = grade(5.5, 2.5, 1.5, sit=True)
print(a)

