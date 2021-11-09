import pygame 
import os
import sys
import random
pygame.init()
def make_deck():
    cards = ['K','K','K','K','Q','Q','Q','Q','J','J','J','J','A','A','A','A',10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]
    p1 = []
    p2 = []
    p3 = []
    counter = 0
    while len(cards) > 0:
        if counter == 0:
            p1.append(cards[0])
            cards = cards[1:]
            counter += 1
        elif counter == 1:
            p2.append(cards[0])
            cards = cards[1:]
            counter += 1
        else:
            p3.append(cards[0])
            cards = cards[1:]
            counter = 0
    random.shuffle(p1)
    random.shuffle(p2)
    random.shuffle(p3)
    return p1,p2,p3
card_images = {
# have to put r so it can read it as a raw string
  "A": r"C:\Users\samus\Desktop\３－Way-War\A.png",
  "K": r"C:\Users\samus\Desktop\３－Way-War\K.png",
  "Q": r"C:\Users\samus\Desktop\３－Way-War\Q.png",
  "J": r"C:\Users\samus\Desktop\３－Way-War\J.png",
   10: r"C:\Users\samus\Desktop\３－Way-War\10.png",
    9: r"C:\Users\samus\Desktop\３－Way-War\9.png",
    8: r"C:\Users\samus\Desktop\３－Way-War\8.png",
    7: r"C:\Users\samus\Desktop\３－Way-War\7.png",
    6: r"C:\Users\samus\Desktop\３－Way-War\6.png",
    5: r"C:\Users\samus\Desktop\３－Way-War\5.png",
    4: r"C:\Users\samus\Desktop\３－Way-War\4.png",
    3: r"C:\Users\samus\Desktop\３－Way-War\3.png",
    2: r"C:\Users\samus\Desktop\３－Way-War\2.png",


}

# define the RGB value
background_color = (111, 81, 74)

# assigning values to X and Y variable
X = 1300
Y = 1000
  
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('WAR!')

# create a surface object, image is drawn on it.

hands = make_deck()
# game of war process

ranker = ['A','K','Q','J',10,9,8,7,6,5,4,3,2]
x, y = hands[0], hands[1]
# infinite loop
while True :
    display_surface.fill(background_color)
    table = [x[0],y[0]]
    x, y = x[1:], y[1:]

    image = pygame.image.load(card_images[table[0]])
    image2 = pygame.image.load(card_images[table[1]])
    image = pygame.transform.scale(image, (120, 200))
    image2 = pygame.transform.scale(image2, (120, 200))

    # rotate image 
    rotated_image = pygame.transform.rotate(image,270)
    image = rotated_image  
    rotated_image2 = pygame.transform.rotate(image2,270)
    image2 = rotated_image2
    # copying the image surface object
    # to the display surface object at
    display_surface.blit(image, (100, 400))
    display_surface.blit(image2, (950, 400))
    pygame.time.wait(1000)


    if ranker.index(table[0]) < ranker.index(table[1]):
        x.append(table[0])
        x.append(table[1])
    elif ranker.index(table[1]) < ranker.index(table[0]):
        y.append(table[0])
        y.append(table[1])
    elif ranker.index(table[1]) == ranker.index(table[0]): 
        pot = [table[1], table[0]]
        while table[0] == table[1]:
            add = [x[0],x[1],x[2],y[0],y[1],y[2]]
            pot.extend(add)
            x, y = x[3:], y[3:]
            table = [x[0],y[0]]
            x, y = x[1:], y[1:]
        if ranker.index(table[0]) < ranker.index(table[1]):
            pot.append(table[0])
            pot.append(table[1])
            x.extend(pot)
        elif ranker.index(table[1]) < ranker.index(table[0]):
            pot.append(table[0])
            pot.append(table[1])
            y.extend(pot)
    print(x,y)
    if len(x) == 0 or len(y) == 0:
        pygame.time.wait(1000)

            # deactivates the pygame library
        pygame.quit()
  
            # quit the program.
        quit()
  
        # Draws the surface object to the screen.  
    pygame.display.update() 
