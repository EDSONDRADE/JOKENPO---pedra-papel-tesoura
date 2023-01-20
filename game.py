import random
from time import sleep
import pygame
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Botao():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
        
    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False


class Jokenpo():
    def __init__(self):
        pygame.init()

        self.tela = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("PEDRA PAPEL TESOURA => By JEGMASTER")
        icone = pygame.image.load('img/jegmaster.ico')
        pygame.display.set_icon(icone)

        self.interrogacao = pygame.image.load("img/interrogacao2.png").convert_alpha()
        self.backgraund = pygame.image.load("img/backgraund2.png")
        self.pedra_botao = pygame.image.load("img/botao_pedra2.png").convert_alpha()
        self.papel_botao = pygame.image.load("img/botao_papel2.png").convert_alpha()
        self.tesoura_botao = pygame.image.load("img/botao_tesoura2.png").convert_alpha()

        self.escolhe_pedra = pygame.image.load("img/pedra1.png").convert_alpha()
        self.escolhe_papel = pygame.image.load("img/papel2.jpg").convert_alpha()
        self.escolhe_tesoura = pygame.image.load("img/tesoura1.png").convert_alpha()

        self.tela.blit(self.backgraund, (0, 0))
        self.tela.blit(self.pedra_botao, (20, 500))
        self.tela.blit(self.papel_botao, (330, 500))
        self.tela.blit(self.tesoura_botao, (640, 500))

        self.btn_pedra = Botao(30, 520, (30, 520), 300, 140)
        self.btn_papel = Botao(340, 520, (340, 520), 300, 140)
        self.btn_tesoura = Botao(640, 520, (640, 520), 300, 140)

        self.font = pygame.font.Font(('img/Splatch.ttf'),  99)
        self.text = self.font.render(f" ", True, (255, 255, 255))

        self.toca = pygame.mixer.Sound("musica/janken.mp3")

        self.placar_player = 0
        self.placar_pc = 0

    def suspense_pc(self):
        self.tela.blit(self.interrogacao, (600, 200))

    def musica(self):
        self.toca.play()

    def placar_jogador(self):
        self.placar_player = 0
        self.placar_pc = 0

        pl = self.player_opcao
        pc = self.pc_random_choice

        if pl == "pedra" and pc == "papel" or pl == "papel" and pc == "tesoura" or pl == "tesoura" and pc == "pedra":
            self.placar_pc += 1
        elif pl == pc:
            pass
        else:
            self.placar_player += 1

        return self.placar_player

    def placar_computador(self):
        self.placar_player = 0
        self.placar_pc = 0

        pl = self.player_opcao
        pc = self.pc_random_choice

        if pl == "pedra" and pc == "papel" or pl == "papel" and pc == "tesoura" or pl == "tesoura" and pc == "pedra":
            self.placar_pc += 1
        elif pl == pc:
            pass
        else:
            self.placar_player += 1
        return self.placar_pc

    def player(self):
        if self.btn_pedra.clicked(30):
            self.player_opcao = "pedra"
            self.tela.blit(self.escolhe_pedra, (120, 200))
        elif self.btn_papel.clicked(340):
            self.player_opcao = "papel"
            self.tela.blit(self.escolhe_papel, (120, 200))
        else:
            self.btn_tesoura.clicked(640)
            self.player_opcao = "tesoura"
            self.tela.blit(self.escolhe_tesoura, (120, 200))

        return self.player_opcao

    def computador(self):
        self.pc_random_choice = " "
        opcao = ["pedra", "papel", "tesoura"]
        escolha_pc = random.choice(opcao)
        if escolha_pc == "pedra":
            self.pc_random_choice = "pedra"
            escolha_pc = self.escolhe_pedra
        elif escolha_pc == "papel":
            self.pc_random_choice = "papel"
            escolha_pc = self.escolhe_papel
        else:
            self.pc_random_choice = "tesoura"
            escolha_pc = self.escolhe_tesoura
        opcao_pc = self.tela.blit(escolha_pc, (600, 200))
        return opcao_pc

    def img_reset(self):
        self.tela.blit(self.text, (330, 0))
        self.text = self.font.render(" ", True, (0, 0, 0))
        self.tela.blit(self.backgraund, (0, 0))
        self.tela.blit(self.pedra_botao, (20, 500))
        self.tela.blit(self.papel_botao, (330, 500))
        self.tela.blit(self.tesoura_botao, (640, 500))
        pass

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        jeg_game = Jokenpo()

        while run:
            pygame.display.update()
            self.tela.blit(self.text, (330, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jeg_game.player()
                    pygame.display.update()
                    jeg_game.suspense_pc()
                    pygame.display.update()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn_pedra.clicked(30) or self.btn_papel.clicked(340) or self.btn_tesoura.clicked(640):
                        jeg_game.musica()
                        sleep(10)
                        jeg_game.img_reset()
                        jeg_game.player()
                        jeg_game.computador()

                        self.placar_player += jeg_game.placar_jogador()
                        self.placar_pc += jeg_game.placar_computador()
                        self.text = self.font.render(f"{self.placar_player} : {self.placar_pc}", True, (0, 0, 0))

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()


if __name__ == '__main__':
    game = Jokenpo()
    game.game_loop()
