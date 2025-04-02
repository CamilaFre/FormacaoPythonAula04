
quiz = [

    { "pergunta": "Qual a capital do Brasil?",
      "alternativas": ["Sao Paulo", "Brasília", "Rio de Janeiro","Resende"],
      "correta": "Brasília"

    },

    {"pergunta": "Qual a capital da Alemanha?",
     "alternativas": ["Berlim", "Atenas", "Munique","Bayern"],
     "correta": "Berlim"

     },

    {"pergunta": "Qual o Deus do Submundo?",
     "alternativas": ["Zeus", "Hades", "Poseidon","Persephone"],
     "correta": "Hades"

     },

    {"pergunta": "Qual é o nome do irmão do Dexter?",
     "alternativas": ["Joey", "Harrison", "Harry","Brian"],
     "correta": "Brian"

     }

]

l = len(quiz[0]['alternativas'])
y = len(quiz)

print(l)

i = 0
c = 0

while i < y:

    print(quiz[i]['pergunta'])
    print()
    for n, valor in enumerate(quiz[i]['alternativas']):
        print(n + 1, "-", valor)
        print()
    r = input("Digite o número da alternativa correta (ou 'X' para sair):" )
    print()

    if r.lower() =="X".lower():
        break

    if r.isdecimal() and int(r) <= l:
        r = int(r)
        if (quiz[i]["alternativas"][r - 1]) == quiz[i]["correta"]:
            print("Você acertou, miserávi!!!")
            print()
            c +=1
        else:
            print("Você errou feio, errou rude!!!")
            print(f"A resposta correta é {quiz[i]["correta"]}")
            print()
    else:
        print("você digitou um valor inválido, tente novamente")
        continue

    i = i+1

taxa = c/l
print()
print(f'Você acertou {c} perguntas de {l} o que equivale a uma taxa de acertos de {taxa:.0%}  ')
