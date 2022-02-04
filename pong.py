import sys
import pygame
import random

from information import Information
from music_list import Song
from input_events import Input_Events
from state import State
from ball import Ball
from screens import Screens
from pad import Pad

class Pong:
    def __init__(self):
        pygame.init()

        self.state = State()
        self.info = Information(self)
        self.disp = pygame.display.set_mode((self.info.screen_width,self.info.screen_height))
        self.bg_song = Song(self)
        self.screens = Screens(self)
        self.pad = Pad(self)
        self.ball = Ball(self)
        self.input_e = Input_Events(self)
        
        if self.state.bg_music == True:
            self.bg_song.bg_music_play()
    
        pygame.display.set_caption("pong")

    def _check_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.USEREVENT:  
                if len ( self.bg_song.song_list ) > 0:     
                    pygame.mixer.music.queue ( self.bg_song.song_list.pop(random.randint(0,len(self.bg_song.song_list)-1)) )

            self.input_e._check_event(event)

    def _update_screen(self):
        self.disp.fill(self.info.bg_color)

        self.screens._update_screen()
        self.ball._update_ball()
        self.pad._update_pad()

        pygame.display.flip()
        
    def run_game(self):

        while True:
            self._check_event()
            self._update_screen()
    
if __name__ == "__main__":

    ai = Pong()
    ai.run_game()