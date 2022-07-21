import pygame
from spritesheet import Spritesheet
<<<<<<< HEAD
import ptext
from dialogo import Dialogo
from dicionarios import dialogo
=======

class Jogador:
    def __init__(self,x,y):
        self.direita = False
        self.esquerda = False
        self.up = False
        self.down = False
        self.load_sprite()
        self.rect = self.animation_direita[0].get_rect(center=(int(x),int(y)))
        self.vel = 100
        self.velx = 0
        self.vely = 0
        self.xpos = self.rect.x
        self.ypos = self.rect.y
        self.state = "idle"
        self.tempo = 0
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155

class Jogador:
    def __init__(self,x,y):
        self.direita = False
        self.esquerda = False
        self.up = False
        self.down = False
        self.load_sprite()
        self.rect = self.animation_direita[0].get_rect(center=(int(x),int(y)))
        self.vel = 100
        self.velx = 0
        self.vely = 0
        self.state = "idle"
        self.tempo = 0
        self.check_dialogo = False
        self.dialogo_action = False
        self.dialogo = None

<<<<<<< HEAD
    def dialogar(self,obj_npc):
        if self.dialogo_action:
                self.dialogo.atualizacao()
            
        elif self.check_dialogo:
            ptext.draw("Clique em E para dialogar",(obj_npc.dino_rect.midtop[0]-75,obj_npc.dino_rect.midtop[1]-20),fontname="pixel.ttf",fontsize=12)

    def check_dialogo_event(self,npc):

        aperta = pygame.key.get_pressed()
        botao = aperta[pygame.K_e]

        if abs(self.rect.x - npc.dino_rect.x) < 100 and abs(self.rect.y - npc.dino_rect.y) < 100:
            self.check_dialogo = True
        else:
            self.check_dialogo = False
            self.dialogo_action = False
            self.dialogo = None

        if self.check_dialogo and botao and self.dialogo_action == False:
            self.dialogo_action = True
            self.dialogo = Dialogo(npc.falar,npc.num_falar,self)

        self.dialogar(npc)

    def j_desenhar(self,display):

        display.blit(self.imagem,self.rect)

    def animacao(self,delta):

        self.tempo += delta

        if self.state == "idle":
            self.imagem = self.lista_animacao[1]
            return

=======
    def j_desenhar(self,display):

        display.blit(self.imagem,self.rect)

    def animacao(self,delta):

        self.tempo += delta

        if self.state == "idle":
            self.imagem = self.lista_animacao[1]
            return

>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155
        if self.state == "movimento_esquerda":
            self.lista_animacao = self.animation_esquerda

        if self.state == "movimento_direita":
            self.lista_animacao = self.animation_direita

        if self.state == "movimento_up":
            self.lista_animacao = self.animation_up
        
        if self.state == "movimento_down":
            self.lista_animacao = self.animation_down

        if self.tempo > 0.150:
            self.tempo = 0
            self.frame = (self.frame + 1) % len(self.lista_animacao)
            self.imagem = self.lista_animacao[self.frame]

    def update(self,dt):

        self.velx = 0
        self.vely = 0

        #fix pro moonwalk
        if self.up and self.down:
            self.state = "idle"
        if self.esquerda and self.direita:
            self.state = "idle"

        if self.up and not self.down:
            self.vely = -self.vel
            self.state = "movimento_up"
            

        if self.down and not self.up:
            self.vely = self.vel
            self.state = "movimento_down"

        if self.esquerda and not self.direita:
            self.velx = -self.vel
            self.state = "movimento_esquerda"

        if self.direita and not self.esquerda:
            self.velx = self.vel
            self.state = "movimento_direita"

            
        if not self.down and not self.up and not self.direita and not self.esquerda:
            self.state = "idle"
            
<<<<<<< HEAD
        self.rect.x += round(self.velx*dt)
        self.rect.y += round(self.vely*dt)
=======
        self.xpos += self.velx * dt
        self.ypos += self.vely * dt
        self.rect.x = round(self.xpos)
        self.rect.y = round(self.ypos)
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155
        self.animacao(dt)

    def load_sprite(self):

        sprite = Spritesheet("pokemon.png")
        self.animation_direita = []
        self.animation_esquerda = []
        self.animation_up = []
        self.animation_down = []

        for r in range(1,4):

<<<<<<< HEAD
            self.animation_direita.append(sprite.sprite_load(f"sprite_red_left_{r}.png",(255, 200, 106),rev=True))
            self.animation_esquerda.append(sprite.sprite_load(f"sprite_red_left_{r}.png",(255, 200, 106)))
            self.animation_down.append(sprite.sprite_load(f"sprite_red_down_{r}.png",(255, 200, 106)))
            self.animation_up.append(sprite.sprite_load(f"sprite_red_up_{r}.png",(255, 200, 106)))
=======
            self.animation_direita.append(sprite.sprite_load(f"sprite_red_left_{r}.png",rev=True))
            self.animation_esquerda.append(sprite.sprite_load(f"sprite_red_left_{r}.png"))
            self.animation_down.append(sprite.sprite_load(f"sprite_red_down_{r}.png"))
            self.animation_up.append(sprite.sprite_load(f"sprite_red_up_{r}.png"))
>>>>>>> 22de142706235faeabf0690bf96dab6e00a3a155

        self.frame = 0
        self.imagem = 0
        self.lista_animacao = self.animation_direita