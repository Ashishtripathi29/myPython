import pygame

class Create_sound(pygame):
    def __init__(sound_file):
        super().__init__()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()






    # def play_sound(sound_file):
    #     pygame.init()
    #     pygame.mixer.init()
    #     pygame.mixer.music.load(sound_file)
    #     pygame.mixer.music.play()
