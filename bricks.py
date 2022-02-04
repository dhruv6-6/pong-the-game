import pygame

class Bricks:
    def __init__ (self,ai_game):

        self.disp = ai_game.disp
        self.info = ai_game.info
        self.state = ai_game.state
        self.pad = ai_game.pad

    def _update_brick(self):
        self._print_bricks()
    
    def _print_bricks(self):
        for i in range(0 , len(self.info.bricks1_x)):
            self.disp.blit(self.info.brick_image , [self.info.bricks1_x[i] , self.info.bricks1_y[i]])
        for i in range(0 , len(self.info.bricks2_x)):
            self.disp.blit(self.info.brick_image , [self.info.bricks2_x[i] , self.info.bricks2_y[i]])

        