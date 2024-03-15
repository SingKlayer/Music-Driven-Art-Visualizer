import pygame
import numpy as np
import pygame.freetype
import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def load_music(music_file):
    y, sr = librosa.load(music_file)
    D = np.abs(librosa.stft(y))
    S = librosa.amplitude_to_db(D, ref=np.max)  
    return y, sr, S

def select_random_colormap():
    return random.choice(list(plt.colormaps()))

def apply_colormap(S, colormap_name):
    random_colormap_generator = getattr(cm, colormap_name)
    colormap_generator_caller = random_colormap_generator((S - S.min()) / (S.max() - S.min()))
    return colormap_generator_caller

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)

def main():
    try:
        pygame.init()
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Music-Driven Art Visualizer')

        #Add your song to the folder and replace the name.
        music_file = 'Sample_Song.mp3'
        
        y, sr, S = load_music(music_file)

        colormaps = list(plt.colormaps())
        random_colormap = select_random_colormap()
        S_color = apply_colormap(S, random_colormap)

        play_music(music_file)

        running = True
        clock = pygame.time.Clock()

        waveform_change_y = 800
        waveform_change_x = 0
        steps = 50

        last = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            now = pygame.time.get_ticks()

            if now - last >= steps:
                last = now

                if waveform_change_x >= 800:
                    waveform_change_y = 400
                    waveform_change_x = 800
                else:
                    waveform_change_y -= 1
                    waveform_change_x += 1

            screen.fill((0, 0, 0))

            frame = pygame.surfarray.make_surface(S_color[:waveform_change_x, :waveform_change_y, :3] * 255)
            frame = pygame.transform.scale(frame, (width, height))

            screen.blit(frame, (0, 0))
            pygame.display.flip()
            clock.tick(10)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()