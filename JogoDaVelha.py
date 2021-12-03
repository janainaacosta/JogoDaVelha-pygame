import pygame
import sys

pygame.init()
pygame.display.set_caption('Jogo da Velha')   
icon = pygame.image.load('velha.png')
pygame.display.set_icon(icon)

size = width, height = 600, 600
screen = pygame.display.set_mode(size)

azul_grade = 0, 191, 255
azul_tela = 245, 255, 250
amarelo = 173,255,47
laranja = 255, 69, 0

screen.fill(azul_tela)

xis = pygame.image.load('xis.png')
xis = pygame.transform.scale(xis, (100, 100))
bola = pygame.image.load('bola.png')
bola = pygame.transform.scale(bola, (100, 100))

vez_de = 'X'
jogada = 0
parar = ''

# Matriz para verificação de espaços preencidos
matriz = [['_','_','_'],
          ['_','_','_'],
          ['_','_','_']]

quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

def tabuleiro(gray):
    pygame.draw.line(screen, azul_grade, (200, 25), (200, 575), 5) 
    pygame.draw.line(screen, azul_grade, (400, 25), (400, 575), 5)
    pygame.draw.line(screen, azul_grade, (25, 200), (575, 200), 5) 
    pygame.draw.line(screen, azul_grade, (25, 400), (575, 400), 5)
    pygame.draw.line(screen, laranja, (20, 20), (20, 580), 10)   # esquerda
    pygame.draw.line(screen, laranja, (580, 20), (16, 20), 10)   # topo
    pygame.draw.line(screen, laranja, (580, 16), (580, 580), 10) # direita
    pygame.draw.line(screen, laranja, (16, 580), (585, 580), 10) # embaixo 

     
   
# Função que marca as jogadas de 'X'
def xisinho(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if matriz [index_linha][index_coluna] == '_':
        screen.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        matriz [index_linha][index_coluna] = 'X'
        
        return True
    else:
        return False


# Função que marca as jogadas de 'O'
def bolinha(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if matriz [index_linha][index_coluna] == '_':
        screen.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        matriz [index_linha][index_coluna] = 'O'
        
        return True
    else:
        return False

    

def juiz():
#------------------------------ X I S I N H O ------------------------------    
    vencedor = ''
    #CHECK LINHA
    if matriz[0][0] == matriz[1][0] == matriz[2][0] == 'X': 
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (20, 100), (580, 100),  10) 
        vencedor =  'X'

    elif matriz[0][1] == matriz[1][1] == matriz[2][1] == 'X':
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (20, 300), (580, 300),  10) 
        vencedor =  'X'

    elif matriz[0][2] == matriz[1][2] == matriz[2][2] == 'X' :
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (20, 500), (580, 500),  10) 
        vencedor =  'X'
  
    #CHECK COLUNA
    if matriz[0][0] == matriz[0][1] == matriz[0][2] == 'X':  
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (100, 20), (100, 580),  10) 
        vencedor =  'X'
        
    elif matriz[1][0] == matriz[1][1] == matriz[1][2] == 'X':
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (300, 20), (300, 580),  10) 
        vencedor =  'X'
        
    elif matriz[2][0] == matriz[2][1] == matriz[2][2] == 'X':
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (500, 20), (500, 580),  10) 
        vencedor =  'X'
        

    #CHECK DIAGONAL
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] == 'X': 
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (20, 20), (580, 580),  10) 
        vencedor =  'X'
        
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == 'X':
        print('Vitória de X!!')
        pygame.draw.line(screen, amarelo, (580, 20), (20, 580),  10)  
        vencedor =  'X'

#------------------------------ B O L I N H A ------------------------------
    # CHECK COLUNA
    elif matriz[0][0] == matriz[0][1] == matriz[0][2] == 'O':  
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (100, 20), (100, 580),  10) 
        vencedor =  'O'
        
    elif matriz[1][0] == matriz[1][1] == matriz[1][2] == 'O':
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (300, 20), (300, 580),  10) 
        vencedor =  'O'
        
    elif matriz[2][0] == matriz[2][1] == matriz[2][2] == 'O':
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (500, 20), (500, 580),  10) 
        vencedor =  'O'
        
    #CHECK LINHA
    elif matriz[1][0] == matriz[1][1] == matriz[1][2] == 'O': 
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (100, 20), (100, 580),  10) 
        vencedor =  'O'

    elif matriz[0][1] == matriz[1][1] == matriz[2][1] == 'O':
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (20, 300), (580, 300),  10) 
        vencedor =  'O'

    elif matriz[2][0] == matriz[2][1] == matriz[2][2] == 'O' :
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (500, 20), (500, 580),  10) 
        vencedor =  'O'

    #CHECK DIAGONAL
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] == 'O':
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (20, 20), (580, 580),  10)  
        vencedor =  'O'
        
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == 'O':
        print('Vitória de O!!')
        pygame.draw.line(screen, amarelo, (580, 20), (20, 580),  10)  
        vencedor =  'O'
        
    return vencedor



while True:
    tabuleiro(azul_tela)
    
    if jogada >= 9:
        screen.fill(azul_grade)
        print('velha')
        print(matriz)
        break
    
    #verifica eventos na janela do jogo
    for event in pygame.event.get():
        #Se for pressionado o fechar da janela do jogo é encerrado
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            # Alternação entre as jogadas de 'X' e 'O'
            if vez_de == "X":
                if xisinho(click_pos):
                    jogada = jogada + 1
                    parar = juiz()
                    vez_de = "O"

            elif vez_de == "O":
                if bolinha(click_pos):
                    jogada = jogada + 1
                    parar = juiz()
                    vez_de = "X"
                    
            print('Jogada:',jogada)
            
    pygame.display.update()

    if parar == 'X' or parar == 'O':
        break

            

