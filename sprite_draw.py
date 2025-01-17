import pygame as pg
import fontes
from utils import outline_image
from item import Item

last_draw_quantity = 0

def sprite_draw(screen:pg.display.set_mode, camera, player, group_draw_list = [], interactable_list = []):
    global last_draw_quantity
    screen.fill((50,50,50))
    i = 0
    for group in group_draw_list:
        for sprite in group:
            offpos = (sprite.rect.centerx + camera.xoffset - sprite.image.get_width()/2, sprite.rect.centery + camera.yoffset - sprite.image.get_height()/2)
            if offpos[0]+sprite.rect.width > 0 and offpos[0] < screen.get_width() and offpos[1]+sprite.rect.height > 0 and offpos[1] < screen.get_height():
                i+=1
                screen.blit(sprite.image, offpos)
    last_draw_quantity = i
    player_draw_pos =  (player.rect.centerx + camera.xoffset - player.image.get_width()/2, player.rect.centery + camera.yoffset - player.image.get_height()/2)
    screen.blit(player.image, player_draw_pos)
    screen.blit(player.outline, player_draw_pos)

    for obj in interactable_list:
        screen.blit(outline_image(obj.image, (255,255,0)), (obj.rect.x + camera.xoffset, obj.rect.y + camera.yoffset))
        if isinstance(obj, Item):
                    screen.blit(fontes.smallarial.render(str(obj.name), True, (255,255,255)), (obj.rect.x + camera.xoffset, obj.rect.top-18+camera.yoffset))

def get_draw_count():
    return last_draw_quantity
