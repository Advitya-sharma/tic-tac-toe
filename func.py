import sys

def rules():
    print("rules:")
    print(">>overwriting other user's previous input will cost you your turn")
    print(" >>enter valid numbers between 1 and 9 or giveaway your turn\n\n")
def win_check(d):
     winning_positions =[[d[1],d[2],d[3]],
                         [d[4],d[5],[6]],
                         [d[7],d[8],d[9]],
                         [d[9],d[3],d[6]],
                         [d[1],d[4],d[7]],
                         [d[2],d[5],d[8]],
                          [d[1],d[5],d[9]],
                          [d[3],d[5],d[7]]]
     symbol1 = ['X','X','X']
     symbol2= ['O','O','O']
     if(symbol1 in  winning_positions):
        print("you won player X".upper())
        sys.exit()
            
     elif(symbol2 in  winning_positions):
         print("you won player O".upper())
         sys.exit()

def screen_maker(d):
    
    print(d[1],"|",d[2], "|",d[3],sep="  ")
    print("---+-----+--",end="\n",sep="  ")
    print(d[4], "|",d[5], "|",d[6],sep="  ")
    print("---+-----+--",end="\n",sep="  ")
    print(d[7], "|",d[8], "|",d[9],sep="  ")
    print("---+-----+--",end="\n",sep="  ")
    win_check(d)
def turn_asker(d):
    global x
    if x==1:
        print("\n\nenter the number where you want to insert X",end="\n\n")
        user_input_x(d,lst)
        x=0
    else:
        print("\n\n enter the number where you want to insert O",end="\n\n")
        user_input_o(d,lst)
        x=1

def user_input_x(d,lst):

    _ = int(input())
    if _ in lst:
         print("\n You cannot overwrite other users input")
    else:
        d[_]="X"
        lst.append(_)
       
def user_input_o(d,lst):
    
    _ = int(input())
    if _ in lst:
         print("\n You cannot overwrite other users input")
    else:
        d[_]="O"
        lst.append(_)
lst=[]
x=1
