import pygame
import random
import math

class Information:

    def __init__(self,ai_game):
        self.state = ai_game.state

        #basic
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (235,235,235)
        self.text_color = (50,50,50)
        
        #ball
        self.ball_size = 30
        self.ball_speed_x_initial = 250
        self.ball_speed_x = 250
        self.ball_speed_y = 2.5
        self.ball_speed_inc = 25
        self.max_ball_speed = 800
        self.temp_ball_image = pygame.image.load('pong-the-game/images/ball.png')
        self.ball_image = pygame.transform.smoothscale( self.temp_ball_image , [ self.ball_size , self.ball_size])
        
        self.initial_ball_x_pos = (self.screen_width/2) - (self.ball_size/2)
        self.initial_ball_y_pos = (self.screen_height/2) - (self.ball_size/2)
        self.ball_x_pos = self.initial_ball_x_pos
        self.ball_y_pos = self.initial_ball_y_pos
        
        #middle bar
        self.mid_divider_width = 8
        self.temp_bar_image = pygame.image.load('pong-the-game/images/middle_line.png')
        self.middle_bar = pygame.transform.smoothscale( self.temp_bar_image , [self.mid_divider_width , 1080])
        self.temp2_bar_image = pygame.image.load('pong-the-game/images/mid_bar.png')
        self.mid_filled_bar = pygame.transform.smoothscale( self.temp2_bar_image , [self.mid_divider_width , 1080])

        #pad
        self.pad_height = 250
        self.pad_width = 20
        self.pad_speed = 3.5 

        self.initial_leftpad_x_pos = 15
        self.initial_leftpad_y_pos = self.screen_height/2 - self.pad_height/2
        self.leftpad_x_pos = self.initial_leftpad_x_pos
        self.leftpad_y_pos = self.initial_leftpad_y_pos
        
        self.initial_rightpad_x_pos = self.screen_width - self.pad_width - 15
        self.initial_rightpad_y_pos = self.screen_height/2 - self.pad_height/2
        self.rightpad_x_pos = self.initial_rightpad_x_pos
        self.rightpad_y_pos = self.initial_rightpad_y_pos

        self.temp_pad_image = pygame.image.load('pong-the-game/images/pad.png')
        self.pad_image = pygame.transform.smoothscale( self.temp_pad_image , [ self.pad_width , self.pad_height ])
        
        #font style
        self.font_60 = pygame.font.Font("pong-the-game/font/font.otf", 60)
        self.font_140 = pygame.font.Font("pong-the-game/font/font.otf", 140)
        self.font_50 =  pygame.font.Font("pong-the-game/font/font.otf", 50)
        self.font_100 =  pygame.font.Font("pong-the-game/font/font.otf", 100)
        self.font_40 =  pygame.font.Font("pong-the-game/font/font.otf", 40)

        #home screen
        self.multiplayer_image = self.font_50.render("Multiplayer" , True , self.text_color , self.bg_color)
        self.multiplayer_image_rect = self.multiplayer_image.get_rect()
        self.mp_x = self.screen_width/3 - self.multiplayer_image_rect[2]/2
        self.mp_y = 3*self.screen_height/5 - self.multiplayer_image_rect[3]/2 

        self.singleplayer_image = self.font_50.render("Singleplayer" , True , self.text_color , self.bg_color)
        self.singleplayer_image_rect = self.singleplayer_image.get_rect()
        self.sp_x = 2*self.screen_width/3 - self.singleplayer_image_rect[2]/2
        self.sp_y = 3*self.screen_height/5 - self.singleplayer_image_rect[3]/2

        self.settings_image = self.font_50.render("Settings" , True , self.text_color , self.bg_color)
        self.settings_image_rect = self.settings_image.get_rect()
        self.set_x = self.screen_width/2 - self.settings_image_rect[2]/2 
        self.set_y = 4*self.screen_height/5 - self.settings_image_rect[3]/2

        self.pong_image = self.font_140.render("Pong" , True , self.text_color , self.bg_color)
        self.pong_image_rect = self.pong_image.get_rect()
        self.pong_x = self.screen_width/2 - self.pong_image_rect[2]/2 
        self.pong_y = 3*self.screen_height/8 - self.pong_image_rect[3]/2

        #winning screen
        self.p1_win_image = self.font_100.render("Player 1 Won!!" , True , self.text_color , self.bg_color)
        self.p1_win_image_rect = self.p1_win_image.get_rect()
        self.p1_win_x = self.screen_width/2 - self.p1_win_image_rect[2]/2 
        self.p1_win_y = self.screen_height/2 - self.p1_win_image_rect[3]/2

        self.p2_win_image = self.font_100.render("Player 2 Won!!" , True , self.text_color , self.bg_color)
        self.p2_win_image_rect = self.p2_win_image.get_rect()
        self.p2_win_x = self.screen_width/2 - self.p2_win_image_rect[2]/2 
        self.p2_win_y = self.screen_height/2 - self.p2_win_image_rect[3]/2

        #setting mp game
        self.winning_points = 2
        self.player_1_point = 0
        self.player_2_point = 0

        self.how_start = self.font_50.render("Press Space To Start" , True , self.text_color , self.bg_color) 
        self.how_start_rect = self.how_start.get_rect()
        self.how_start_x = self.screen_width/2 - self.how_start_rect[2]/2
        self.how_start_y = self.screen_height/2 - self.how_start_rect[3]/2

        #ai pad
        self.ai_pad_height = 250
        self.ai_pad_width = 20
        self.ai_pad_speed = 3.5 
        self.ai_pad_speed_initial = 3.5

        self.ai_initial_pad_x_pos = self.screen_width - self.pad_width - 15
        self.ai_initial_pad_y_pos = self.screen_height/2 - self.ai_pad_height/2
        self.ai_pad_x_pos = self.ai_initial_pad_x_pos
        self.ai_pad_y_pos = self.ai_initial_pad_y_pos

        self.temp_ai_pad_image = pygame.image.load('pong-the-game/images/pad.png')
        self.ai_pad_image = pygame.transform.smoothscale( self.temp_ai_pad_image , [ self.ai_pad_width , self.ai_pad_height ])

        #sp game
        self.sp_pad_height = 250
        self.sp_pad_width = 20
        self.sp_pad_speed = 3.5 

        self.sp_initial_pad_x_pos = 15
        self.sp_initial_pad_y_pos = self.screen_height/2 - self.sp_pad_height/2
        self.sp_pad_x_pos = self.sp_initial_pad_x_pos
        self.sp_pad_y_pos = self.sp_initial_pad_y_pos

        self.temp_sp_pad_image = pygame.image.load('pong-the-game/images/pad.png')
        self.sp_pad_image = pygame.transform.smoothscale( self.temp_sp_pad_image , [ self.sp_pad_width , self.sp_pad_height ])

        #ball
        self.sp_ball_size = 30
        self.sp_ball_speed_x_initial = 250
        self.sp_ball_speed_x = 250
        self.sp_ball_speed_y = 2.5
        self.sp_ball_speed_inc = 25
        self.sp_max_ball_speed = 800
        self.sp_temp_ball_image = pygame.image.load('pong-the-game/images/ball.png')
        self.sp_ball_image = pygame.transform.smoothscale( self.sp_temp_ball_image , [ self.ball_size , self.ball_size])
        
        self.sp_initial_ball_x_pos = (self.screen_width/2) - (self.sp_ball_size/2)
        self.sp_initial_ball_y_pos = (self.screen_height/2) - (self.sp_ball_size/2)
        self.sp_ball_x_pos = self.sp_initial_ball_x_pos
        self.sp_ball_y_pos = self.sp_initial_ball_y_pos

        self.ball_delay = 0

        self.sp_initial_ball1_x_pos = 80
        self.sp_initial_ball1_y_pos = (self.screen_height/2) - (self.sp_ball_size/2)
        self.sp_ball1_x_pos = self.sp_initial_ball1_x_pos
        self.sp_ball1_y_pos = self.sp_initial_ball1_y_pos

        self.sp_initial_ball2_x_pos = self.screen_width - self.ball_size - 80 
        self.sp_initial_ball2_y_pos = (self.screen_height/2) - (self.sp_ball_size/2)
        self.sp_ball2_x_pos = self.sp_initial_ball2_x_pos
        self.sp_ball2_y_pos = self.sp_initial_ball2_y_pos


        #sp select screen
        self.level_select_circle = 100
        self.temp_clear_ball_image = pygame.image.load('pong-the-game/images/clear_ball.png')
        self.clear_ball_image = pygame.transform.smoothscale( self.temp_clear_ball_image , [ self.level_select_circle , self.level_select_circle])
        self.temp_filled_ball_image = pygame.image.load('pong-the-game/images/ball.png')
        self.filled_ball_image = pygame.transform.smoothscale( self.temp_filled_ball_image , [ self.level_select_circle , self.level_select_circle])
        
        self.bg_color_select = (50,50,50)
        self.num_color = (235,235,235)
        self.one_image = self.font_40.render("1" , True , self.num_color , self.bg_color_select)
        self.two_image = self.font_40.render("2" , True , self.num_color , self.bg_color_select)
        self.three_image = self.font_40.render("3" , True , self.num_color , self.bg_color_select)
        self.four_image = self.font_40.render("4" , True , self.num_color , self.bg_color_select)
        self.five_image = self.font_40.render("5" , True , self.num_color , self.bg_color_select)
        self.six_image = self.font_40.render("6" , True , self.num_color , self.bg_color_select)

        self.cl_one_image = self.font_40.render("1" , True , self.text_color , self.bg_color)
        self.cl_two_image = self.font_40.render("2" , True , self.text_color , self.bg_color)
        self.cl_three_image = self.font_40.render("3" , True , self.text_color , self.bg_color)
        self.cl_four_image = self.font_40.render("4" , True , self.text_color , self.bg_color)
        self.cl_five_image = self.font_40.render("5" , True , self.text_color , self.bg_color)
        self.cl_six_image = self.font_40.render("6" , True , self.text_color , self.bg_color)

        #delay timings 
        self.win_screen_delay_initial = 500
        self.win_screen_delay = 500

        #sounds
        self.hit = pygame.mixer.Sound('pong-the-game/sound_effect/hit.wav')
        self.hit.set_volume(0.35) 
        self.change = pygame.mixer.Sound('pong-the-game/sound_effect/screen_change.wav')
        self.change.set_volume(0.35) 
        self.select = pygame.mixer.Sound('pong-the-game/sound_effect/select.wav')
        self.select.set_volume(0.35) 

        #setting
        self.ball_speed_image = self.font_60.render("Ball Speed" , True , self.text_color , self.bg_color) 
        self.ball_speed_image_rect = self.ball_speed_image.get_rect()
        self.ball_speed_image_x = self.screen_width/4 - 300
        self.ball_speed_image_y = self.screen_height/6 - self.ball_speed_image_rect[3]/2

        self.pad_size_image = self.font_60.render("Pad Size" , True , self.text_color , self.bg_color) 
        self.pad_size_image_rect = self.pad_size_image.get_rect()
        self.pad_size_image_x = self.screen_width/4 - 300
        self.pad_size_image_y = 2*self.screen_height/6 - self.pad_size_image_rect[3]/2

        self.win_point_image = self.font_60.render("Win Points" , True , self.text_color , self.bg_color) 
        self.win_point_image_rect = self.win_point_image.get_rect()
        self.win_point_image_x = self.screen_width/4 - 300
        self.win_point_image_y = 3*self.screen_height/6 - self.win_point_image_rect[3]/2     

        self.bg_music_image = self.font_60.render("BG Music" , True , self.text_color , self.bg_color) 
        self.bg_music_image_rect = self.bg_music_image.get_rect()
        self.bg_music_image_x = self.screen_width/4 - 300
        self.bg_music_image_y = 4*self.screen_height/6 - self.bg_music_image_rect[3]/2  

        self.on_image = self.font_40.render("on" , True , self.text_color , self.bg_color) 
        self.on_image_rect = self.on_image.get_rect()
        self.on_image_x = 2*self.screen_width/4
        self.on_image_y = 4*self.screen_height/6 - self.on_image_rect[3]/2  

        self.off_image = self.font_40.render("off" , True , self.text_color , self.bg_color) 
        self.off_image_rect = self.off_image.get_rect()
        self.off_image_x = 3*self.screen_width/4 
        self.off_image_y = 4*self.screen_height/6 - self.off_image_rect[3]/2  

        self.music_volume_image = self.font_60.render("Music Volume" , True , self.text_color , self.bg_color) 
        self.music_volume_image_rect = self.music_volume_image.get_rect()
        self.music_volume_image_x = self.screen_width/4 - 300
        self.music_volume_image_y = 5*self.screen_height/6 - self.music_volume_image_rect[3]/2  
                        
        self.boxes_size = 50
        self.temp_box_image = pygame.image.load('pong-the-game/images/box.png')
        self.temp_filled_box_image = pygame.image.load('pong-the-game/images/filled_box.png')
        self.box_image = pygame.transform.smoothscale( self.temp_box_image , [self.boxes_size , self.boxes_size])
        self.filled_box_image = pygame.transform.smoothscale( self.temp_filled_box_image , [self.boxes_size , self.boxes_size])

        self.bar_width = 1000
        self.bar_height = 50
        self.temp_bar_image = pygame.image.load('pong-the-game/images/bar.png')
        self.bar_image = pygame.transform.smoothscale( self.temp_bar_image , [ self.bar_width , self.bar_height])
        self.bar_image_rect = self.bar_image.get_rect()
        self.bar_x = 2*self.screen_width/3 - self.bar_image_rect[2]/2

        self.slider_width_speed = 500
        self.slider_width_size = 500
        self.slider_width_win = 200
        self.slider_width_volume = 500
        
        self.slider_x = 2*self.screen_width/3 - self.bar_image_rect[2]/2

    def _update_points(self):

        self.player_1_points = self.font_50.render( str(self.player_1_point) , True , self.text_color , self.bg_color )
        self.player_1_points_rect = self.player_1_points.get_rect()
        self.player_1_points_x = 3*self.screen_width/8 - self.player_1_points_rect[2]/2
        self.player_1_points_y = self.screen_height/8 - self.player_1_points_rect[3]/2

        self.player_2_points = self.font_50.render( str(self.player_2_point) , True , self.text_color , self.bg_color )
        self.player_2_points_rect = self.player_2_points.get_rect()
        self.player_2_points_x = 5*self.screen_width/8 - self.player_2_points_rect[2]/2
        self.player_2_points_y = self.screen_height/8 - self.player_2_points_rect[3]/2
    
    def _update_settings(self):
              
        if self.state.speed_change == True:
            mos_pos = pygame.mouse.get_pos()
            if self.slider_x < mos_pos[0] < self.slider_x + self.bar_width:
                self.ball_speed_x = math.floor(100 + (mos_pos[0] - self.slider_x)/2.5)
                self.ball_speed_x_initial = math.floor(100 + (mos_pos[0] - self.slider_x)/2.5)
            if self.slider_x + 10 < mos_pos[0] < self.slider_x + self.bar_width:
                self.slider_width_speed = mos_pos[0] - self.slider_x 

        if self.state.size_change == True:
            mos_pos = pygame.mouse.get_pos()
            if self.slider_x < mos_pos[0] < self.slider_x + self.bar_width:
                self.pad_height = math.floor(150 + (mos_pos[0] - self.slider_x)/5)
            if self.slider_x + 10 < mos_pos[0] < self.slider_x + self.bar_width:
                self.slider_width_size = mos_pos[0] - self.slider_x 

        if self.state.win_change == True:
            mos_pos = pygame.mouse.get_pos()
            if self.slider_x < mos_pos[0] < self.slider_x + self.bar_width:
                self.winning_points = math.ceil((mos_pos[0] - self.slider_x)/100)
            if self.slider_x + 10 < mos_pos[0] < self.slider_x + self.bar_width:
                self.slider_width_win = mos_pos[0] - self.slider_x 

        if self.state.volume_change == True:
            mos_pos = pygame.mouse.get_pos()
            if self.slider_x < mos_pos[0] < self.slider_x + self.bar_width:
                pygame.mixer.music.set_volume( math.ceil((mos_pos[0] - self.slider_x)/100)/10 )
            if self.slider_x + 10 < mos_pos[0] < self.slider_x + self.bar_width:
                self.slider_width_volume = mos_pos[0] - self.slider_x 
        
        self.initial_leftpad_x_pos = 15
        self.initial_leftpad_y_pos = self.screen_height/2 - self.pad_height/2
        self.leftpad_x_pos = self.initial_leftpad_x_pos
        self.leftpad_y_pos = self.initial_leftpad_y_pos
        
        self.initial_rightpad_x_pos = self.screen_width - self.pad_width - 15
        self.initial_rightpad_y_pos = self.screen_height/2 - self.pad_height/2
        self.rightpad_x_pos = self.initial_rightpad_x_pos
        self.rightpad_y_pos = self.initial_rightpad_y_pos

        self.pad_image = pygame.transform.smoothscale( self.temp_pad_image , [ self.pad_width , self.pad_height ])

        self.temp_slider_image = pygame.image.load('pong-the-game/images/slider.png')
        self.slider_speed_image = pygame.transform.smoothscale( self.temp_slider_image , [ self.slider_width_speed , self.bar_height])
        self.slider_size_image = pygame.transform.smoothscale( self.temp_slider_image , [ self.slider_width_size , self.bar_height])
        self.slider_win_image = pygame.transform.smoothscale( self.temp_slider_image , [ self.slider_width_win , self.bar_height])
        self.slider_volume_image = pygame.transform.smoothscale( self.temp_slider_image , [ self.slider_width_volume , self.bar_height])

        self.win_num_image = self.font_40.render( str(self.winning_points) , True , self.text_color , self.bg_color )
        self.win_num_image_rect = self.win_num_image.get_rect()
        self.win_num_image_x = 3*self.screen_width/8 - 100

    def _update_yspeed(self):
        
        if self.ball_speed_x < 220:
            self.ball_speed_y = (random.randint(self.ball_speed_x - 75 , self.ball_speed_x + 75))/100
        elif 220 < self.ball_speed_x > 280:
            self.ball_speed_y = (random.randint(self.ball_speed_x - 150 , self.ball_speed_x + 150))/100
        elif self.ball_speed_x > 280:
            self.ball_speed_y = (random.randint(self.ball_speed_x - 225 , self.ball_speed_x + 225))/100

    def _sp_update_yspeed(self):
        
        if self.sp_ball_speed_x < 220:
            self.sp_ball_speed_y = (random.randint(self.sp_ball_speed_x - 75 , self.sp_ball_speed_x + 75))/100
        elif 220 < self.sp_ball_speed_x > 280:
            self.sp_ball_speed_y = (random.randint(self.sp_ball_speed_x - 150 , self.sp_ball_speed_x + 150))/100
        elif self.sp_ball_speed_x > 280:
            self.sp_ball_speed_y = (random.randint(self.sp_ball_speed_x - 225 , self.sp_ball_speed_x + 225))/100
        
    def _sp_update_pad(self):

        if self.state.sp_1_game_start == True:
            self.sp_pad_height = 250
            self.ai_pad_height = 250
        elif self.state.sp_2_game_start == True:
            self.sp_pad_height = 200
            self.ai_pad_height = 300
        elif self.state.sp_3_game_start == True:
            self.sp_pad_height = 150
            self.ai_pad_height = 350
        elif self.state.sp_4_game_start == True:
            self.sp_pad_height = 250
            self.ai_pad_height = 250
        elif self.state.sp_5_game_start == True:
            self.sp_pad_height = 250
            self.ai_pad_height = 250
        elif self.state.sp_6_game_start == True:
            self.sp_pad_height = 250
            self.ai_pad_height = 250
        
        self.sp_pad_image = pygame.transform.smoothscale( self.temp_sp_pad_image , [ self.sp_pad_width , self.sp_pad_height ])
        self.ai_pad_image = pygame.transform.smoothscale( self.temp_ai_pad_image , [ self.ai_pad_width , self.ai_pad_height ])