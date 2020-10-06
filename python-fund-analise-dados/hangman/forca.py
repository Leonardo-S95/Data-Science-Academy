import random
from pygame import mixer
from time import sleep

board = ['''

 +----------+
 |          |
            |
            |
            |
            |
    ================''', '''
    
 +----------+
 |          |
 O          |
            |
            |
            |
    ================''', '''

 +----------+
 |          |
 O          |
 |          |
            |
            |
    ================''', '''
    
 +----------+
 |          |
 O          |
/|          |
            |
            |
    ================''', '''
    
 +----------+
 |          |
 O          |
/|\         |
            |
            |
    ================''', '''
    
 +----------+
 |          |
 O          |
/|\         |
/           |
            |
    ================''', '''
    
 +----------+
 |          |
 O          |
/|\         |
/ \         |
            |
    ================'''
         ]


class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.lstcorrect = []
        self.lstwrong = []
        self.hiddenword = ['_' for i in range(0, len(word))]
        self.countcorrect = 0
        self.countwrong = 0
        print('\n=-=-=-=-=-=-=- Hangman -=-=-=-=-=-=-=')

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            if letter not in self.lstcorrect:
                self.lstcorrect.append(letter)
                for i in range(0, len(self.word)):
                    if letter == self.word[i]:
                        self.hiddenword[i] = letter
                        self.countcorrect += 1
        else:
            if letter not in self.lstwrong:
                self.lstwrong.append(letter)
                self.countwrong += 1

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.countwrong == 6:
            return True
            
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.countcorrect == len(self.word):
            self.print_game_status()
            return True

    # Método para mostrar letras certas e erradas
    def guessed_letters(self):
        print('\n\nLetras corretas: ')

        for i in self.lstcorrect:
            print(i, end=' ')

        print('\nLetras erradas: ')

        for i in self.lstwrong:
            print(i, end=' ')

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.countwrong], '\n')
        for i in range(0, len(self.hiddenword)):
            print(self.hiddenword[i], end=' ')


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras2.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip().upper()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while True:
        game.print_game_status()
        game.guessed_letters()
        game.guess(str(input('\nDigite uma letra: '))[0].strip().upper())

    # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_won():
            print('\n\nYOU WIN!! (leia com a voz do Street Fighter)')
            mixer.init()
            mixer.music.load('gnome.mp3')
            mixer.music.play()
            sleep(2)
            break
        elif game.hangman_over():
            print('\nGame over!')
            print('A palavra era ' + game.word)
            break

    print('\nSee ya!      :D')


# Executa o programa
if __name__ == "__main__":
    main()
