print("digites seu email")
email = str(input("seu email: ")).lower()
possicaoDOarroba = email.find('@')
possicaoFinal = len(email)-1
simbolos = '!#$%&*()_-+=/*-+<>;?[]{}' in email
versetemponto = email.find('.')
possicaoDoPonto = '.' in email
# se o email esta vazio
if email == '':
    print("ERRO digite alguma coisa")
# se o @ esta no lugar errado
elif possicaoDOarroba ==  0 or possicaoDOarroba == possicaoFinal:
    print("ERRO, o @ não pode estar nem no começo nem no final")
# se nao tem @
elif possicaoDOarroba == -1:
    print(" este emial nao tem @")
elif simbolos:
    print("ERRO o email nao pode ter simbolos")
elif versetemponto == 0 or versetemponto == possicaoFinal:
        print("ERRO o . nao pode estar nem no começo nem no final")
#  se tem @
elif possicaoDOarroba > 1:
    aposArooba = email[possicaoDOarroba+1]
    possicaoDoPontoAPosarroba = '.' in aposArooba
    
    if possicaoDoPonto == False:
        print(" este arroba precosa de um ponto")
    elif aposArooba == 0 or aposArooba == possicaoFinal:
        print("ERRO o . nao pode estar nem no começo nem no final")
    else:
         print("EMAIL VALIDO")