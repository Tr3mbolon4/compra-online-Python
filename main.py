print('Codigo de: [Alexandre Santos]')
print('='*35)

print('Simulando compra online no cartão')
print('='*35)
print('Senha do cartao: 123456')
print('='*35)


nome = input('Nome: ')
sobre_nome = input('Sobre Nome: ')
data_nasc = input('Data de nascimento: ')
cidade = input('Cidade: ')
estado = input('estado: ')
cpf = int(input('CPF somente Numeros: '))
numero_card = int(input('Numero do Cartão somente numero: '))
data_validade = int(input('Data de validade do Cartão Mes/ANO: '))
codigo = int(input('Codigo cartão: '))
print('='*35)

valor_compra = float(input('valor da compra: '))
print('='*35)

resumo = (f' {nome}{sobre_nome}{data_nasc}{cidade}{estado}{cpf}{numero_card}{data_validade} Efetuando uma compra Online no valor{valor_compra} confirme a compra a baixo pra efetiva a pagamento')

senha = int(input('Digita a senha: '))

for enviar in range(4):
    if senha != 123456:
      print('Senha incorreta... Apos três tentativas  bloqueio do cartão e o cancelamento da compra!')
      senha = int(input('Digita a senha: '))
      break
  
else:
    print('Compra confirmanda')
    print('E-mail com detalhes da compra enviado')

                  
    print(resumo)