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
                if self.info.max_ball_speed >= self.info.ball_speed_x:
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
                if self.info.max_ball_speed >= self.info.ball_speed_x:
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
                    if self.info.sp_max_ball_speed >= self.info.sp_ball_speed_x:
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
                    if self.info.sp_max_ball_speed >= self.info.sp_ball_speed_x:
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
            if self.info.ball1_delay == 0:

                if self.info.sp_ball1_y_pos <= 0:
                    self.state.sp_ball1_moving_up = False
                elif self.info.sp_ball1_y_pos + self.info.sp_ball_size >= self.info.screen_height:
                    self.state.sp_ball1_moving_up = True

                if self.state.sp_ball1_moving_right == True:
                    self.info.sp_ball1_x_pos += self.info.sp_ball1_speed_x/100

                    if self.info.sp_ball1_x_pos > self.info.screen_width/2 - self.info.ball_size:
                        self.state.sp_ball1_moving_right = False    

                    for i in range(0 , len(self.info.bricks1_x)):
                        if self.info.bricks1_x[i] <= self.info.sp_ball1_x_pos + self.info.sp_ball_size <= self.info.bricks1_x[i] + self.info.brick_w and self.info.bricks1_y[i] - 10 <= self.info.sp_ball1_y_pos <= self.info.bricks1_y[i] + self.info.brick_h - self.info.sp_ball_size + 10:
                            self.info.bricks1_x.pop(i)
                            self.info.bricks1_y.pop(i)
                            self.state.sp_ball1_moving_right = False
                            break

                elif self.state.sp_ball1_moving_right == False:
                    self.info.sp_ball1_x_pos -= self.info.sp_ball1_speed_x/100

                    if self.info.sp_pad_x_pos + self.info.sp_pad_width -4 <= self.info.sp_ball1_x_pos <= self.info.sp_pad_x_pos + self.info.sp_pad_width + 4 and self.info.sp_pad_y_pos - 20 <= self.info.sp_ball1_y_pos <= self.info.sp_pad_y_pos + self.info.sp_pad_height + 20:
                        self.info.hit.play()
                        self.state.sp_ball1_moving_right = True
                        self.info._sp_update1_yspeed()
                        if self.info.sp_max_ball_speed >= self.info.sp_ball1_speed_x:
                            self.info.sp_ball1_speed_x += self.info.sp_ball_speed_inc

                    if self.info.sp_ball1_x_pos < 0:
                        self.info.sp_ball1_speed_x = self.info.sp_ball1_speed_x_initial
                        self.info.sp_ball1_x_pos = self.info.sp_initial_ball1_x_pos
                        self.info.sp_ball1_y_pos = self.info.sp_initial_ball1_y_pos
                        self.info.ball1_delay = 600
                        self.state.sp_ball1_moving_right = True

                    for i in range(0 , len(self.info.bricks1_x)):
                        if self.info.bricks1_x[i] <= self.info.sp_ball1_x_pos <= self.info.bricks1_x[i] + self.info.brick_w and self.info.bricks1_y[i] - 10 <= self.info.sp_ball1_y_pos <= self.info.bricks1_y[i] + self.info.brick_h - self.info.sp_ball_size + 10:
                            self.info.bricks1_x.pop(i)
                            self.info.bricks1_y.pop(i)
                            self.state.sp_ball1_moving_right = True
                            break

                if self.state.sp_ball1_moving_up == True:
                    self.info.sp_ball1_y_pos -= self.info.sp_ball1_speed_y
                elif self.state.sp_ball1_moving_up == False:
                    self.info.sp_ball1_y_pos += self.info.sp_ball1_speed_y

            else:
                self.info.ball1_delay -= 1

            if self.info.ball2_delay == 0:

                if self.info.sp_ball2_y_pos <= 0:
                    self.state.sp_ball2_moving_up = False
                elif self.info.sp_ball2_y_pos + self.info.sp_ball_size >= self.info.screen_height:
                    self.state.sp_ball2_moving_up = True

                if self.state.sp_ball2_moving_right == True:
                    self.info.sp_ball2_x_pos += self.info.sp_ball2_speed_x/100

                    if self.info.sp_ball2_x_pos > self.info.screen_width:
                        self.info.sp_ball2_speed_x = self.info.sp_ball2_speed_x_initial
                        self.info.sp_ball2_x_pos = self.info.sp_initial_ball2_x_pos
                        self.info.sp_ball2_y_pos = self.info.sp_initial_ball2_y_pos
                        self.info.ball2_delay = 600
                        self.state.sp_ball2_moving_right = False  

                    if self.info.ai_pad_x_pos + self.info.ai_pad_width -4 <= self.info.sp_ball2_x_pos + self.info.sp_ball_size <= self.info.ai_pad_x_pos + self.info.ai_pad_width + 4 and self.info.ai_pad_y_pos - 20 <= self.info.sp_ball2_y_pos <= self.info.ai_pad_y_pos + self.info.ai_pad_height + 20:
                        self.info.hit.play()
                        self.state.sp_ball2_moving_right = False
                        self.info._sp_update2_yspeed()
                        if self.info.sp_max_ball_speed >= self.info.sp_ball2_speed_x:
                            self.info.sp_ball2_speed_x += self.info.sp_ball_speed_inc
                        
                    for i in range(0 , len(self.info.bricks2_x)):
                        if self.info.bricks2_x[i] <= self.info.sp_ball2_x_pos + self.info.sp_ball_size <= self.info.bricks2_x[i] + self.info.brick_w and self.info.bricks2_y[i] - 20 <= self.info.sp_ball2_y_pos <= self.info.bricks2_y[i] + self.info.brick_h - self.info.sp_ball_size + 20:
                            self.info.bricks2_x.pop(i)
                            self.info.bricks2_y.pop(i)
                            self.state.sp_ball2_moving_right = False
                            break

                elif self.state.sp_ball2_moving_right == False:
                    self.info.sp_ball2_x_pos -= self.info.sp_ball2_speed_x/100

                    if self.info.sp_ball2_x_pos < self.info.screen_width/2:
                        self.state.sp_ball2_moving_right = True

                    for i in range(0 , len(self.info.bricks2_x)):
                        if self.info.bricks2_x[i] <= self.info.sp_ball2_x_pos <= self.info.bricks2_x[i] + self.info.brick_w and self.info.bricks2_y[i] - 20 <= self.info.sp_ball2_y_pos <= self.info.bricks2_y[i] + self.info.brick_h - self.info.sp_ball_size + 20:
                            self.info.bricks2_x.pop(i)
                            self.info.bricks2_y.pop(i)
                            self.state.sp_ball2_moving_right = True
                            break

                if self.state.sp_ball2_moving_up == True:
                    self.info.sp_ball2_y_pos -= self.info.sp_ball2_speed_y
                elif self.state.sp_ball2_moving_up == False:
                    self.info.sp_ball2_y_pos += self.info.sp_ball2_speed_y

            else:
                self.info.ball2_delay -= 1


