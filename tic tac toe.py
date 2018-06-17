import time

class tictactoe:
    def __init__ (self):
        self.board = [" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print (" %s | %s | %s " %(self.board[1],self.board[2],self.board[3]))
        print ("--------------")
        print (" %s | %s | %s " %(self.board[4],self.board[5],self.board[6]))
        print ("--------------")
        print (" %s | %s | %s " %(self.board[7],self.board[8],self.board[9]))

    def update(self,choice,value):
        if self.board[choice] == " ":
            self.board[choice] = value
        else:
            print ("Already Occupied")
                   

    def tie(self):
        used = 0
        for i in self.board:
            if i != " ":
                used +=1
        if used == 9:
            return True
        else:
            return False
                
    def winner(self,value):
        if (self.board[1]==value and self.board[2]==value and self.board[3]==value) or (self.board[4]==value and self.board[5]==value and self.board[6]==value) or (self.board[7]==value and self.board[8]==value and self.board[9]==value) or (self.board[1]==value and self.board[5]==value and self.board[9]==value) or (self.board[3]==value and self.board[5]==value and self.board[7]==value) or (self.board[1]==value and self.board[4]==value and self.board[7]==value) or (self.board[2]==value and self.board[5]==value and self.board[8]==value) or (self.board[3]==value and self.board[6]==value and self.board[9]==value):
            return True

    def reset(self):
        self.board = [" "," "," "," "," "," "," "," "," "," "]

cname = tictactoe()

def welcome():
    print ("Welcome to Tictactoe\n")
welcome()
cname.display()


while True:
    x = int(input(" Please enter no between 1 - 9 "))
    cname.update(x,"X")
    cname.display()

    if cname.winner("X"):
        print ("X wins\n")
        chance = input ("Do you want to play again (Y/N) ")
        if chance.upper() == "Y":
            cname.reset()
            cname.display()
        else:
            time.sleep(2)
            break

    if cname.tie():
        print ("Tie\n")
        chance = input ("Do you want to play again (Y/N) ")
        if chance.upper() == "Y":
            cname.reset()
            cname.display()
        else:
            time.sleep(2)
            break


    o = int (input("Please enter no between 1 - 9 "))
    cname.update(o,"O")
    cname.display()

    if cname.winner("O"):
        print ("O wins\n")
        chance = input ("Do you want to play again (Y/N) ")
        if chance.upper() == "Y":
            cname.reset()
            cname.display()
        else:
            time.sleep(2)
            break

    if cname.tie():
        print ("Tie\n")
        chance = input ("Do you want to play again (Y/N) ")
        if chance.upper() == "Y":
            cname.reset()
            cname.display()
        else:
            time.sleep(2)
            break


    
welcome()
