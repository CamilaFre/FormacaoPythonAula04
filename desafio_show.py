
quiz = [

    { "pergunta": "Qual a capital do Brasil?",
      "alternativas": ["Sao Paulo", "Brasília", "Rio de Janeiro"],
      "correta": "Brasília"

    },

    {"pergunta": "Qual a capital da Alemanha?",
     "alternativas": ["Berlim", "Atenas", "Munique"],
     "correta": "Berlim"

     },

    {"pergunta": "Qual o Deus do Submundo?",
     "alternativas": ["Zeus", "Hades", "Poseidon"],
     "correta": "Hades"

     }
]

l = len(quiz)

print(l)

i = 0
c = 0

while i < l:

    print(quiz[i]['pergunta'])
    for n, valor in enumerate(quiz[i]['alternativas']):
     
        print(n + 1, "-", valor)
    r = input( )
    if r.isdecimal() and int(r) <= 3:
        r = int(r)
        if (quiz[i]["alternativas"][r - 1]) == quiz[i]["correta"]:
            print("Você acertou, miserávi!!!")
            c +=1
        else:
            print("Você errou feio, errou rude!!!")
    else:
        print("você digitou um valor inválido, tente novamente")
        continue

    i = i+1

taxa = c/l
print(f'Você acertou {c} perguntas de {l} o que equivale a uma taxa de acertos de {taxa:.0%}  ')
