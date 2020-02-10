# ---- Imprimir info na tela
#----------ctrl+K ctrl+c
# print('\n')
# print('canalhas'*10)
# print('Ola', 'Chimbinha', 'guitarrista')
# print('a' + 'lua' +  'me' = 'traiu')
# print('\n')

#----- pegar entrada do usuario
nome = input("digite o nome")
sobrenome = input('digite seu sobrenome')

#----- Usando a funcao format para concatenação de string
print(' ola {} {}'.format(nome, sobrenome))

#---- interpolação de string
print(f'ola {nome} {sobrenome}')