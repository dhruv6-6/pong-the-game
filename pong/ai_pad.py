import pygame

class Ai_Pad():
    def __init__(self , ai_game):
        self.info = ai_game.info
        self.state = ai_game.state
        self.screens = ai_game.screens

    def _update_pad(self):

        if self.state.sp_ball_moving_right == True:
            if (self.info.ai_pad_y_pos + self.info.ai_pad_height/2 >= self.info.sp_ball_y_pos) and (self.info.ai_pad_y_pos > 15):
                self.info.ai_pad_y_pos -= self.info.ai_pad_speed
            elif self.info.sp_ball_y_pos >= self.info.ai_pad_y_pos+self.info.ai_pad_height/2 and (self.info.ai_pad_y_pos + self.info.ai_pad_height< self.info.screen_height - 15):
                self.info.ai_pad_y_pos += self.info.ai_pad_speed
