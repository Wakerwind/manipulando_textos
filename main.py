#------fatiamento-----

frase = 'curso em video de python'
print(f'{frase[9]}')
#imprime do index 0 até 14-1
#Vamos imprimir os elementos da string até antes da posição do elemento depois de :
print(f'{frase[0:14]}')

#Quando omitimos o inicio ele começa do 0
print(f'{frase[:5]}')
#imprime de 0 até 13 pulando de 2 em 2
print(f'{frase[0:14:2]}')

#imprime do 15 até o final
print(f'{frase[18:]}')

#-----Análise------

#tamanho da string
print('Tamanho da frase: ',len(frase))

#quantidade de ocorreência de um elemento
print('Quantas vezes a letra o aparece: ',frase.count('o'))

#quantidade de ocorreência de um elemento entre um intervalo
print('Quantas vezes a letra o aparece entre 0 e 13: ',frase.count('o',0,13))

#retorna a posição onde começa encontra esse elemento na frase
#retorna -1 se não encontrar
print('Em que posição eu tenho deo: ',frase.find('deo'))

#O operador in verifica a existencia de um elemento em uma lista e retorna True ou False
print(f'A frase tem a palavra curso? ','curso' in frase)

#------Transformação------
#Troca um elemento de uma lista por outro
print('Vamos trocar a palavra python na frase por android: ',frase.replace('python','android'))

#converte a frase para maiúscula
print('Frase em maiúscula: ',frase.upper())

#converte a frase para minúscula
print('Frase em minúscula: ',frase.lower())

#Transforma a primeira letra da frase em maiúscula e o resto em minúscula
print('Primeira letra em maiúscula: ',frase.capitalize())

#Analisa cada palavra na frase e coloca a primeira letra de cada em maiúscula
print('Primeira letra de cada palavra em maiúsculo: ',frase.title())

frase2 = '   Amo aprender python!    '
#Corta os espaços em branco nas extremidades da frase
print('Frase com os espaços: ',frase2)
print('Frase sem os espaços nas extremidades: ',frase2.strip())
print('Frase sem os espaços na extremidade direita: ',frase2.rstrip())
print('Frase sem os espaços na extremidade esquerda: ',frase2.lstrip())

#Divisão
#separa as palavras da string de acordo com os epaços da string
#Pode separar de acordo com outros parametros como: / ou , ou ;
#Gera uma lista com os elementos separados
print('Frase com as palavras separadas de acordo com os epaços da string: ',frase.split())

frase = frase.split()
print(frase)
#Join junta cada string em uma só e separa cada palavra com um caractere que escolhermos
print('-'.join(frase))



