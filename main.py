import pygame
import os
import random
import math
import sys
import neat

# from dinosaur import Dinosaur,AI_Dino

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
        pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

global high_score

high_score = 0

# class Dinosaur:
#     X_POS = 0
#     Y_POS = 310
#     Y_POS_DUCK = 340
#     JUMP_VEL = 8.5

#     def __init__(self):
#         self.duck_img = DUCKING
#         self.run_img = RUNNING
#         self.jump_img = JUMPING

#         self.dino_duck = False
#         self.dino_run = True
#         self.dino_jump = False

#         self.step_index = 0
#         self.jump_vel = self.JUMP_VEL
#         self.image = self.run_img[0]
#         self.dino_rect = self.image.get_rect()
#         self.dino_rect.x = self.X_POS
#         self.dino_rect.y = self.Y_POS
#         self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#     def update(self,userInput):
#         if self.dino_duck:
#             self.duck()
#         if self.dino_run:
#             self.run()
#         if self.dino_jump:
#             self.jump()
        
#         if self.step_index >= 10:
#             self.step_index = 0
        
#         if not AI_player:
#             if userInput[pygame.K_UP] and not self.dino_jump:
#                 self.dino_duck = False
#                 self.dino_run = False
#                 self.dino_jump = True
#             elif userInput[pygame.K_DOWN] and not self.dino_jump:
#                 self.dino_duck = True
#                 self.dino_run = False
#                 self.dino_jump = False
#             elif not (self.dino_jump or userInput[pygame.K_DOWN]):
#                 self.dino_duck = False
#                 self.dino_run = True
#                 self.dino_jump = False
        
#     def duck(self):
#         self.image = self.duck_img[self.step_index // 5] 
#         self.dino_rect = self.image.get_rect()
#         self.dino_rect.x = self.X_POS
#         self.dino_rect.y = self.Y_POS_DUCK
#         self.step_index += 1
    
#     def run(self):
#         self.image = self.run_img[self.step_index // 5] 
#         self.dino_rect = self.image.get_rect()
#         self.dino_rect.x = self.X_POS
#         self.dino_rect.y = self.Y_POS
#         self.step_index += 1
    
#     def jump(self): 
#         self.image = self.jump_img
#         if self.dino_jump:
#             self.dino_rect.y -= self.jump_vel * 4
#             self.jump_vel -= 1
#         if self.jump_vel <= - self.JUMP_VEL:
#             self.dino_jump = False
#             self.dino_run = True
#             self.jump_vel = self.JUMP_VEL

#     def draw(self, SCREEN):
#         SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
#         pygame.draw.rect(SCREEN, self.color, (self.dino_rect.x, self.dino_rect.y, self.dino_rect.width, self.dino_rect.height), 2)
#         for obstacle in obstacles:
#             pygame.draw.line(SCREEN, self.color, (self.dino_rect.x + 54, self.dino_rect.y + 12), obstacle.rect.center, 2)

class Dinosaur:
    X_POS = 0
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self,userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        
        if self.step_index >= 10:
            self.step_index = 0
                
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
        
    def duck(self):
        self.image = self.duck_img[self.step_index // 5] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
    
    def run(self):
        self.image = self.run_img[self.step_index // 5] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
    
    def jump(self): 
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= - self.JUMP_VEL:
            self.dino_jump = False            
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))



class AI_Dino:
    X_POS = 0
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 9

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    
    def update(self):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL


    def duck(self):
        self.image = self.duck_img[self.step_index // 5] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1


    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        pygame.draw.rect(SCREEN, self.color, (self.dino_rect.x, self.dino_rect.y, self.dino_rect.width, self.dino_rect.height), 2)
        for obstacle in obstacles:
                pygame.draw.line(SCREEN, self.color, (self.dino_rect.x + 54, self.dino_rect.y + 12), obstacle.rect.center, 2)
        




class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
    
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

def remove(index):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)

def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes,config):
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles,dinosaurs,ge,nets
    run = True
    clock = pygame.time.Clock()
    points = 0

    dinosaurs = []
    ge =[]
    nets = []
    obstacles = []
    
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    
    death_count = 0

    for genome_id, genome in genomes:
        dinosaurs.append(AI_Dino())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0
    
    def score():       
        global points, game_speed
        points += 5
        if (points % 100 == 0) and (game_speed < 48):
            game_speed += 2       
       
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
        for g in ge:
            g.fitness += 2


    def statistics():
        global dinosaurs, game_speed, ge
        text_1 = font.render(f'Dinosaurs Alive:  {str(len(dinosaurs))}', True, (0, 0, 0))
        text_2 = font.render(f'Generation:  {pop.generation+1}', True, (0, 0, 0))
        text_3 = font.render(f'Game Speed:  {str(game_speed)}', True, (0, 0, 0))

        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50, 480))
        SCREEN.blit(text_3, (50, 510))


    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        SCREEN.fill((255, 255, 255))

        if len(obstacles) == 0:
            rand_int = random.randint(0, 2)
            if rand_int == 0: 
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif rand_int == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif rand_int == 2:
                obstacles.append(Bird(BIRD))


        if not AI_player:
            userInput = pygame.key.get_pressed()
            for dinosaur in dinosaurs:
                dinosaur.draw(SCREEN)
                dinosaur.update(userInput)
        else:            
            for dinosaur in dinosaurs:
                dinosaur.draw(SCREEN)
                dinosaur.update()

        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            for i,dinosaur in enumerate(dinosaurs):
                if dinosaur.dino_rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    remove(i)
                    # nets.pop(i)
                    # ge.pop(i)

        if AI_player:
            for i, dinosaur in enumerate(dinosaurs):
                output = nets[i].activate((dinosaur.dino_rect.y,distance((dinosaur.dino_rect.x, dinosaur.dino_rect.y), obstacle.rect.midtop),obstacle.type))
                if output[0] > 0.5 and dinosaur.dino_rect.y == dinosaur.Y_POS:
                    dinosaur.dino_jump = True
                    dinosaur.dino_run = False
                    dinosaur.dino_duck = False
                elif output[1] > 0.5 and dinosaur.dino_rect.y == dinosaur.Y_POS:
                    dinosaur.dino_jump = False
                    dinosaur.dino_run = False
                    dinosaur.dino_duck = True
            
            if len(dinosaurs) == 0:
                break


        if len(dinosaurs) == 0 and not AI_player:
            game_speed = 0                
            death_count += 1
            menu(death_count)
            run = False

        background()
        statistics()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points,high_score,AI_player
    run = True
    AI_player = False
    
    def run(config_path):
        global pop
        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path
        )

        pop = neat.Population(config = config)
        pop.run(eval_genomes,100)

        



    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            if points > high_score:
                high_score = points
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()            
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            scorehigh = font.render("Your High Score: " + str(high_score), True, (0, 0, 0))
            scoreHighRect = scorehigh.get_rect()
            scoreHighRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(scorehigh, scoreHighRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                AI_player = True                
                if __name__ == '__main__':
                    local_dir = os.path.dirname(__file__)
                    config_path = os.path.join(local_dir,'config.txt')
                    run(config_path)
                run = False
                
                


menu(death_count=0)


