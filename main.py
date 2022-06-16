print("Importando módulos")
import pygame as pg
import sys
import images
import fontes
import lc
from player import Player, drop_item_group
import item
import calendario
from camera import Camera
from cursor import Cursor
from hud import Hud
from sprite_draw import sprite_draw, get_draw_count
from collision import collision_check
from time import time
print("Módulos importados")

pg.init()

fullscreen = False
screen = images.screen
pg.display.set_caption("Oho")
clock = pg.time.Clock()
pg.mouse.set_visible(False)

player = Player()
player_group = pg.sprite.Group()
player_group.add(player)
player.inv_list = [item.Manguza(), item.Pacoca(), item.Key(4), item.Money(50)]

wall_group = pg.sprite.Group()
lc.level_construct(wall_group, lc.level0)

door_group = pg.sprite.Group()
door_group.add(lc.Door(288, -255, 10, 64, True, 4))

day_time = calendario.Calendario()

cursor = Cursor()
camera = Camera(player.rect, screen)
hud = Hud(screen)


group_draw_list = [wall_group, door_group, item.ball_group, drop_item_group, player_group]
collision_group_list = [wall_group, door_group]
interactable_group_list = [door_group]

#sons.musica.play(sons.radio_video, 0, 5000)
#sons.musica_fila(sons.musica, sons.atwa)
debug_delay = 1
debug_last = 0

while True:

	keys_pressed = pg.key.get_pressed()
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		if keys_pressed[pg.K_ESCAPE]:
			print("bye")
			pg.quit()
			sys.exit()
		if keys_pressed[pg.K_F11]:
			if fullscreen:
				pg.display.set_mode(screen.get_size())
				fullscreen = False	
			elif fullscreen == False :
				pg.display.set_mode(screen.get_size(), pg.FULLSCREEN)
				fullscreen = True
		if keys_pressed[pg.K_h]:
			obj = item.Item()
			obj.rect.center = player.rect.center
			drop_item_group.add(obj)

		
	player.control(keys_pressed)
	player_group.update()
	player.get_interactable_list(drop_item_group, interactable_group_list)
	item.ball_group.update()

	day_time.update()
	cursor.update()
	camera.update(player.rect, screen)

	collision_check(player, collision_group_list, item.ball_group)

	sprite_draw(screen, camera, group_draw_list, player.interactable_list)
	hud.draw_inv(screen, player.inv_list, player.inv_select)
	hud.draw_ui(screen, player, day_time, cursor)

	screen.blit(fontes.smallarial.render(str("Drawing:"+str(get_draw_count())), True, (255,255,0)), (screen.get_width()/2, screen.get_height()-60))
	screen.blit(fontes.smallarial.render(str("Interactables:"+str(len(drop_item_group)+len(door_group))), True, (255,255,0)), (screen.get_width()/2, screen.get_height()-40))
	screen.blit(fontes.smallarial.render(str("frametime:" + str(clock.get_rawtime())), True, (255,255,0)), (screen.get_width()/2, screen.get_height()-20))

	pg.display.update()
	clock.tick(60)