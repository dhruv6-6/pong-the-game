from tkinter.tix import Tree


class State:

    def __init__(self):
        
        self.home_screen = True
        self.settings_screen = False
        self.highscore_screen = False

        self.mp_game_start = False
        self.mp_game_active = False
        self.mp_win_screen = False

        self.sp_game_active = False  
        self.sp_select_screen = False
        self.sp_1_game_start = True
        self.sp_2_game_start = False
        self.sp_3_game_start = False
        self.sp_4_game_start = False
        self.sp_5_game_start = False
        self.sp_6_game_start = False
        self.sp_win_screen = False

        self.ball_moving_right = True
        self.ball_moving_up = True

        self.leftpad_up = False
        self.leftpad_down = False
        self.rightpad_up = False
        self.rightpad_down = False

        self.speed_change = False
        self.size_change = False
        self.win_change = False
        self.volume_change = False

        self.bg_music = True
        
        self.sp_pad_up = False
        self.sp_pad_down = False

        self.sp_ball_moving_up = True
        self.sp_ball_moving_right = True 

        self.sp_ball1_moving_up = False
        self.sp_ball1_moving_right = True

        self.sp_ball2_moving_up = True
        self.sp_ball2_moving_right = False