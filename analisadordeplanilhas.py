import csv
#declara variavel de deslocamento de linha e a pontuaçao das acoes
e=0
p=0
c1=0
c2=0
c3=0
c4=0
#scaneia os arquivos
print('escreva o nome do primeiro arquivo:')
arq1=input()
print('escreva o nome do segundo arquivo:')

arq2=input()
if arq2=="":
    print('nenhum arquivo iniciado')
    r2=""
else:
    a2=open(arq2+'.csv','r')
    r2=csv.reader(a2)
print('escreva o nome do terceiro arquivo:')

arq3=input()
if arq3=="":
    print('nenhum arquivo iniciado')
else:
    a3=open(arq3+'.csv','r')
    r3=csv.reader(a3)
print('escreva o nome do quarto arquivo:')

arq4=input()
if arq4=="":
    print('nenhum arquivo iniciado')
else:
    a4=open(arq4+'.csv','r')
    r4=csv.reader(a4)

#abre o arquivo csv e o leitor do modulo csv
a1=open(arq1+'.csv','r')
r1=csv.reader(a1)

#declara o arquivo como uma lista
linha1=list(r1)
linha2=list(r2)
linha3=list(r3)
linha4=list(r4)
#declara cada linha como uma lista
choice1=list(linha1)
choice2=list(linha2)
choice3=list(linha3)
choice4=list(linha4)
#função que compara e imprime a melhor opção entre as ações

while p<4:
 while e < 26 :
   choice1=list(linha1[e])
   choice1f=float(choice1[p].replace('.','').replace(',','.'))
   choice2=list(linha2[e])
   choice2f=float(choice2[p].replace('.','').replace(',','.'))
   choice3=list(linha3[e])
   choice3f=float(choice3[p].replace('.','').replace(',','.'))
   choice4=list(linha4[e])
   choice4f=float(choice4[p].replace('.','').replace(',','.'))

   if choice1f>choice2f and choice1f>choice3f and choice1f>choice4f:
          c1 += 1
   if choice2f>choice1f and choice2f>choice3f and choice2f>choice4f:
          c2 += 1
   if choice3f>choice1f and choice3f>choice2f and choice3f>choice4f:
          c3 += 1
   if choice4f>choice1f and choice4f>choice2f and choice4f>choice3f:
          c4 += 1

   
   e += 1
 p +=1

if c1>c2 and c1>c3 and c1>c4:
     print("a melhor opcao ",arq1)
if c2>c1 and c1>c3 and c1>c4:
     print("a melhor opcao ",arq2)
if c3>c1 and c3>c2 and c3>c4:
     print("a melhor opcao ",arq3)
if c4>c1 and c4>c2 and c4>c3:
     print("a melhor opcao ",arq4)












       
     
