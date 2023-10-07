
nome = input('Digite seu nome completo: ')

print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')

#Separo o nome depois junto com join sem separar as palavras do nome, depois conto isso
tam = ''.join(nome.split())
print('Tamanho do seu nome: ',len(tam))

#Separo o nome e uso len() pra saber o tamanh do primeiro elemento da lista gerada
primeiro = nome.split()
print('Tamanho do seu primeiro nome: ',len(primeiro[0]))




