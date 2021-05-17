import random
def Block_Check(x,y):
    for i in list_block_points:
        if(x==i.split(",")[0] and y==i.split(",")[1]):
            return False

    return True
def front_left(x,y):
    return x-2,y-1

def front_right(x,y):
    return x-2,y+1

def back_left(x,y):
    return x+2,y-1

def back_right(x,y):
    return x+2,y+1 

def left_right(x,y):
    return x-1,y-2

def left_left(x,y):
    return x+1,y-2

def right_left(x,y):
    return x-1,y+2

def right_right(x,y):
    return x+1,y+2 

def front_left_bishop(x,y):
    return x-1,y-1

def front_right_bishop(x,y):
    return x-1,y+1
def back_left_bishop(x,y):
    return x+1,y-1
def back_right_bishop(x,y):
    return x+1,y+1            


def Get_all_Bishop_Possible_Moves(x_bishop,y_bishop):
    moves=list()
    for i in bishop_move:
        flag=True
        x,y=x_bishop,y_bishop
        while flag:
            x,y=i(x,y)
            if x<=7 and y<=7 and x>=0 and y>=0:
                if str(x)+","+str(y) not in list_block_points:
                    moves.append(str(x)+","+str(y))
                else:
                    break         
            else:
                flag=False     
    return moves            

def Get_Bishop_Possible_Moves(x_bishop,y_bishop,fun):
    moves=list()
    flag=True
    x,y=x_bishop,y_bishop
    while flag:
        x,y=fun(x,y)
        if x<=7 and y<=7 and x>=0 and y>=0:
            if str(x)+","+str(y) not in list_block_points:
                moves.append(str(x)+","+str(y))
            else:
                break         
        else:
            flag=False     
    return moves    

def Get_Horse_Possible_Moves(x_horse,y_horse):
    moves=list()
    for i in horse_move:
        x,y=i(x_horse,y_horse)
        if x<=7 and y<=7 and x>=0 and y>=0 and str(x)+","+str(y) not in list_block_points:
            moves.append(str(x)+","+str(y))
    return moves


def Horse_Move(x_bishop,y_bishop,x_horse,y_horse,expected=None):
    if(expected!=None):
        return expected
        

             
        

def Bishop_Move(x_bishop,y_bishop,x_horse,y_horse):
    expected=""
    nex="" 
    if (x_bishop+y_bishop)%2 != (x_horse+y_horse)%2:
        found=False
        moves=Get_Horse_Possible_Moves(x_horse,y_horse)
        moves_bishop=Get_all_Bishop_Possible_Moves(x_bishop,y_bishop)
        for i in moves:
            moves_check=Get_all_Bishop_Possible_Moves(int(i.split(",")[0]),int(i.split(",")[1]))
            for y in moves_check:
                if y in moves_bishop:
                    expected=i
                    nex=y
                    found=True
            if(found):
                break
        if found==False:
            for i in moves:
                nex=Move_Bishop_with_surrounding(x_bishop,y_bishop,int(i.split(",")[0]),int(i.split(",")[1]))
                if(nex!=""):
                    expected=i
                    break       
    else:
        nex=None
        expected=None
        
    return nex,expected

def Move_Bishop_with_surrounding(x_bishop,y_bishop,x_horse,y_horse):
    horse_surrounding=[str(x_horse-1)+","+str(y_horse),str(x_horse+1)+","+str(y_horse),str(x_horse)+","+str(y_horse-1),str(x_horse)+","+str(y_horse+1)]
    for i in horse_surrounding:
        if i in list_block_points:
            horse_surrounding.remove(i)
    if x_horse<x_bishop and y_horse<y_bishop or x_horse>x_bishop and x_horse>x_bishop:
        moves=Get_Bishop_Possible_Moves(x_bishop,y_bishop,front_right_bishop)
        for i in horse_surrounding:
            h_moves=Get_all_Bishop_Possible_Moves(int(i.split(",")[0]),int(i.split(",")[0]))
            for y in moves:
                if y in h_moves:
                    return y
        moves=Get_Bishop_Possible_Moves(x_bishop,y_bishop,back_left_bishop)
        for i in horse_surrounding:
            h_moves=Get_all_Bishop_Possible_Moves(int(i.split(",")[0]),int(i.split(",")[0]))
            for y in moves:
                if y in h_moves:
                    return y
    elif x_horse<x_bishop and y_horse>y_bishop or x_horse>x_bishop and y_horse<y_bishop:
        moves=Get_Bishop_Possible_Moves(x_bishop,y_bishop,front_left_bishop)
        for i in horse_surrounding:
            h_moves=Get_all_Bishop_Possible_Moves(int(i.split(",")[0]),int(i.split(",")[0]))
            for y in moves:
                if y in h_moves:
                    return y
        moves=Get_Bishop_Possible_Moves(x_bishop,y_bishop,back_right_bishop)
        for i in horse_surrounding:
            h_moves=Get_all_Bishop_Possible_Moves(int(i.split(",")[0]),int(i.split(",")[0]))
            for y in moves:
                if y in h_moves:
                    return y
                        


def Get_Common_Position(x_bishop,y_bishop,x_horse,y_horse,check=1,expected=None):
    if(check==1):
        if (x_bishop+y_bishop)%2 == (x_horse+y_horse)%2:
            moves=Get_all_Bishop_Possible_Moves(x_bishop,y_bishop)
            move_h=Get_all_Bishop_Possible_Moves(x_horse,y_horse)
            if str(x_horse)+","+str(y_horse) in moves:
                print("Bishop Moved and met at "+str(x_horse)+","+str(y_horse))
            else:
                coord=random.choice(moves)
                expected=random.choice(Get_Horse_Possible_Moves(x_horse,y_horse))
                print("Bishop Moved to "+coord)
                Get_Common_Position(int(coord.split(",")[0]),int(coord.split(",")[1]),x_horse,y_horse,0,expected)
        else:    
            nex,expected=Bishop_Move(x_bishop,y_bishop,x_horse,y_horse)
            if(nex!=None):
                print("Bishop Moved to "+nex)
                Get_Common_Position(int(nex.split(",")[0]),int(nex.split(",")[1]),x_horse,y_horse,0,expected)
            else:
                Get_Common_Position(x_bishop,y_bishop,x_horse,y_horse,0,expected)

    else:
        expected=Horse_Move(x_bishop,y_bishop,x_horse,y_horse,expected)
        print("Horse Moved To : "+expected)
        Get_Common_Position(x_bishop,y_bishop,int(expected.split(",")[0]),int(expected.split(",")[1]),1)


list_block_points=["0,3","0,7","2,0","2,6","4,3","7,1","6,7"]
common_postion=[]
visited=[]
horse_move=[front_left,front_right,back_left,back_right,left_left,left_right,right_left,right_right]
bishop_move=[front_left_bishop,front_right_bishop,back_left_bishop,back_right_bishop]
horse_possible=[]
bishop_possible=[]
meet_positions=set()
if __name__ == "__main__":
    bishop_coordinate=input("Current Bishop Coordinate : ")
    x_bishop,y_bishop = bishop_coordinate.split(",")
    horse_coordinate=input("Current Horse Coordinate : ")
    x_horse,y_horse = horse_coordinate.split(",")
    if(Block_Check(x_bishop,y_bishop)==True and Block_Check(x_horse,y_horse)==True ): 
        Get_Common_Position(int(x_bishop),int(y_bishop),int(x_horse),int(y_horse))
        for i in meet_positions:
            print("Meet Position : "+i)  
    else:
        print("Inactive Grid Coordinates given!!!")

                             