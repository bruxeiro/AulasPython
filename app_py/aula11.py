# Controle de erros

try:
    divisao = 10/0
    numero = lista[2]
    x = a

except ZeroDivisionError:
    print('Não é possivel dividir um número por 0')
except IndexError:
    print('Erro ao acessar um indice inválido na lista')
except NameError:
    print('Erro ao definir uma referencia')