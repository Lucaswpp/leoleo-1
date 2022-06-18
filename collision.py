import pygame as pg
import groups
import sons
from math import ceil

def collision_check(player:pg.sprite.Sprite, collision_group_list):
	#colisão jogador/parede
	for group in collision_group_list:
		obj = pg.sprite.spritecollideany(player, group)
		if obj != None:
			if abs(obj.rect.bottom - player.rect.top) < player.yspeed*2:
				player.rect.y += ceil(abs(player.yvel))
			if abs(obj.rect.left - player.rect.right) < player.xspeed*2:
				player.rect.x -= ceil(abs(player.xvel))
			if abs(obj.rect.right - player.rect.left) < player.xspeed*2:
				player.rect.x += ceil(abs(player.xvel))
			if abs(obj.rect.top - player.rect.bottom) < player.yspeed*2:
				player.rect.y -= ceil(abs(player.yvel))
				
	#colisão bola/parede -> https://www.youtube.com/watch?v=1_H7InPMjaY
	for group in collision_group_list:
		col_dict = pg.sprite.groupcollide(groups.ball_group, group, False, False)
		for ball in col_dict:
			ball.kill()
			sons.play_far_effect(player.rect, ball.rect, sons.ball_hit)