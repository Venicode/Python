#importa a biblioteca random com a função choice
from random import choice

placarVitorias = 0
placarDerrotas = 0

#lista com cada arquivo das artes dos frames da forca
forcas = ["asciiArtes/forca0.txt", "asciiArtes/forca1.txt","asciiArtes/forca2.txt","asciiArtes/forca3.txt",
         "asciiArtes/forca4.txt","asciiArtes/forca5.txt","asciiArtes/forca6.txt","asciiArtes/forca7.txt"]

#caminho para a arte do titulo do jogo da forca
artePrincipal = "asciiArtes/jogodaForca.txt"

traco = "_"*60

def espaco():
    espaco = " "*55
    return espaco

#funcoes para printar as artes do txt no programa
def asciiArt(arte):
     with open (arte,encoding="utf-8") as arte:
        for linha in arte:
                print(linha.strip())
                
def asciiArtForca(arte):
     with open (arte,encoding="utf-8") as arte:
        for linha in arte:
                print(linha)
    
while True:
    asciiArt(artePrincipal)
    print(traco,"Menu".upper(),traco)
         
    #menu do jogo, onde cada opção contem o caminho das listas de palavras de acordo com o tema
    listaTemas = {'1-Jogos':'temas/jogos.txt','2-Filmes':'temas/filmes.txt','3-Músicas':'temas/musicas.txt',
                  '4-Tecnologia':'temas/tecnologia.txt','5-Esportes':'temas/esportes.txt','6-Assuntos Gerais':'temas/geral.txt'}
    for i in listaTemas.keys():
        print(espaco(),i.upper(),espaco())

    resposta = int(input("\nEscolha um tema para jogar:".upper()))

    if resposta == 1:
        arquivo = listaTemas["1-Jogos"]
    if resposta == 2:
        arquivo = listaTemas["2-Filmes"]
    if resposta == 3:
        arquivo = listaTemas["3-Músicas"]
    if resposta == 4:
        arquivo = listaTemas["4-Tecnologia"]
    if resposta == 5:
        arquivo = listaTemas["5-Esportes"]
    if resposta == 6:
        arquivo = listaTemas["6-Assuntos Gerais"]

    palavras = []

    #abre o arquivo palavras.txt e lê cada linha.
    with open (arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    #com a função choice, escolhe aleatoriamente uma palavra dentro do arquivo para ser a palavrasecreta
    palavrasecreta = choice(palavras).upper()
    letrasC = ""
    letrasE = ""
    contador = 0
    while True:
        pista = ""
        asciiArtForca(forcas[contador])
        #percorre cada letra da palavra secreta e verifica se a letra que o usuário digitou contém nela
        for letra in palavrasecreta:
            if letra in letrasC:
                pista += letra
            #caso não contenha, aparece o _ no lugar da letra
            else:
                pista += "_ "
        print(pista)

        #quando não tiver mais nenhum _ , quer dizer que o usuário acertou a palavra
        if "_" not in pista:
            print("Voce ganhou")
            placarVitorias+=1
            break

        #caso o usuário erre 6 vezes as letras da palavra secreta, ele perde o jogo
        if len(letrasE)==7:
            asciiArtForca(forcas[7])
            print("Game over")
            print("A palavra secreta era", palavrasecreta)
            print("Tentativas erradas:",len(letrasE))
            placarDerrotas+=1
            break
        letra = input("Digite uma letra: ").upper()
        #verifica se a letra digitada é apenas 1 e que não é um número
        if len(letra) !=1 or not letra.isalpha():
            print("Digite apenas 1 letra.")
            continue
        #se a letra já tiver sido armazenada na variavel letrasC ou letrasE, quer dizer que já foi digitada.
        if letra in letrasC or letra in letrasE:
            print("Letra já digitada")
            continue
        #se a letra tiver na palavra secreta, acrescenta na variavel letrasC
        if letra in palavrasecreta:
            letrasC+=letra
        #se não, acrescenta na variável letrasE
        else:
            letrasE+=letra
            contador +=1
            asciiArtForca(forcas[contador])

#quando o usuario acertar ou errar 6 vezes, irá aparecer a pergunta de jogar novamente
    pergunta = input("Deseja jogar novamente? Se sim digite sim, se não aperte qualquer outra tecla\n").upper().strip()
    if "S" not in pergunta:
        print("Fim do jogo")
        print("Quantidade de vitórias: ",placarVitorias)
        print("Quantidade de derrotas:",placarDerrotas)
        input('Aperte "Enter" para sair!')
        break
    continue
