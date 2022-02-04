import pygame
class Ball:
    def __init__ (self,ai_game):

        self.disp = ai_game.disp
        self.info = ai_game.info
        self.state = ai_game.state
        self.pad = ai_game.pad

    def _update_ball(self):

        if self.state.mp_game_active == True:
            self._mp_ball()
        if self.state.sp_game_active == True:
            self._sp_ball()
            
    def _mp_ball(self):
        
        self.disp.blit(self.info.ball_image , [self.info.ball_x_pos , self.info.ball_y_pos])

        if self.info.ball_y_pos <= 0:
            self.state.ball_moving_up = False
        elif self.info.ball_y_pos + self.info.ball_size >= self.info.screen_height:
            self.state.ball_moving_up = True

        if self.state.ball_moving_right == True:
            self.info.ball_x_pos += self.info.ball_speed_x/100

            if self.info.rightpad_x_pos - self.info.ball_size -4 <= self.info.ball_x_pos <= self.info.rightpad_x_pos - self.info.ball_size + 4 and self.info.rightpad_y_pos - 20 <= self.info.ball_y_pos <= self.info.rightpad_y_pos + self.info.pad_height + 20:
                self.info.hit.play()
                self.state.ball_moving_right = False    
                self.info._update_yspeed()
                self.info.ball_speed_x += self.info.ball_speed_inc

            if self.info.ball_x_pos > self.info.screen_width - self.info.ball_size:
                self.info.player_1_point += 1
                self.state.mp_game_start = True
                self.state.mp_game_active = False
                self.state.ball_moving_right = False

                if self.info.player_1_point == self.info.winning_points:
                    self.state.mp_win_screen = True
                    self.state.mp_game_active = False
                    self.state.mp_game_start = False

        elif self.state.ball_moving_right == False:
            self.info.ball_x_pos -= self.info.ball_speed_x/100

            if self.info.leftpad_x_pos + self.info.pad_width -4 <= self.info.ball_x_pos <= self.info.leftpad_x_pos + self.info.pad_width + 4 and self.info.leftpad_y_pos - 20 <= self.info.ball_y_pos <= self.info.leftpad_y_pos + self.info.pad_height + 20:
                self.info.hit.play()
                self.state.ball_moving_right = True
                self.info._update_yspeed()
                self.info.ball_speed_x += self.info.ball_speed_inc

            if self.info.ball_x_pos < 0:
                self.info.player_2_point += 1
                self.state.mp_game_start = True
                self.state.mp_game_active = False 
                self.state.ball_moving_right = True

                if self.info.player_2_point == self.info.winning_points:
                    self.state.mp_win_screen = True
                    self.state.mp_game_active = False
                    self.state.mp_game_start = False

        if self.state.ball_moving_up == True:
            self.info.ball_y_pos -= self.info.ball_speed_y
        elif self.state.ball_moving_up == False:
            self.info.ball_y_pos += self.info.ball_speed_y
    
    def _sp_ball(self):
        if self.state.sp_1_game_start == True or self.state.sp_2_game_start == True or self.state.sp_3_game_start == True:
            self.disp.blit(self.info.sp_ball_image , [self.info.sp_ball_x_pos , self.info.sp_ball_y_pos])

            if self.info.sp_ball_y_pos <= 0:
                self.state.sp_ball_moving_up = False
            elif self.info.sp_ball_y_pos + self.info.sp_ball_size >= self.info.screen_height:
                self.state.sp_ball_moving_up = True

            if self.state.sp_ball_moving_right == True:
                self.info.sp_ball_x_pos += self.info.sp_ball_speed_x/100

                if self.info.ai_pad_x_pos - self.info.sp_ball_size -4 <= self.info.sp_ball_x_pos <= self.info.ai_pad_x_pos - self.info.sp_ball_size + 4 and self.info.ai_pad_y_pos - 20 <= self.info.sp_ball_y_pos <= self.info.ai_pad_y_pos + self.info.ai_pad_height + 20:
                    self.info.hit.play()
                    self.state.sp_ball_moving_right = False    
                    self.info._sp_update_yspeed()
                    self.info.sp_ball_speed_x += self.info.sp_ball_speed_inc

                if self.info.sp_ball_x_pos > self.info.screen_width - self.info.sp_ball_size:
                    self.info.sp_ball_speed_x = self.info.sp_ball_speed_x_initial 
                    self.state.sp_select_screen = True
                    self.state.sp_game_active = False
                    self.state.sp_ball_moving_right = False
                    pygame.mouse.set_visible(True)

            elif self.state.sp_ball_moving_right == False:
                self.info.sp_ball_x_pos -= self.info.sp_ball_speed_x/100

                if self.info.sp_pad_x_pos + self.info.sp_pad_width -4 <= self.info.sp_ball_x_pos <= self.info.sp_pad_x_pos + self.info.sp_pad_width + 4 and self.info.sp_pad_y_pos - 20 <= self.info.sp_ball_y_pos <= self.info.sp_pad_y_pos + self.info.sp_pad_height + 20:
                    self.info.hit.play()
                    self.state.sp_ball_moving_right = True
                    self.info._sp_update_yspeed()
                    self.info.sp_ball_speed_x += self.info.sp_ball_speed_inc

                if self.info.sp_ball_x_pos < 0:
                    self.info.sp_ball_speed_x = self.info.sp_ball_speed_x_initial
                    self.state.sp_select_screen = True
                    self.state.sp_game_active = False 
                    self.state.sp_ball_moving_right = True
                    pygame.mouse.set_visible(True)

            if self.state.sp_ball_moving_up == True:
                self.info.sp_ball_y_pos -= self.info.sp_ball_speed_y
            elif self.state.sp_ball_moving_up == False:
                self.info.sp_ball_y_pos += self.info.sp_ball_speed_y

        elif self.state.sp_4_game_start == True:
            self.disp.blit(self.info.sp_ball_image , [self.info.sp_ball1_x_pos , self.info.sp_ball1_y_pos])
            self.disp.blit(self.info.sp_ball_image , [self.info.sp_ball2_x_pos , self.info.sp_ball2_y_pos])
            if self.info.ball_delay == 0:

                if self.info.sp_ball1_y_pos <= 0:
                    self.state.sp_ball1_moving_up = False
                elif self.info.sp_ball1_y_pos + self.info.sp_ball_size >= self.info.screen_height:
                    self.state.sp_ball1_moving_up = True

                if self.state.sp_ball1_moving_right == True:
                    self.info.sp_ball1_x_pos += self.info.sp_ball_speed_x/100

                    if self.info.sp_ball1_x_pos > self.info.screen_width/2 - self.info.ball_size:
                        self.state.sp_ball1_moving_right = False    

                elif self.state.sp_ball1_moving_right == False:
                    self.info.sp_ball1_x_pos -= self.info.sp_ball_speed_x/100

                    if self.info.sp_pad_x_pos + self.info.sp_pad_width -4 <= self.info.sp_ball1_x_pos <= self.info.sp_pad_x_pos + self.info.sp_pad_width + 4 and self.info.sp_pad_y_pos - 20 <= self.info.sp_ball1_y_pos <= self.info.sp_pad_y_pos + self.info.sp_pad_height + 20:
                        self.info.hit.play()
                        self.state.sp_ball1_moving_right = True
                        self.info._sp_update_yspeed()
                        self.info.sp_ball_speed_x += self.info.sp_ball_speed_inc

                    if self.info.sp_ball1_x_pos < 0:
                        self.info.sp_ball_speed_x = self.info.sp_ball_speed_x_initial
                        self.info.sp_ball1_x_pos = self.info.sp_initial_ball1_x_pos
                        self.info.sp_ball1_y_pos = self.info.sp_initial_ball1_y_pos
                        self.info.ball_delay = 600
                        self.state.sp_ball1_moving_right = True

                if self.state.sp_ball1_moving_up == True:
                    self.info.sp_ball1_y_pos -= self.info.sp_ball_speed_y
                elif self.state.sp_ball1_moving_up == False:
                    self.info.sp_ball1_y_pos += self.info.sp_ball_speed_y

            else:
                self.info.ball_delay -= 1