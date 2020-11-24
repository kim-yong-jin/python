import pygame
import sys
import random
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()
flag_ing = True
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)

b1 = (255, 0, 0)
b2 = (245, 0, 0)
b3 = (235, 0, 0)
b4 = (225, 0, 0)
b5 = (215, 0, 0)
b6 = (205, 0, 0)
b7 = (195, 0, 0)
s1 = (0, 0, 255)
s2 = (0, 0, 245)
s3 = (0, 0, 235)
s4 = (0, 0, 225)
s5 = (0, 0, 215)
s6 = (0, 0, 205)
s7 = (0, 0, 195)




pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

mission_cnt = 2


block2D =[ 
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
]
stack2D =[ 
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0]
]
print2D =[ 
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
]

class Block:
    def __init__(self):
        self.kind = 1 #random.randrange(1,8)
        self.status = 0
        self.i = 2
        self.j = 4
        
    def __str__(self):
        return "kind:{},status:{},i:{},j:{}".format(self.kind,self.status,self.i,self.j);    
        
block =  Block()       

def show2D(p2D):
    print("=========================================================")
    for i in p2D :
        print(i)
        
def setBlock2DByBlock():  
    for i in range(23):
        for j in range(10):
            print2D[i][j]=0;
            block2D[i][j]=0;
            
    if block.kind == 1 :
        block2D[block.i  ][block.j  ] = block.kind
        block2D[block.i  ][block.j+1] = block.kind
        block2D[block.i+1][block.j  ] = block.kind
        block2D[block.i+1][block.j+1] = block.kind    
        
    if(block.kind == 2):
        block2D[block.i  ][block.j  ] = block.kind
        if(block.status == 0):
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i+1][block.j-1] = block.kind
        elif(block.status == 1):
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i+1][block.j+1] = block.kind
            
    if(block.kind == 3): 
        block2D[block.i  ][block.j  ] = block.kind
        if(block.status == 0):
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i+1][block.j+1] = block.kind
        elif(block.status == 1): 
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i+1][block.j-1] = block.kind
    
    if(block.kind == 4): 
        block2D[block.i  ][block.j  ] = block.kind
        if(block.status == 0): 
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i  ][block.j-2] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
        elif(block.status == 1): 
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i-2][block.j  ] = block.kind
    
    if(block.kind == 5): 
        block2D[block.i][block.j] = block.kind
        if(block.status == 0): 
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i  ][block.j-1] = block.kind
        elif(block.status == 1):
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
        elif(block.status == 2): 
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i  ][block.j-1] = block.kind
        elif(block.status == 3): 
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i  ][block.j-1] = block.kind
    
    
    if(block.kind == 6): 
        block2D[block.i][block.j] = block.kind
        if(block.status == 0): 
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i-1][block.j-1] = block.kind
        elif(block.status == 1): 
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i-1][block.j+1] = block.kind
        elif(block.status == 2): 
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i+1][block.j+1] = block.kind
        elif(block.status == 3): 
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i+1][block.j-1] = block.kind
    
    if(block.kind == 7) : 
        block2D[block.i][block.j] = block.kind
        if(block.status == 0): 
            block2D[block.i-1][block.j+1] = block.kind
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
        elif(block.status == 1): 
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i+1][block.j+1] = block.kind
        elif(block.status == 2): 
            block2D[block.i-1][block.j  ] = block.kind
            block2D[block.i+1][block.j  ] = block.kind
            block2D[block.i+1][block.j-1] = block.kind
        elif(block.status == 3): 
            block2D[block.i  ][block.j-1] = block.kind
            block2D[block.i  ][block.j+1] = block.kind
            block2D[block.i-1][block.j-1] = block.kind  
            
def setPrint2DByBlockStack():  
    for i in range(23):
        for j in range(10):
            if(stack2D[i][j] > 0):
                print2D[i][j] = stack2D[i][j];
            if(block2D[i][j] > 0):
                print2D[i][j] = block2D[i][j];
                
                
def changeStatus():           
    if(block.kind == 1):
        pass
    
    if(block.kind == 2 or block.kind == 3 or block.kind == 4):
        if(block.status == 0):
            block.status = 1
        elif(block.status == 1):
            block.status = 0
   
    
    if(block.kind == 5 or block.kind == 6 or block.kind == 7):
        if(block.status == 0):
            block.status = 1
        elif(block.status == 1):
            block.status = 2
        elif(block.status == 2):
            block.status = 3
        elif(block.status == 3):
            block.status = 0

def isCrash():
    for i in range(23):
        for j in range(10): 
            if(block2D[i][j]>0 and stack2D[i][j]>0):
                return True
    return False 
            
def moveBlock2Stack():
    for i in range(23):
        for j in range(10): 
            if(block2D[i][j]>0 ):
                stack2D[i][j] = block2D[i][j]+10;

