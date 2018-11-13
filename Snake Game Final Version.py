import pygame, random, sys
from pygame.locals import *
import winsound
import time


print("\n")
print("This is very simple game. Press the up, down, left, or right arrows to make the snake eat the food. If you hit the edge of the screen or eat yourself , the game will end!")
print("\n")
user_input= input("Do you understand how the game works? Type yes to proceed: ")
print("\n")

if user_input.lower() == "yes":
    print("Game will start in 10 seconds! Get ready!!")
  

timer=int(10)
while (timer != 0 ):
    timer=timer-1
    time.sleep(1)
    print(str(timer) + " seconds left!")

      
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False
def die(screen, score):
	f=pygame.font.SysFont('Times New Roman', 30);t=f.render('Your amazing score was: '+str(score) + "!!!!", True, (255, 255, 255))
	winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
	screen.blit(t, (10, 270))
	pygame.display.update()
	pygame.time.wait(2000)
xs = [290, 290, 290, 290, 290];ys = [290, 270, 250, 230, 210];dirs = 0;score = 0;applepos = (random.randint(0, 590), random.randint(0, 590))
pygame.init();s=pygame.display.set_mode((600, 600));pygame.display.set_caption('Snake')
Food = pygame.Surface((20,20));Food.fill((0, 0, 238))
Snake = pygame.Surface((40, 40));Snake.fill((255,255,0))
f = pygame.font.SysFont('Times New Roman', 20);clock = pygame.time.Clock()
while True:
	clock.tick(10)
	for e in pygame.event.get():
		if e.type == QUIT:
			sys.exit(0)
		elif e.type == KEYDOWN:
			if e.key == K_UP and dirs != 0:dirs = 2
			elif e.key == K_DOWN and dirs != 2:dirs = 0
			elif e.key == K_LEFT and dirs != 1:dirs = 3
			elif e.key == K_RIGHT and dirs != 3:dirs = 1
	i = len(xs)-1
	while i >= 2:
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
			die(s, score)
			break
		i-= 1
	if collide(xs[0], applepos[0], ys[0], applepos[1], 40, 20, 40, 20):
		score+=1;xs.append(700);ys.append(700);applepos=(random.randint(0,590),random.randint(0,590))
	if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: die(s, score);break
	i = len(xs)-1
	while i >= 1:
		xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
	if dirs==0:ys[0] += 20
	elif dirs==1:xs[0] += 20
	elif dirs==2:ys[0] -= 20
	elif dirs==3:xs[0] -= 20	
	s.fill((0,0,0))	
	for i in range(0, len(xs)):
		s.blit(Snake, (xs[i], ys[i]))
	s.blit(Food, applepos);t=f.render(str(score), True, (255, 255, 0));s.blit(t, (10, 10))
	pygame.display.update()
					
					
		

