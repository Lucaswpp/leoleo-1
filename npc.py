import pygame
from spritesheet import Spritesheet
from dicionarios import dialogo

class Npc:
    def __init__(self,x,y,jogador):
        self.sprite_load_npc()
        self.dino_rect = self.animation_dino_idle[0].get_rect(center=(int(x),int(y)))
        self.imagem = 0
        self.frame = 0
        self.tempo = 0
        self.imagem = self.animation_dino_idle[0]
        self.dialogo = False
        self.check_dialogo = False
        self.jogador = jogador
        self.falar = dialogo
        self.num_falar = 5

        
    def desenhar_dino(self,display):
        display.blit(self.imagem,self.dino_rect)

    def update(self,dt,display):
  
        self.animacao_dino(dt)


    def animacao_dino(self,deltatime):
        self.tempo += deltatime
        
        if self.tempo > 0.150:
            self.tempo = 0
            self.frame = (self.frame + 1) % len(self.animation_dino_idle)
            self.imagem = self.animation_dino_idle[self.frame]

    def sprite_load_npc(self):

        sprite = Spritesheet("doux.png")

        self.animation_dino_idle = []

        for r in range(1,5):
            self.animation_dino_idle.append(sprite.sprite_load(f"sprite_dino_idle_{r}.png",(0,0,0)))