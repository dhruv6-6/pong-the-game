class Pad:

    def __init__(self,ai_game):
        self.disp = ai_game.disp
        self.state = ai_game.state
        self.info = ai_game.info

    def _update_pad(self):

        if self.state.mp_game_active == True:
            self._mp_pad()
        
        if self.state.sp_game_active == True:
            self._sp_pad()
    
    def _mp_pad(self):
        
        self.disp.blit(self.info.pad_image , [self.info.leftpad_x_pos , self.info.leftpad_y_pos])
        self.disp.blit(self.info.pad_image , [self.info.rightpad_x_pos , self.info.rightpad_y_pos])

        if self.state.leftpad_up == True and self.info.leftpad_y_pos > 15:
            self.info.leftpad_y_pos -= self.info.pad_speed
        
        if self.state.leftpad_down == True and self.info.leftpad_y_pos < self.info.screen_height - self.info.pad_height - 15:
            self.info.leftpad_y_pos += self.info.pad_speed
        
        if self.state.rightpad_up == True and self.info.rightpad_y_pos > 15:
            self.info.rightpad_y_pos -= self.info.pad_speed
        
        if self.state.rightpad_down == True and self.info.rightpad_y_pos < self.info.screen_height - self.info.pad_height - 15:
            self.info.rightpad_y_pos += self.info.pad_speed

    def _sp_update_pad(self):

        if self.state.sp_1_game_start == True or self.state.sp_2_game_start == True or self.state.sp_3_game_start == True:
            if self.state.sp_ball_moving_right == True:
                if (self.info.ai_pad_y_pos + self.info.ai_pad_height/2 >= self.info.sp_ball_y_pos) and (self.info.ai_pad_y_pos > 15):
                    self.info.ai_pad_y_pos -= self.info.ai_pad_speed
                elif self.info.sp_ball_y_pos >= self.info.ai_pad_y_pos+self.info.ai_pad_height/2 and (self.info.ai_pad_y_pos + self.info.ai_pad_height< self.info.screen_height - 15):
                    self.info.ai_pad_y_pos += self.info.ai_pad_speed
        elif self.state.sp_4_game_start == True:
            if (self.info.ai_pad_y_pos + self.info.ai_pad_height/2 >= self.info.sp_ball2_y_pos) and (self.info.ai_pad_y_pos > 15):
                    self.info.ai_pad_y_pos -= self.info.ai_pad_speed
            elif self.info.sp_ball2_y_pos >= self.info.ai_pad_y_pos+self.info.ai_pad_height/2 and (self.info.ai_pad_y_pos + self.info.ai_pad_height< self.info.screen_height - 15):
                self.info.ai_pad_y_pos += self.info.ai_pad_speed

    def _sp_pad(self):
        self._sp_update_pad()

        self.disp.blit(self.info.sp_pad_image , [self.info.sp_pad_x_pos , self.info.sp_pad_y_pos])
        self.disp.blit(self.info.ai_pad_image , [self.info.ai_pad_x_pos , self.info.ai_pad_y_pos])

        if self.state.sp_pad_up == True and self.info.sp_pad_y_pos > 15:
            self.info.sp_pad_y_pos -= self.info.sp_pad_speed
        
        if self.state.sp_pad_down == True and self.info.sp_pad_y_pos < self.info.screen_height - self.info.sp_pad_height - 15:
            self.info.sp_pad_y_pos += self.info.sp_pad_speed