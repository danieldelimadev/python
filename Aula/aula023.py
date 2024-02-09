try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir por zero.')
except KeyboardInterrupt:
    print('Saindo')
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Volte sempre!')
