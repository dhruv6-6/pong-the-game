import pygame

class Bricks:
    def __init__ (self,ai_game):

        self.disp = ai_game.disp
        self.info = ai_game.info
        self.state = ai_game.state
        self.pad = ai_game.pad

    def _update_brick(self):
        self._print_bricks()
        self._win_lose()
    
    def _print_bricks(self):
        for i in range(0 , len(self.info.bricks1_x)):
            self.disp.blit(self.info.brick_image , [self.info.bricks1_x[i] , self.info.bricks1_y[i]])
        for i in range(0 , len(self.info.bricks2_x)):
            self.disp.blit(self.info.brick_image , [self.info.bricks2_x[i] , self.info.bricks2_y[i]])
    
    def _win_lose(self):
        if len(self.info.bricks1_x) == 0:
            self.state.win_screen = True
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
    
        if len(self.info.bricks2_x) == 0:
            self.state.lose_screen = True
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

        if self.state.win_screen == True:
            while self.info.sp_win_screen_delay != 0:
                self.disp.blit(self.info.win_image , [self.info.win_x , self.info.win_y]) 
                self.info.sp_win_screen_delay -= 1
            self.info.sp_win_screen_delay = self.info.sp_win_screen_delay_initial
            self.state.win_screen = False
            self.state.sp_select_screen = True
        
        if self.state.lose_screen == True:
            while self.info.sp_win_screen_delay != 0:
                self.disp.blit(self.info.lose_image , [self.info.lose_x , self.info.lose_y]) 
                self.info.sp_win_screen_delay -= 1
            self.info.sp_win_screen_delay = self.info.sp_win_screen_delay_initial
            self.state.lose_screen = False
            self.state.sp_select_screen = True

        