import pygame

x = pygame.image.load("close.png")
o = pygame.image.load("circle-ring.png")
background_color = (241, 250, 238)
match_over_background = (17, 138, 178)
match_over_color = (244, 162, 97)

def check_who_won(grid):
    x_pos = []
    o_pos = []
    x_values = [0] * 8
    o_values = [0] * 8
    """
    x_row1 = 0
    x_row2 = 0
    x_row3 = 0
    x_col1 = 0
    x_col2 = 0
    x_col3 = 0
    x_diagonal = 0
    x_inv_diagonal = 0
    o_row1 = 0
    o_row2 = 0
    o_row3 = 0
    o_col1 = 0
    o_col2 = 0
    o_col3 = 0
    o_diagonal = 0
    o_inv_diagonal = 0
    """
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                x_pos.append((i, j))
            elif grid[i][j] == 'o':
                o_pos.append((i, j))

    for i in x_pos:
        if i[0] == i[1]:
            # x_diagonal += 1
            x_values[6] += 1
        if i[1] == 0:
            # x_col1 += 1
            x_values[3] += 1
        if i[1] == 1:
            # x_col2 += 1
            x_values[4] += 1
        if i[1] == 2:
            # x_col3 += 1
            x_values[5] += 1
        if i[0] == 0:
            # x_row1 += 1
            x_values[0] += 1
        if i[0] == 1:
            # x_row2 += 1
            x_values[1] += 1
        if i[0] == 2:
            # x_row3 += 1
            x_values[2] += 1
        if (i[1] == 1 and i[0] == 1) or (i[1] - i[0] == 2 or i[1] - i[0] == -2):
            # x_inv_diagonal += 1
            x_values[7] += 1

    for i in x_values:
        if i > 2:
            return 'x'

    for i in o_pos:
        if i[0] == i[1]:
            # x_diagonal += 1
            o_values[6] += 1
        if i[1] == 0:
            # x_col1 += 1
            o_values[3] += 1
        if i[1] == 1:
            # x_col2 += 1
            o_values[4] += 1
        if i[1] == 2:
            # x_col3 += 1
            o_values[5] += 1
        if i[0] == 0:
            # x_row1 += 1
            o_values[0] += 1
        if i[0] == 1:
            # x_row2 += 1
            o_values[1] += 1
        if i[0] == 2:
            # x_row3 += 1
            o_values[2] += 1
        if (i[1] == 1 and i[0] == 1) or (i[1] - i[0] == 2 or i[1] - i[0] == -2):
            # x_inv_diagonal += 1
            o_values[7] += 1

    for i in o_values:
        if i > 2:
            return 'o'

    return 'e'


def put(screen, grid, x_axis, y_axis, las, row, col):
    if grid[row][col] == 'e':
        if las == 'o':
            screen.blit(x, (x_axis, y_axis))
            grid[row][col] = 'x'
        else:
            screen.blit(o, (x_axis, y_axis))
            grid[row][col] = 'o'

    return las


def main():
    grid = []
    for i in range(3):
        col = []
        for j in range(3):
            col.append('e')
        grid.append(col)

    print(grid)

    pygame.init()
    screen = pygame.display.set_mode((480, 400))

    screen.fill(background_color)

    pygame.draw.line(screen, (0, 0, 0), (160, 0), (160, 380), 3)
    pygame.draw.line(screen, (0, 0, 0), (320, 0), (320, 380), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 120), (500, 120), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 240), (500, 240), 3)

    # x_won = None
    # y_won = None
    running = True
    last = 'o'
    count = 0

    while running:
        for event in pygame.event.get():
            if count > 8:
                running = False
            if count > 4:
                if check_who_won(grid) == 'x':
                    pygame.draw.rect(screen, match_over_background, pygame.Rect(0, 160, 480, 40))
                    font = pygame.font.SysFont('comicsans', 30)
                    text = font.render('X WON', False, match_over_color)
                    screen.blit(text, (175, 170))
                    """
                    count = 0
                    last = 'o'
                    x_won = True
                    main()
                    break
                    """
                    running = False
                elif check_who_won(grid) == 'o':
                    pygame.draw.rect(screen, match_over_background, pygame.Rect(0, 160, 480, 40))
                    font = pygame.font.SysFont('comicsans', 30)
                    text = font.render('O WON', False, match_over_color)
                    screen.blit(text, (175, 170))
                    """
                    count = 0
                    last = 'o'
                    y_won = True
                    main()
                    break
                    """
                    running = False
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < 160 and event.pos[1] < 120:
                    # screen.blit(x, (45, 30))
                    put(screen, grid, 45, 30, last, 0, 0)
                    if put(screen, grid, 45, 30, last, 0, 0) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 160 and event.pos[1] < 240:
                    # screen.blit(x, (45, 150))
                    put(screen, grid, 45, 150, last, 1, 0)
                    if put(screen, grid, 45, 150, last, 1, 0) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 160 and event.pos[1] < 360:
                    # screen.blit(x, (45, 270))
                    put(screen, grid, 45, 270, last, 2, 0)
                    if put(screen, grid, 45, 270, last, 2, 0) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 320 and event.pos[1] < 120:
                    # screen.blit(x, (205, 30))
                    put(screen, grid, 205, 30, last, 0, 1)
                    if put(screen, grid, 205, 30, last, 0, 1) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 320 and event.pos[1] < 240:
                    # screen.blit(x, (205, 150))
                    put(screen, grid, 205, 150, last, 1, 1)
                    if put(screen, grid, 205, 150, last, 1, 1) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 320 and event.pos[1] < 360:
                    # screen.blit(x, (205, 270))
                    put(screen, grid, 205, 270, last, 2, 1)
                    if put(screen, grid, 205, 270, last, 2, 1) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 480 and event.pos[1] < 120:
                    # screen.blit(x, (365, 30))
                    put(screen, grid, 365, 30, last, 0, 2)
                    if put(screen, grid, 365, 30, last, 0, 2) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 480 and event.pos[1] < 240:
                    # screen.blit(x, (365, 150))
                    put(screen, grid, 365, 150, last, 1, 2)
                    if put(screen, grid, 365, 150, last, 1, 2) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1
                elif event.pos[0] < 480 and event.pos[1] < 360:
                    # screen.blit(x, (365, 270))
                    put(screen, grid, 365, 270, last, 2, 2)
                    if put(screen, grid, 365, 270, last, 2, 2) == 'o':
                        last = 'x'
                    else:
                        last = 'o'
                    count += 1

        pygame.display.update()

    print(grid)
    return True


main()


def test():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((480, 400))
    screen.fill(background_color)
    """
    surface = pygame.Surface((480, 50))
    surface.set_alpha(330)
    surface.fill(background_color)
    screen.blit(surface, (0, 0))
    """
    pygame.draw.rect(screen, match_over_background, pygame.Rect(0, 160, 480, 40))
    font = pygame.font.SysFont('comicsans', 30)
    text = font.render('Match Over', False, match_over_color)
    screen.blit(text, (175, 170))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
        pygame.display.update()
