import pygame
import time
<<<<<<< HEAD
from dialogo import Dialogo
from player import Jogador
from npc import Npc
from dicionarios import dialogo
=======
from player import Jogador
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155

pygame.init()

class Jogo:
    def __init__(self):
<<<<<<< HEAD
        self.largura,self.altura = 700,700
=======
        self.largura,self.altura = 500,400
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155
        self.tela = pygame.display.set_mode((self.largura,self.altura))
        self.jogo_ativo = True
        self.clock = pygame.time.Clock()
        self.tempo_inicial = time.time()
        self.deltatime = 0
        self.jogador = Jogador(250,200)
<<<<<<< HEAD
        self.npc = Npc(100,100,self.jogador)
  
=======

>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155

    def iniciar(self):
        while self.jogo_ativo:
            self.get_delta()
            self.evento()
            self.desenhar()

    def evento(self):

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                self.jogo_ativo = False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_LEFT:
                    self.jogador.esquerda = True
                if evento.key == pygame.K_RIGHT:
                    self.jogador.direita = True
                if evento.key == pygame.K_UP:
                    self.jogador.up = True
                if evento.key == pygame.K_DOWN:
                    self.jogador.down = True

<<<<<<< HEAD

=======
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155
            if evento.type == pygame.KEYUP:

                if evento.key == pygame.K_LEFT:
                    self.jogador.esquerda = False
                if evento.key == pygame.K_RIGHT:
                    self.jogador.direita = False
                if evento.key == pygame.K_UP:
                    self.jogador.up = False
                if evento.key == pygame.K_DOWN:
<<<<<<< HEAD
                    self.jogador.down = False        
=======
                    self.jogador.down = False

>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155



    def desenhar(self):

        self.clock.tick(30)
<<<<<<< HEAD
        self.tela.fill((128,128,128))
        self.npc.update(self.deltatime,self.tela)
        self.npc.desenhar_dino(self.tela)
        self.jogador.update(self.deltatime)
        self.jogador.j_desenhar(self.tela)
        self.jogador.check_dialogo_event(self.npc)
        pygame.display.update()
=======
        self.tela.fill("#000000")
        self.jogador.update(self.deltatime)
        self.jogador.j_desenhar(self.tela)
        pygame.display.update()
       
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155

    def get_delta(self):
        tempo_final = time.time()
        self.deltatime = tempo_final - self.tempo_inicial
        self.tempo_inicial = tempo_final



if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()