if __name__ == "__main__":
    with open('morse.in') as entrada:
        with open('morse.out','w') as saida:
            morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]

            # realiza a leitura de todas as linhas do arquivo de entrada
            linhas = entrada.readlines()

            # laço que percorre a lista
            for linha in linhas:
                # retira o fim de linha e espaços
                temp = linha.rstrip('\n').split(" ")
                # cria uma variável vazia                    
                palavra = ""

                # novo laço que percorre a linha tratada
                for t in temp:    
                    # inicia um contador
                    cont = 0        

                    # laço percorre a variável morse e comparar com os elementos
                    for p in morse:
                        if (t == p):
                            # se for encontrada a letra
                            # palavra recebe ela mesma mais a letra convertida
                            palavra += chr(97 + cont)  
                            break                  
                        cont += 1
                # escreve a palavra no arquivo "morse.out"
                saida.write(palavra+'\n')
                # testa a condição de parada - palavra FIM
                if (linha == '..-. .. --'):
                    break
            # fecha arquivo de entrada
            entrada.close
            # fecha arquivo de saída
            saida.close
