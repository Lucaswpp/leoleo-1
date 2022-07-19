import pygame
import ptext

def desenhar_box_dialog(texto,tamanho,cor):

    display = pygame.display.get_surface()

    bg_surf = pygame.Surface((400,200))
    bg_rect = bg_surf.get_rect(center=(300,300))

    frame_rect = bg_rect.copy()
    frame_rect.inflate_ip(15,15)

    pygame.draw.rect(display,(255,255,255),frame_rect)
    pygame.draw.rect(display,(0,0,0),bg_rect)

    ptext.draw(texto,(bg_rect.topleft[0]+20,bg_rect.topleft[1]+20),fontsize=tamanho,color=cor,fontname="pixel.ttf")

class Dialogo:
    def __init__(self,dialogos,fala_final,player):

        self.tamanho = 20
        self.cor = (255,255,255)
        self.pos_x = 5
        self.pos_y = 10
        self.player = player


        self.fala_final = fala_final
        self.etapa = 0 
        self.falas = dialogos

        self.vel_fala = 0.3
        self.inicio_fala = 0
        self.numero_fala = self.falas[self.etapa]
        self.dialog_ativo = self.player.dialogo_action

    def atualizacao(self):

        aperta = pygame.key.get_pressed()
        espaco = aperta[pygame.K_SPACE]

        if self.dialog_ativo:

            if self.etapa < self.fala_final:
                if int(self.inicio_fala) < len(self.numero_fala):
                    self.inicio_fala += self.vel_fala
                else:
                    if espaco:
                        self.etapa += 1
                        self.inicio_fala = 0
                        self.numero_fala = self.falas[self.etapa]

            elif self.etapa == self.fala_final:
                if int(self.inicio_fala) < len(self.numero_fala):
                    self.inicio_fala += self.vel_fala
                
                else:
                    if espaco:
                        self.inicio_fala = 0
                        self.etapa = 0
                        self.numero_fala = 0
                        self.dialog_ativo = self.player.dialogo_action = False

            self.desenhar_texto()

    def desenhar_texto(self):

        if self.dialog_ativo:

            texto = self.numero_fala
            desenhar_box_dialog(texto[0:int(self.inicio_fala)],15,(255,255,255))