def remove10(): 
    arrTemp = [];
    cnt10 = 0;
    for i in range(23):
        if(    stack2D[i][0]>0 and
                stack2D[i][1]>0 and
                stack2D[i][2]>0 and
                stack2D[i][3]>0 and
                stack2D[i][4]>0 and
                
                stack2D[i][5]>0 and
                stack2D[i][6]>0 and
                stack2D[i][7]>0 and
                stack2D[i][8]>0 and
                stack2D[i][9]>0):
            cnt10+=1
        else :
            arrTemp.append(str(stack2D[i][0])+","+str(stack2D[i][1])+","+str(stack2D[i][2])+","+str(stack2D[i][3])+","+str(stack2D[i][4])+","+
                           str(stack2D[i][5])+","+str(stack2D[i][6])+","+str(stack2D[i][7])+","+str(stack2D[i][8])+","+str(stack2D[i][9])       );
            
    for i in range(cnt10):        
        arrTemp.insert(0,"0,0,0,0,0,0,0,0,0,0");

    for i in range(23):
        str_line = arrTemp[i];
        arr_line = str_line.split(",");
        stack2D[i][0]=int(arr_line[0]);
        stack2D[i][1]=int(arr_line[1]);
        stack2D[i][2]=int(arr_line[2]);
        stack2D[i][3]=int(arr_line[3]);
        stack2D[i][4]=int(arr_line[4]);
        
        stack2D[i][5]=int(arr_line[5]);
        stack2D[i][6]=int(arr_line[6]);
        stack2D[i][7]=int(arr_line[7]);
        stack2D[i][8]=int(arr_line[8]);
        stack2D[i][9]=int(arr_line[9]);
 
    
    return cnt10;
    
def changeFormRandom() :
    num = random.randrange(1,8)
    block.kind = num
            
def myrender(): 
    screen.fill(gray) 
    for i in range(23):
        for j in range(10):
            if (print2D[i][j] == 0) : pygame.draw.rect(screen, white, [j*20,i*20,19,19])
            
            if (print2D[i][j] == 1) : pygame.draw.rect(screen, b1, [j*20,i*20,19,19])
            if (print2D[i][j] == 2) : pygame.draw.rect(screen, b2, [j*20,i*20,19,19])
            if (print2D[i][j] == 3) : pygame.draw.rect(screen, b3, [j*20,i*20,19,19])
            if (print2D[i][j] == 4) : pygame.draw.rect(screen, b4, [j*20,i*20,19,19])
            if (print2D[i][j] == 5) : pygame.draw.rect(screen, b5, [j*20,i*20,19,19])
            if (print2D[i][j] == 6) : pygame.draw.rect(screen, b6, [j*20,i*20,19,19])
            if (print2D[i][j] == 7) : pygame.draw.rect(screen, b7, [j*20,i*20,19,19])

            if (print2D[i][j] == 11) : pygame.draw.rect(screen, s1, [j*20,i*20,19,19])
            if (print2D[i][j] == 12) : pygame.draw.rect(screen, s2, [j*20,i*20,19,19])
            if (print2D[i][j] == 13) : pygame.draw.rect(screen, s3, [j*20,i*20,19,19])
            if (print2D[i][j] == 14) : pygame.draw.rect(screen, s4, [j*20,i*20,19,19])
            if (print2D[i][j] == 15) : pygame.draw.rect(screen, s5, [j*20,i*20,19,19])
            if (print2D[i][j] == 16) : pygame.draw.rect(screen, s6, [j*20,i*20,19,19])
            if (print2D[i][j] == 17) : pygame.draw.rect(screen, s7, [j*20,i*20,19,19])      
            
    font = pygame.font.Font('CONSOLA.ttf',30)  
    text = font.render("Count {}".format(mission_cnt),True,(28,0,0))  
    screen.blit(text,(200,0))         
    pygame.display.update()

clock = pygame.time.Clock()
while True:
    clock.tick(10)
    if not flag_ing :
        break; 
    flag_render = False
    
    flagDown        = False;
    pre_i           = block.i;
    pre_j           = block.j;
    pre_status      = block.status;
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT] and key_event[pygame.K_DOWN] :
        continue
    
    if key_event[pygame.K_RIGHT] and key_event[pygame.K_DOWN] :
        continue
    
    if key_event[pygame.K_LEFT]:
        block.j-=1
        flag_render = True

    if key_event[pygame.K_RIGHT]:
        block.j+=1
        flag_render = True

    if key_event[pygame.K_UP]:
        changeStatus();
        flag_render = True

    if key_event[pygame.K_DOWN]:
        block.i+=1
        flagDown = True
        flag_render = True

    if key_event[pygame.K_d]:
        show2D(block2D) 
        show2D(print2D) 
        print(block)         

        
    if flag_render :
        
        flagOut = False
        try:
            block.j -= 10
            setBlock2DByBlock()
            block.j += 10
            setBlock2DByBlock()
        except:
            flagOut = True
            print("너나갔어")
            
        flagCrash = isCrash()
        
        if(flagOut or flagCrash):
            block.i         =pre_i;
            block.j         =pre_j;
            block.status    =pre_status;
            setBlock2DByBlock();
            if(flagDown):
                moveBlock2Stack()
                
                if(     stack2D[5][0]>0 or
                        stack2D[5][1]>0 or
                        stack2D[5][2]>0 or
                        stack2D[5][3]>0 or
                        stack2D[5][4]>0 or
                        stack2D[5][5]>0 or
                        stack2D[5][6]>0 or
                        stack2D[5][7]>0 or
                        stack2D[5][8]>0 or
                        stack2D[5][9]>0):
                    messagebox.showinfo("You Lose", "You Lose")
                    flag_ing = False;
            
                cnt10 = remove10()
                if(cnt10>0):
                    mission_cnt -= cnt10;
                    if(mission_cnt<=0):
                        messagebox.showinfo("You Win", "You Win")
                        
                        flag_ing = False
                
                changeFormRandom()
                block.status = 0;
                block.i = 2;
                block.j = 4;
                setBlock2DByBlock();
            
        
        setPrint2DByBlockStack()
        myrender()
        
        
        show2D(block2D) 
        show2D(print2D) 
        print(block)  
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    