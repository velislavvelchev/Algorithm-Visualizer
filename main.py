import pygame
import random
pygame.init()

class DrawInformation:
    BLACK = 0, 0 ,0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont("comicsans", 20)
    LARGE_FONT = pygame.font.SysFont("comicsans", 40)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        # create the window

        pygame.display.set_caption("Algorithm Visualizer")
        # set the caption

        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        # take the whole drawable width area (without the padding) and dividing it by the number of the list elements
        # the width of the element would then be relative to how many elements we have

        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        # subtracting max from min val will tell us the number of values we have and then adjust the height relative to that number
        # the bigger the range, the smaller the scale

        self.start_x = self.SIDE_PAD // 2
        # top left corner in (x,y) for pygame is (0, 0)

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Coding | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 5))
    # subtract the w/2 of the screen from t/2 to get the coordinate x of where we should start drawing in order to center the object perfectly in the middle

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 35))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        # if it is the first rectangle, we start from 50 on the x and so on
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        # figure out what the height of the rectangle needs to be, then subtract it from the overall height of the screen

        color = draw_info.GRADIENTS[i % 3]
        # iterate over colors 0, 1, 2

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True

    while run:
        clock.tick(60)

        draw(draw_info)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False


    pygame.quit()


if __name__ == '__main__':
    main()
