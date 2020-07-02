
def escrever_arquivo(texto):


    arquivo = open('teste.txt', 'w')

    arquivo.write ('segunda linha')

    arquivo.close()

def atualizar_arquivo(texto):

    arquivo = open('teste.txt', 'a')

    arquivo.write(texto)

    arquivo.close()

def ler_arquivo(nome_arquivo):

    arquivo = open(nome_arquivo, 'r')

    texto = arquivo.read()

    print(texto)



if __name__ == '__main__':

    # atualizar_arquivo('Segunda linha \n'
    #                   )

    ler_arquivo('teste.txt')