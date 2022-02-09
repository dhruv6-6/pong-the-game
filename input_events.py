from operator import truediv
from pickle import TRUE
import pygame
import sys
import math

from pygame import key

class Input_Events:
    
    def __init__(self,ai_game):
        self.info = ai_game.info
        self.state = ai_game.state
        self.screens = ai_game.screens
        self.disp = ai_game.disp
        self.ball = ai_game.ball

    def _check_event(self, event):
        self._mousedown_event(event)
        self._mouseup_event(event)
        self._keydown_event(event)
        self._keyup_event(event)

    def _keydown_event(self, event):
        if event.type == pygame.KEYDOWN:

            if self.state.home_screen == True:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            
            if self.state.settings_screen == True:

                if event.key == pygame.K_ESCAPE:
                    self.state.settings_screen = False
                    self.state.home_screen = True
                    self.info.change.play()
                    
            if self.state.mp_game_active == True:

                if event.key == pygame.K_ESCAPE:

                    self.info.ball_speed_x = self.info.ball_speed_x_initial

                    self.state.home_screen = True
                    self.state.mp_game_active = False
                    
                    self.info.player_1_point = 0
                    self.info.player_2_point = 0

                    pygame.mouse.set_visible(True)
                    self.info.change.play()

                if event.key == pygame.K_w:
                    self.state.leftpad_up = True

                if event.key == pygame.K_s:
                    self.state.leftpad_down = True
                
                if event.key == pygame.K_UP:
                    self.state.rightpad_up = True

                if event.key == pygame.K_DOWN:
                    self.state.rightpad_down = True

            if self.state.mp_game_start == True:
                
                if event.key == pygame.K_ESCAPE:
                    self.info.ball_speed_x = self.info.ball_speed_x_initial
                    self.state.home_screen = True
                    self.state.mp_game_start = False
                    self.info.player_1_point = 0
                    self.info.player_2_point = 0
                    pygame.mouse.set_visible(True)
                    self.info.change.play()

                if event.key == pygame.K_SPACE:
                    self.state.mp_game_start = False
                    self.state.mp_game_active = True

                    self.info._update_yspeed()

                    self.info.ball_x_pos = self.info.initial_ball_x_pos
                    self.info.ball_y_pos = self.info.initial_ball_y_pos

                    self.info.leftpad_x_pos = self.info.initial_leftpad_x_pos
                    self.info.leftpad_y_pos = self.info.initial_leftpad_y_pos

                    self.info.rightpad_x_pos = self.info.initial_rightpad_x_pos
                    self.info.rightpad_y_pos = self.info.initial_rightpad_y_pos

                    self.state.leftpad_up = False
                    self.state.leftpad_down = False
                    self.state.rightpad_up = False
                    self.state.rightpad_down = False

            if self.state.sp_select_screen == True:

                if event.key == pygame.K_ESCAPE:
                    self.state.home_screen = True
                    self.state.sp_select_screen = False
    
                    self.info.change.play()

                if event.key == pygame.K_SPACE:
                    self.state.sp_game_active = True
                    self.state.sp_select_screen = False
                    self.info.change.play()
                    pygame.mouse.set_visible(False)

                    self.info.sp_pad_x_pos = self.info.sp_initial_pad_x_pos
                    self.info.sp_pad_y_pos = self.info.sp_initial_pad_y_pos
                    self.info.sp_ball_x_pos = self.info.sp_initial_ball_x_pos
                    self.info.sp_ball_y_pos = self.info.sp_initial_ball_y_pos

                    self.state.sp_pad_up = False
                    self.state.sp_pad_down = False 
            
            if self.state.sp_game_active == True:

                if event.key == pygame.K_ESCAPE:
                    self.state.sp_select_screen = True
                    self.state.sp_game_active = False
                    self.info.sp_ball1_speed_x = self.info.sp_ball1_speed_x_initial
                    self.info.sp_ball1_x_pos = self.info.sp_initial_ball1_x_pos
                    self.info.sp_ball1_y_pos = self.info.sp_initial_ball1_y_pos
                    self.info.sp_ball2_speed_x = self.info.sp_ball2_speed_x_initial
                    self.info.sp_ball2_x_pos = self.info.sp_initial_ball2_x_pos
                    self.info.sp_ball2_y_pos = self.info.sp_initial_ball2_y_pos
                    self.info.bricks1_x = self.info.bricks1_x_initial.copy()
                    self.info.bricks1_y = self.info.bricks1_y_initial.copy()
                    self.info.bricks2_x = self.info.bricks2_x_initial.copy()
                    self.info.bricks2_y = self.info.bricks2_y_initial.copy()
                    self.state.sp_ball2_moving_right = False  
                    self.state.sp_ball1_moving_right = True

                    self.info.ball1_delay = 0
                    self.info.ball2_delay = 0

                    self.info.change.play()
                    pygame.mouse.set_visible(True)
                
                if event.key == pygame.K_w:
                    self.state.sp_pad_up = True

                if event.key == pygame.K_s:
                    self.state.sp_pad_down = True
                

    def _keyup_event(self, event):

        if event.type == pygame.KEYUP:

            if self.state.mp_game_active == True:

                if event.key == pygame.K_w:
                    self.state.leftpad_up = False

                if event.key == pygame.K_s:
                    self.state.leftpad_down = False
                
                if event.key == pygame.K_UP:
                    self.state.rightpad_up = False

                if event.key == pygame.K_DOWN:
                    self.state.rightpad_down = False

            if self.state.sp_game_active == True:

                if event.key == pygame.K_w:
                    self.state.sp_pad_up = False

                if event.key == pygame.K_s:
                    self.state.sp_pad_down = False
                

         
    def _mousedown_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mos_pos = pygame.mouse.get_pos()

            if self.state.home_screen == True:

                if self.info.mp_x < mos_pos[0] < self.info.mp_x + self.info.multiplayer_image_rect[2] and self.info.mp_y < mos_pos[1] < self.info.mp_y + self.info.multiplayer_image_rect[3]:
                    self.state.mp_game_start = True
                    self.state.home_screen = False
                    self.info.change.play()
                    pygame.mouse.set_visible(False)

                if self.info.sp_x < mos_pos[0] < self.info.sp_x + self.info.singleplayer_image_rect[2] and self.info.sp_y < mos_pos[1] < self.info.sp_y + self.info.singleplayer_image_rect[3]:
                    self.state.sp_select_screen = True
                    self.state.home_screen = False
                    self.info.change.play()

                if self.info.set_x < mos_pos[0] < self.info.set_x + self.info.settings_image_rect[2] and self.info.set_y < mos_pos[1] < self.info.set_y + self.info.settings_image_rect[3]:
                    self.state.settings_screen = True
                    self.state.home_screen = False
                    self.info.change.play()
            
            if self.state.settings_screen == True:

                if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width and self.info.screen_height/6 - self.info.bar_image_rect[3]/2 < mos_pos[1] < self.info.screen_height/6 - self.info.bar_image_rect[3]/2 + self.info.bar_height:
                    self.state.speed_change = True
                    self.info.select.play()

                if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width and 2*self.info.screen_height/6 - self.info.bar_image_rect[3]/2 < mos_pos[1] < 2*self.info.screen_height/6 - self.info.bar_image_rect[3]/2 + self.info.bar_height:
                    self.state.size_change = True
                    self.info.select.play()

                if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width and 3*self.info.screen_height/6 - self.info.bar_image_rect[3]/2 < mos_pos[1] < 3*self.info.screen_height/6 - self.info.bar_image_rect[3]/2 + self.info.bar_height:
                    self.state.win_change = True
                    self.info.select.play()

                if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width and 5*self.info.screen_height/6 - self.info.bar_image_rect[3]/2 < mos_pos[1] < 5*self.info.screen_height/6 - self.info.bar_image_rect[3]/2 + self.info.bar_height:
                    self.state.volume_change = True
                    self.info.select.play()
                    
                if self.info.on_image_x + 100 < mos_pos[0] < self.info.on_image_x + 100 + self.info.boxes_size and self.info.on_image_y < mos_pos[1] < self.info.on_image_y + self.info.boxes_size:
                    self.state.bg_music = True
                    self.info.select.play()
                    pygame.mixer.music.unpause()

                if self.info.off_image_x + 100 < mos_pos[0] < self.info.off_image_x + 100 + self.info.boxes_size and self.info.off_image_y < mos_pos[1] < self.info.off_image_y + self.info.boxes_size:
                    self.state.bg_music = False
                    self.info.select.play()
                    pygame.mixer.music.pause()

            if self.state.sp_select_screen == True:
                
                if 1*self.info.screen_width/4 - self.info.level_select_circle/2 < mos_pos[0] < 1*self.info.screen_width/4 + self.info.level_select_circle/2 and 1*self.info.screen_height/4 - self.info.level_select_circle/2 < mos_pos[1] < 1*self.info.screen_height/4 + self.info.level_select_circle/2 :
                    self.state.sp_1_game_start ,self.state.sp_2_game_start ,self.state.sp_3_game_start ,self.state.sp_4_game_start ,self.state.sp_5_game_start ,self.state.sp_6_game_start = True,False,False,False,False,False

                if 2*self.info.screen_width/4 - self.info.level_select_circle/2 < mos_pos[0] < 2*self.info.screen_width/4 + self.info.level_select_circle/2 and 1*self.info.screen_height/4 - self.info.level_select_circle/2 < mos_pos[1] < 1*self.info.screen_height/4 + self.info.level_select_circle/2 :
                    self.state.sp_1_game_start ,self.state.sp_2_game_start ,self.state.sp_3_game_start ,self.state.sp_4_game_start ,self.state.sp_5_game_start ,self.state.sp_6_game_start = False,True,False,False,False,False

                if 3*self.info.screen_width/4 - self.info.level_select_circle/2 < mos_pos[0] < 3*self.info.screen_width/4 + self.info.level_select_circle/2 and 1*self.info.screen_height/4 - self.info.level_select_circle/2 < mos_pos[1] < 1*self.info.screen_height/4 + self.info.level_select_circle/2 :
                    self.state.sp_1_game_start ,self.state.sp_2_game_start ,self.state.sp_3_game_start ,self.state.sp_4_game_start ,self.state.sp_5_game_start ,self.state.sp_6_game_start = False,False,True,False,False,False
                
                if 1*self.info.screen_width/4 - self.info.level_select_circle/2 < mos_pos[0] < 1*self.info.screen_width/4 + self.info.level_select_circle/2 and 2*self.info.screen_height/4 - self.info.level_select_circle/2 < mos_pos[1] < 2*self.info.screen_height/4 + self.info.level_select_circle/2 :
                    self.state.sp_1_game_start ,self.state.sp_2_game_start ,self.state.sp_3_game_start ,self.state.sp_4_game_start ,self.state.sp_5_game_start ,self.state.sp_6_game_start = False,False,False,True,False,False

                if 2*self.info.screen_width/4 - self.info.level_select_circle/2 < mos_pos[0] < 2*self.info.screen_width/4 + self.info.level_select_circle/2 and 2*self.info.screen_height/4 - self.info.level_select_circle/2 < mos_pos[1] < 2*self.info.screen_height/4 + self.info.level_select_circle/2 :
                    self.state.sp_1_game_start ,self.state.sp_2_game_start ,self.state.sp_3_game_start ,self.state.sp_4_game_start ,self.state.sp_5_game_start ,self.state.sp_6_game_start = False,False,False,False,True,False
                    
                if 3*self.info.screen_width/4 - self.info.level_select_circle/2 < mos_pos[0] < 3*self.info.screen_width/4 + self.info.level_select_circle/2 and 2*self.info.screen_height/4 - self.info.level_select_circle/2 < mos_pos[1] < 2*self.info.screen_height/4 + self.info.level_select_circle/2 :
                    self.state.sp_1_game_start ,self.state.sp_2_game_start ,self.state.sp_3_game_start ,self.state.sp_4_game_start ,self.state.sp_5_game_start ,self.state.sp_6_game_start = False,False,False,False,False,True

                self.info._sp_update_pad()

    def _mouseup_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mos_pos = pygame.mouse.get_pos()

            if self.state.settings_screen == True:

                if self.state.speed_change == True:
                    
                    if mos_pos[0] < self.info.slider_x:
                        self.info.ball_speed_x = 100
                        self.info.slider_width_speed = 10
                        self.info.initial_leftpad_x_pos = 100
                        
                    if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width:
                        self.info.ball_speed_x = math.floor(100 + (mos_pos[0] - self.info.slider_x)/2.5)
                        self.info.initial_leftpad_x_pos = math.floor(100 + (mos_pos[0] - self.info.slider_x)/2.5)

                    if  mos_pos[0] > self.info.slider_x + self.info.bar_width :
                        self.info.ball_speed_x = 500
                        self.info.slider_width_speed = 1000
                        self.info.initial_leftpad_x_pos = 500

                    self.state.speed_change = False

                if self.state.size_change == True:
                    
                    if mos_pos[0] < self.info.slider_x:
                        self.info.pad_height = 150
                        self.info.slider_width_size = 10
                        
                    if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width:
                        self.info.pad_height = math.floor(150 + (mos_pos[0] - self.info.slider_x)/5)

                    if  mos_pos[0] > self.info.slider_x + self.info.bar_width :
                        self.info.pad_height = 350
                        self.info.slider_width_size = 1000

                    self.state.size_change = False
                
                if self.state.win_change == True:
                    
                    if mos_pos[0] < self.info.slider_x:
                        self.info.winning_points = 1
                        self.info.slider_width_win = 10
                        
                    if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width:
                        self.info.winning_points = math.ceil((mos_pos[0] - self.info.slider_x)/100)

                    if  mos_pos[0] > self.info.slider_x + self.info.bar_width :
                        self.info.winning_points = 10
                        self.info.slider_width_win = 1000

                    self.state.win_change = False
                
                if self.state.volume_change == True:
                    
                    if mos_pos[0] < self.info.slider_x:
                        pygame.mixer.music.set_volume(0)
                        self.info.slider_width_volume = 10
                        
                    if self.info.slider_x < mos_pos[0] < self.info.slider_x + self.info.bar_width:
                        pygame.mixer.music.set_volume( math.ceil((mos_pos[0] - self.info.slider_x)/100)/10 )

                    if  mos_pos[0] > self.info.slider_x + self.info.bar_width :
                        pygame.mixer.music.set_volume(1)
                        self.info.slider_width_volume = 1000

                    self.state.volume_change = False



                