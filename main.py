import pygame

pygame.init()

def copyList(list):
    newList = []
    for item in list:
        newList.append(item)
    return newList

grid = []

for i in range(50):
    grid.append([])
    for j in range(30):
        grid[i].append(0)
    
class Thing:

    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.selected = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x*20, self.y*20, self.width*20, self.height*20))
        text = pygame.font.Font("freesansbold.ttf", 10).render(self.name, True, (100, 200, 255))
        screen.blit(text, (self.x*20, self.y*20))

    def contained(self, x, y):
        if x >= self.x*20 and x < self.x*20 + self.width*20 and y >= self.y*20 and y < self.y*20 + self.height*20:
            return True
        return False

def drawBackground(screen):
    for i in range(50):
        for j in range(30):
            pygame.draw.rect(screen, (0, 0, 0), (i*20, j*20, 20, 20))
            if grid[i][j] == 1:
                pygame.draw.rect(screen, (255, 200, 100), (i*20+1, j*20+1, 19.8, 19.8))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i*20+1, j*20+1, 19.8, 19.8))
            


screen = pygame.display.set_mode((1000, 600))

objects = []

sink = Thing(0, 0, 1, 2, "Sink")
stove = Thing(0, 2, 1, 2, "Stove")
oven = Thing(0, 4, 1, 2, "Oven")
window = Thing(0, 6, 1, 4, "Window")
dishwasher = Thing(0, 10, 2, 2, "Dishwasher")
pantry1 = Thing(0, 12, 1, 2, "Pantry")
pantry2 = Thing(1, 12, 1, 2, "Pantry")
bigPantry = Thing(0, 14, 4, 5, "Big Pantry")
bigFridge1 = Thing(0, 19, 10, 5, "Big Fridge")
bigFridge2 = Thing(10, 19, 10, 5, "Big Fridge")
miniFridge = Thing(0, 24, 1, 2, "Mini Fridge")
grill = Thing(0, 26, 2, 1, "Grill")
fryer = Thing(2, 26, 2, 1, "Fryer")


objects.append(sink)
objects.append(stove)
objects.append(oven)
objects.append(window)
objects.append(dishwasher)
objects.append(pantry1)
objects.append(pantry2)
objects.append(bigPantry)
objects.append(bigFridge1)
objects.append(bigFridge2)
objects.append(miniFridge)
objects.append(grill)
objects.append(fryer)




gameOver = False
clicked = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameOver = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not clicked:
                clicked = True
                for object in objects:
                    if object.contained(event.pos[0], event.pos[1]):
                        object.selected = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
            found = False
            for object in objects:
                if object.selected:
                    found = True
                    object.selected = False
            
            if not found:
                if grid[event.pos[0]//20][event.pos[1]//20] == 1:
                    grid[event.pos[0]//20][event.pos[1]//20] = 0
                grid[event.pos[0]//20][event.pos[1]//20] = 1

    drawBackground(screen)

    for object in objects:
        if object.selected:
            object.x = event.pos[0]//20
            object.y = event.pos[1]//20
        object.draw(screen)
        

    pygame.display.update()
    
