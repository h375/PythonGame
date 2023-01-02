import pygame
import os
import random
from game import Player
from game import Enemy
from game import Banana
from game import Fireball

WIDTH,HEIGHT = 800,600

monkeyImg = pygame.image.load(os.path.join('Images', 'monkey.png'))
monkey= pygame.transform.rotate(pygame.transform.scale(monkeyImg, (100, 100)), 0)

bananaImg = pygame.image.load(os.path.join('Images', 'banana.png'))
banana = pygame.transform.rotate(pygame.transform.scale(bananaImg, (50, 50)), 0)

spaceshipImg = pygame.image.load(os.path.join('Images', 'spaceship.png'))
spaceship = pygame.transform.rotate(pygame.transform.scale(spaceshipImg, (90, 90)), 90)

fireballImg = pygame.image.load(os.path.join('Images', 'fireball.png'))
fireball = pygame.transform.rotate(pygame.transform.scale(fireballImg, (30, 30)), 0)

background_colour = (0,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
screen.fill(background_colour)
screen.blit(monkey,(0,200))
# screen.blit(spaceship,(700,200))
pygame.display.update()

def releaseEnemies():
    enemy = Enemy(700,random.randint(0, 520))
    enemy.moveLeft()
    screen.blit(spaceship,(enemy.x,enemy.y))
    fireballs = Fireball(enemy.x,enemy.y)  
    fireballs.shoot()
    screen.blit(fireball,(fireballs.x,fireballs.y))
    pygame.display.update()



def main():

    player = Player(0,200)

    clock = pygame.time.Clock()
    start = True

    enemy = Enemy(700,random.randint(0, 520))
    enemy.moveLeft()
    screen.blit(spaceship,(enemy.x,enemy.y))
    fireballs = Fireball(enemy.x,enemy.y)  
    fireballs.shoot()
    screen.blit(fireball,(fireballs.x,fireballs.y))
    pygame.display.update()

    while start:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space key was pressed")

                    
                    # print(random.randint(0, 520))

                    # enemy = Enemy(700,random.randint(0, 520))
                    # enemy.moveLeft()
                    # screen.blit(spaceship,(enemy.x,enemy.y))
                    # fireballs = Fireball(enemy.x,enemy.y)  
                    # fireballs.shoot()
                    # screen.blit(fireball,(fireballs.x,fireballs.y))
                    # pygame.display.update()

                if event.key == pygame.K_UP:
                   
                    # if X_player > 1:
                    print("pressed up")
                    # X_player-=20
                    player.moveUp()
                    screen.fill(background_colour)    
                    screen.blit(monkey,(player.x,player.y))
              
                if event.key == pygame.K_DOWN:
                    
                    # if X_player < 500:
                    print("pressed down")
                    # X_player+=20
                    player.moveDown()
                    screen.fill(background_colour)    
                    screen.blit(monkey,(player.x,player.y))

                if event.key == pygame.K_RIGHT:

                    
                    print("pressed right")

                    # for i in range(len(player.bananas)):
                    #     if player.bananas[i].x >= 810:
                    #         print("over")
                    #         player.bananas.remove(player.bananas[i])
                    
                    player.bananas.append(Banana())


        for i in range(len(player.bananas)):
        
            screen.fill(background_colour)    
            screen.blit(monkey,(player.x,player.y))
            # enemy.moveLeft()
            # screen.blit(spaceship,(enemy.x,enemy.y))

            player.bananas[i].shoot()
            #print(i, player.bananas[i].x)
            screen.blit(banana,(player.bananas[i].x,player.y))

            #screen.blit(fireball,(fireballs.x,fireballs.y))
            pygame.display.update()

            if player.bananas[i].x >= 810:
                print("over")
                player.bananas.remove(player.bananas[i])
                break

        
        pygame.display.update()
        
        
        


if __name__ == "__main__":
    main()