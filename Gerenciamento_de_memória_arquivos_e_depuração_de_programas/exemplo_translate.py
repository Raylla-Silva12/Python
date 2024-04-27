
def words(filename):
    # Retorna a lista de palavras reais, sem pontuação
    arq = open(filename, 'r')
    content = arq.read()
    arq.close()
    table = str.maketrans('!,.:;?', 6*' ')
    content = content.translate(table)
    content = content.lower()
    return content.split()


words('teste.txt')




def meuGrep(nomearq, alvo):
    # Exibe cada linha do arquivo que contém a string alvo
    arqEntrada = open(nomearq, 'r')
    for linha in arqEntrada:
        if alvo in linha:
            print(linha, end='')

alvo = 'alvo'
meuGrep('teste.txt', 'alvo')
