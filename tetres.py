import pygame
import time
import random

pygame.init()
pygame.mixer.init()

music = pygame.mixer.Sound('/home/michael/coding/python/tetres.wav')

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

def add_line(screen, text, x, y):
    # used to print the status of the variables
    text = font.render(text, True, (200, 200, 200))
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

font = pygame.font.Font("freesansbold.ttf", 32)

points = 0

blocks = []

pblocks = [[[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [120, 0, 120, 0]], [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [30, 60, 30, 60]], [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [30, 30, 30, 30]], [[0, 0, 0, 0], [30, 0, 30, 0], [0, 30, 0, 30], [30, 30, 30, 30]], [[0, 0, 0, 0]], [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [90, 30, 90, 30]]]

# cblocks = random.choice(pblocks)
cblocks = []


posx, posy = 0, 0

time1 = 0

mpoints = 0

o = 1

pygame.mixer.Sound.play(music)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

r = 0

# Run until the user asks to quit
running = True
while running:
    # Fill the background with white
    screen.fill((0, 0, 0))
    pygame.event.poll()
    keys = pygame.key.get_pressed()
    
    if r <= 1:
        pygame.mixer.Sound.play(music)
    
    if r > (points*10 + 30)*10.5:
        r = 0
    
    if keys[pygame.K_d]:
        if time1 % 15 == 0:
            for i in cblocks:
                i[0] += 30
    if keys[pygame.K_a]:
        if time1 % 15 == 0:
            for i in cblocks:
                i[0] -= 30
    if keys[pygame.K_s]:
        if time1 % 5 == 0:
            for i in cblocks:
                i[1] += 30
    
    r += 1
    
    if keys[pygame.K_e]:
        if time1 % 15 == 0:
            o += 1
            if o == 1:
                b = -1
                c = -1
            elif o == 2:
                b = 1
                c = 1
            elif o == 3:
                b = -1
                c = 1
            elif o == 4:
                b = 1
                c = -1
            for i in cblocks:
                u = cblocks[0]
                n = i[0] - u[0]
                m = i[1] - u[1]
                i[0] = m*b + u[0]
                i[1] = n*c + u[1]
    for i in blocks:
        if i[1] == 0:
            running = False
    
    if o > 4:
        o = 1
    
    time1 += 1
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not cblocks:
        y = random.choice(pblocks)
        for i in y:
            cblocks.append([i[0] + 300, i[1], i[0] + 300, i[1]])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    
    for i in cblocks:
        if time1 % 20 == 0:
            i[1] += 30
        if i[1] >= 600:
            for i in cblocks:
                i[0] = i[2]
                i[1] = i[3]
                blocks.append([i[0], i[1], color])
            cblocks = []
    
    pblocks = [[[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [120, 0, 120, 0]], [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [30, 60, 30, 60]], [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [30, 30, 30, 30]], [[0, 0, 0, 0], [30, 0, 30, 0], [0, 30, 0, 30], [30, 30, 30, 30]], [[0, 0, 0, 0]], [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [90, 30, 90, 30]]]
    
    j = False
    
    for i in cblocks:
        for j in blocks:
            if i[0] == j[0]:
                if i[1] == j[1]:
                    for i in cblocks:
                        i[0] = i[2]
                        i[1] = i[3]
                        blocks.append([i[0], i[1], color])
                    cblocks = []
    
    for i in range(20):
        h = []
        for j in blocks:
            if j[1] == i*30:
                h.append(j)
        
        if len(h) >= 10:
            for i in h:
                blocks.remove(i)
            for l in blocks:
                if l[1] < h[0][1]:
                    l[1] += 30
            points += 1
    
    for i in cblocks:
        if i[0] < 150:
            for i in cblocks:
                i[0] = i[2]
                i[1] = i[3]
        if i[0] > 420:
            for i in cblocks:
                i[0] = i[2]
                i[1] = i[3]
    for i in cblocks:
        map1 = pygame.Rect(i[0], i[1], 30, 30)
        pygame.draw.rect(screen, color, map1)
    for i in blocks:
        map1 = pygame.Rect(i[0], i[1], 30, 30)
        pygame.draw.rect(screen, i[2], map1)
    
    map1 = pygame.Rect(0, 0, 150, 600)
    pygame.draw.rect(screen, (128, 128, 128), map1)
    
    map1 = pygame.Rect(450, 0, 150, 600)
    pygame.draw.rect(screen, (128, 128, 128), map1)
    
    add_line(screen, f'points: {points + mpoints}', 0, 0)
    
    for i in cblocks:
        i[2] = i[0]
        i[3] = i[1]
    
    if points >= 5:
        add_line(screen, 'yay!', 200, 45)
        pygame.display.flip()
        time.sleep(2)
        cblocks = []
        blocks = []
        points = 0
        mpoints += 7
    
    time.sleep(1/(points*10 + 30))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

print(str(points + mpoints)  + ' points')