pessoas = []
dados = {}
soma = 0
media = 0

while True:
    dados['nome'] = str(input("Nome: "))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF' :
            break
        print('ERROR! digite um valor valido [M/F]')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Deseja Prosseguir? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Insira um resposta valida [S/N]: ')
    if resp == 'N':
        break

media = soma / len(pessoas)    
print('=-='*30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
print('=-='*30)
print(f'A média de idade é {media:5.2f} anos.')
print('=-='*30)
print(f'As mulheres presentes na lista são: ' , end="; ")
for f in pessoas:
    if f['sexo'] == 'F':
        print(f'{f["nome"]}', end="")
print('')
print('=-='*30)
print(f'A lista de pessoas que estão acima da média de idade são: ')
for p in pessoas:
    if p['idade'] >= media:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}; ' , end='')
            print()

print(">>>ENCERRADO<<<")