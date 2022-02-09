import pygame
import random

class Song():
    def __init__(self,ai_game):
        self.info = ai_game.info

        self.song_list = []

        self.song_list.append('background_music/Air.mp3')
        self.song_list.append('background_music/August.mp3')
        self.song_list.append('background_music/Behind Clouds & sar.casm - Wonders of the Unknown.mp3')
        self.song_list.append('background_music/blessin.mp3')
        self.song_list.append('background_music/Daffodils.mp3')
        self.song_list.append('background_music/Hindsight.mp3')
        self.song_list.append('background_music/hyperparadise - morning.mp3')
        self.song_list.append('background_music/I Have Love for Everyone Besides Myself.mp3')
        self.song_list.append('background_music/Joan of Arc.mp3')
        self.song_list.append('background_music/last time.mp3')
        self.song_list.append('background_music/Lofi Smoke and Pass Out.mp3')
        self.song_list.append('background_music/mommy - ocean floor.mp3')
        self.song_list.append('background_music/No Samples.mp3')
        self.song_list.append('background_music/ORANGE.mp3')
        self.song_list.append("background_music/Sarcastic Sounds - It's Ok To Cry.mp3")
        self.song_list.append('background_music/sekao.mp3')
        self.song_list.append('background_music/Shinigami.mp3')
        self.song_list.append('background_music/sorry.mp3')
        self.song_list.append('background_music/summer nights.mp3')
        self.song_list.append('background_music/The Best Moment.mp3')
        self.song_list.append('background_music/Ukulele and Chill.mp3')
        self.song_list.append('background_music/us.mp3')
        self.song_list.append('background_music/With U.mp3')

    def bg_music_play(self):
        
        pygame.mixer.music.load ( self.song_list.pop(random.randint(0,len(self.song_list)-1)) )  
        pygame.mixer.music.queue ( self.song_list.pop(random.randint(0,len(self.song_list)-1)) ) 
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )  
        pygame.mixer.music.play() 
        pygame.mixer.music.set_volume(0.5) 