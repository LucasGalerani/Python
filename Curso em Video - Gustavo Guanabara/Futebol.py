golsz = []
dados = {'nome': "variable", 'gols': golsz, 'total': "variable"}
partidas = 0
goleadas = 0
goleadas2 = 0
cont = 0

dados['nome'] = input("Nome do jogador: ")
partidas = input(f"Quantas partidas {dados['nome']} jogou? ")
partidasz = int(partidas)
glos = []

for c in range(1,partidasz+1):
  golsz.append(int(input(f'Quantos gols ele fez na partida {c}? ')))

for pos, goz in enumerate(golsz):
  goleadas = golsz[pos]
  goleadas2 += goleadas

goleadas3 = str(goleadas2)

dados['total'] = goleadas3

print('=-='*15)
print(dados)
print('=-='*15)

for k,v in dados.items():
  print(f'O campo {k} tem valor {v}')
print('=-='*15)
print(f"O jogador {dados['nome']} jogou {partidasz} partidas.")

glos.append(dados['gols'].copy())


for c in range(1, partidasz+1):
 print(f' => Na partida {c}, fez {glos[0][cont]} gols')
 cont+=1

print(f"Foi um total de {dados['total']} gols")