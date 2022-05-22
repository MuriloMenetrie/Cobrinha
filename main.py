#importação de bibliotecas usadas
import pygame
import random
 
pygame.init()
 
#Defição de cores usadas 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (219, 24, 86, 56)
green = (0, 255, 0)
blue = (50, 153, 213)
grey = (235, 225, 235, 92)

#Largura e Altura do Display 
dis_width = 600
dis_height = 400 
dis = pygame.display.set_mode((dis_width, dis_height))

#titulo
pygame.display.set_caption('Jogo da Cobrinha')
 
clock = pygame.time.Clock()

#Tamanho e velocidade da Cobrinha 
snake_block = 10
snake_speed = 12

#Configurações das Fontes de texto 
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 15)
 
#Configurações do placar de pontuação 
def Your_score(score):
    value = score_font.render("Sua pontuação: " + str(score), True, black)
    dis.blit(value, [5, 5])
 
 
#Configurações da Cobrinha 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
#Configurações das mensagens 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [235,150])

def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [50,200]) 

#Configurações do jogo 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:

        #Configurações do menu de derrota  
        while game_close == True:
            dis.fill(red)
            message("Você perdeu!", white)
            message1("Pressione C para Jogar de novo ou Q para Sair", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #Definições da movimentação da Cobrinha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #Limites do mapa e da Cobrinha
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(grey)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()

        #Randomização da comidinha NHAM! 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()