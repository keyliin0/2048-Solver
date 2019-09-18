import gym_2048
import gym
import pygame
import search
grid_size = 70

def render(screen, observation):
  black = (0, 0, 0)
  grey = (128, 128, 128)
  blue = (0, 0, 128)
  white = (255, 255, 255)
  tile_colour_map = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (234, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237,204,97),
    512: (237,200,80),
    1024: (237,197,63),
    2048: (237,197,1),
  }
  # Background
  screen.fill(black)
  # Board
  pygame.draw.rect(screen, grey, (0, 0, grid_size * 4, grid_size * 4))
  myfont = pygame.font.SysFont('Tahome', 30)
  for y in range(4):
    for x in range(4):
      o = observation[y][x]
      if o:
        pygame.draw.rect(screen, tile_colour_map[o], (x * grid_size, y * grid_size, grid_size, grid_size))
        text = myfont.render(str(o), False, white)
        text_rect = text.get_rect()
        width = text_rect.width
        height = text_rect.height
        assert width < grid_size
        assert height < grid_size
        screen.blit(text, (x * grid_size + grid_size / 2 - text_rect.width / 2,
                           y * grid_size + grid_size / 2 - text_rect.height / 2))
  pygame.display.update()

env = gym.make('2048-v0')
env.seed(42)
search = search
search.init()
height = 4 * grid_size
width = 4 * grid_size
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.font.init()
current_state = env.reset()
done = False

while not done:
    best_action = search.get_best_move(env, current_state)
    new_state, reward, done, info = env.step(best_action)
    current_state = new_state
    render(screen, new_state)
env.render()
env.close()