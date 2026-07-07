import os
import sys
import traceback

def run_with_dummy(dummy):
    if dummy:
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sys.modules.pop('pygame', None)
    try:
        import pygame
        print('Imported pygame', getattr(pygame, '__version__', 'unknown'))
        pygame.init()
        print('pygame.init OK')
        screen = pygame.display.set_mode((200, 200))
        pygame.display.set_caption('Test')
        pygame.event.pump()
        pygame.time.wait(500)
        pygame.quit()
        print(f'Window test OK (dummy={dummy})')
    except Exception as e:
        print(f'Error (dummy={dummy}):', e)
        traceback.print_exc()


if __name__ == '__main__':
    run_with_dummy(False)
    # If the first attempt failed or no display, retry with dummy driver
    if os.environ.get('SDL_VIDEODRIVER') != 'dummy':
        print('Retrying with dummy driver...')
        run_with_dummy(True)
