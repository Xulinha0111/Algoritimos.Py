"""
Autora: Julia Bellini Sorrente
Instituição: Etec Prof Idio Zucchi
Curso: 1° Ano P.I Informática para Internet 

Desafio: Um código que lesse um arquivo escrito em código Morse que
continha letras maiúsculas e números, e traduzisse as letras maiúsculas em
minúsculas e digitar os 10 primeiros números de Fibonacci.

Obs: Wagner, esse foi o meu máximo. Se eu olhasse fixamente 
para esse código por mais 15 min, com certeza estaria prestes a entrar para
a linhagem da Informática e começaria ali a minha jornada de calvície.
"""

if __name__ == "__main__":
    with open('morse.in') as entrada:
        with open('morse.out','w') as saida:
            morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]

            #-- Realiza a leitura de todas as linhas do arquivo de entrada
            linhas = entrada.readlines()

            #-- Laço que percorre a lista
            for linha in linhas:
                # retira o fim de linha e espaços
                temp = linha.rstrip('\n').split(" ")
                # cria uma variável vazia                    
                palavra = ""

                #-- Novo laço que percorre a linha tratada
                for t in temp:    
                    # inicia um contador
                    cont = 0        

                    #-- Laço percorre a variável morse e comparar com os elementos
                    for p in morse:
                        if (t == p):
                            #-- (se for encontrada a letra)
                            #-- (palavra recebe ela mesma + a letra convertida)
                            palavra += chr(97 + cont)  
                            break                  
                        cont += 1

                #-- Escreve a palavra no arquivo "morse.out"
                saida.write(palavra+'\n')
                #-- Testa a condição de parada - palavra FIM
                if (linha == '..-. .. --'):
                    break
            #-- Fecha arquivo de entrada
            entrada.close
            #-- Fecha arquivo de saída
            saida.close
