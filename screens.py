import pygame

class Screens:
    def __init__(self,ai_game):

        self.disp = ai_game.disp
        self.state = ai_game.state
        self.info = ai_game.info

    def _update_screen(self):
        
        if self.state.home_screen == True:
            self._home_screen()

        if self.state.settings_screen == True:
            self._settings_screen()

        self.sp_game()
        self.mp_game()

    def _home_screen(self):        
        pygame.mouse.set_visible(True)

        self.disp.blit(self.info.multiplayer_image , [self.info.mp_x , self.info.mp_y])
        
        self.disp.blit(self.info.singleplayer_image , [self.info.sp_x , self.info.sp_y])

        self.disp.blit(self.info.settings_image , [self.info.set_x , self.info.set_y])

        self.disp.blit(self.info.pong_image , [ self.info.pong_x , self.info.pong_y ])

    def mp_game(self):

        if self.state.mp_game_active == True:
            self.disp.blit(self.info.middle_bar , [ self.info.screen_width/2 - self.info.mid_divider_width/2 , 0 ] )

            self.info._update_points()

            self.disp.blit(self.info.player_1_points , [ self.info.player_1_points_x , self.info.player_1_points_y])
            self.disp.blit(self.info.player_2_points , [ self.info.player_2_points_x , self.info.player_2_points_y])

        if self.state.mp_game_start == True:
            self.info.ball_speed_x = self.info.ball_speed_x_initial
            self.disp.blit(self.info.how_start , [ self.info.how_start_x , self.info.how_start_y ])

        if self.state.mp_win_screen == True:
            if self.info.player_1_point == self.info.winning_points:
                self.disp.blit(self.info.p1_win_image , [ self.info.p1_win_x , self.info.p1_win_y])

            if self.info.player_2_point == self.info.winning_points:
                self.disp.blit(self.info.p2_win_image , [ self.info.p2_win_x , self.info.p2_win_y])
            
            if self.info.win_screen_delay > 0:
                self.info.win_screen_delay -= 1
            else:
                self.state.home_screen = True
                self.state.mp_win_screen = False
                self.info.ball_speed_x = self.info.ball_speed_x_initial
                self.info.win_screen_delay = self.info.win_screen_delay_initial
                pygame.mouse.set_visible(True)
                self.info.player_1_point = 0
                self.info.player_2_point = 0

    def _settings_screen(self):
        pygame.mouse.set_visible(True)
        self.info._update_settings()

        self.disp.blit( self.info.ball_speed_image , [ self.info.ball_speed_image_x , self.info.ball_speed_image_y])
        self.disp.blit( self.info.pad_size_image , [ self.info.pad_size_image_x , self.info.pad_size_image_y])
        self.disp.blit( self.info.win_point_image , [ self.info.win_point_image_x , self.info.win_point_image_y])
        self.disp.blit( self.info.bg_music_image , [ self.info.bg_music_image_x , self.info.bg_music_image_y])
        self.disp.blit( self.info.music_volume_image , [ self.info.music_volume_image_x , self.info.music_volume_image_y])

        self.disp.blit( self.info.on_image , [ self.info.on_image_x , self.info.on_image_y])
        self.disp.blit( self.info.off_image , [ self.info.off_image_x , self.info.off_image_y])
        self.disp.blit( self.info.box_image , [ self.info.on_image_x + 100, self.info.on_image_y] )
        self.disp.blit( self.info.box_image , [ self.info.off_image_x + 100, self.info.off_image_y] )

        if self.state.bg_music == True:
            self.disp.blit( self.info.filled_box_image , [ self.info.on_image_x + 100, self.info.on_image_y] )
        else:
            self.disp.blit( self.info.filled_box_image , [ self.info.off_image_x + 100, self.info.off_image_y] )

        self.disp.blit( self.info.bar_image , [ self.info.bar_x , self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )
        self.disp.blit( self.info.bar_image , [ self.info.bar_x , 2*self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )
        self.disp.blit( self.info.bar_image , [ self.info.bar_x , 3*self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )
        self.disp.blit( self.info.bar_image , [ self.info.bar_x , 5*self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )

        self.disp.blit( self.info.slider_speed_image , [ self.info.slider_x , self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )
        self.disp.blit( self.info.slider_size_image , [ self.info.slider_x , 2*self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )
        self.disp.blit( self.info.slider_win_image , [ self.info.slider_x , 3*self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )
        self.disp.blit( self.info.slider_volume_image , [ self.info.slider_x , 5*self.info.screen_height/6 - self.info.bar_image_rect[3]/2] )

        self.disp.blit( self.info.win_num_image , [ self.info.win_num_image_x ,  3*self.info.screen_height/6 - self.info.win_num_image_rect[3]/2 ])

    def sp_game(self):
        if self.state.sp_select_screen == True:

            self.disp.blit( self.info.clear_ball_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2])
            if self.state.sp_1_game_start == False:
                self.disp.blit( self.info.cl_one_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 + 43 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
            else:
                self.disp.blit( self.info.filled_ball_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2])
                self.disp.blit( self.info.one_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 + 43 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])

            self.disp.blit( self.info.clear_ball_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2])
            if self.state.sp_2_game_start == False:
                self.disp.blit( self.info.cl_two_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
            else:
                self.disp.blit( self.info.filled_ball_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2])
                self.disp.blit( self.info.two_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])

            self.disp.blit( self.info.clear_ball_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2])
            if self.state.sp_3_game_start == False:
                self.disp.blit( self.info.cl_three_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
            else:
                self.disp.blit( self.info.filled_ball_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2])
                self.disp.blit( self.info.three_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  1*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])

            self.disp.blit( self.info.clear_ball_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2])
            if self.state.sp_4_game_start == False:
                self.disp.blit( self.info.cl_four_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
            else:
                self.disp.blit( self.info.filled_ball_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2])
                self.disp.blit( self.info.four_image , [ 1*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])

            self.disp.blit( self.info.clear_ball_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2])
            if self.state.sp_5_game_start == False:
                self.disp.blit( self.info.cl_five_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
            else:
                self.disp.blit( self.info.filled_ball_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2])
                self.disp.blit( self.info.five_image , [ 2*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])

            self.disp.blit( self.info.clear_ball_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2])
            if self.state.sp_6_game_start == False:
                self.disp.blit( self.info.cl_six_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
            else:
                self.disp.blit( self.info.filled_ball_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2])
                self.disp.blit( self.info.six_image , [ 3*self.info.screen_width/4 - self.info.level_select_circle/2 + 38 ,  2*self.info.screen_height/4 - self.info.level_select_circle/2 + 24 ])
             
            self.disp.blit(self.info.how_start , [ self.info.how_start_x ,  3*self.info.screen_height/4 - self.info.how_start_rect[3]/2])
        
        if self.state.sp_game_active == True:
            
            if self.state.sp_1_game_start == True or self.state.sp_2_game_start == True or self.state.sp_3_game_start == True:
                self.disp.blit(self.info.middle_bar , [ self.info.screen_width/2 - self.info.mid_divider_width/2 , 0 ] )
            elif self.state.sp_4_game_start == True:
                self.disp.blit(self.info.mid_filled_bar , [ self.info.screen_width/2 - self.info.mid_divider_width/2 , 0 ] )
