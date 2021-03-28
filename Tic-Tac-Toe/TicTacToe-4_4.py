#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 07:16:10 2020

@author: saikiran
"""


import random


class TicTacToe:

    def __init__(self):
        self.board = [' ']*16
        self.children = []
        self.rewards = 0
        self.selections = 0
        self.limit = 50000
        
    def Display_board(self):
        print(' ' + self.board[0] + '|' +  self.board[1] + '|' + self.board[2]+ '|' + self.board[3])
        print('_________')
        print(' ' + self.board[4] + '|' +  self.board[5] + '|' + self.board[6]+ '|' + self.board[7])
        print('_________')
        print(' ' + self.board[8] + '|' +  self.board[9] + '|' + self.board[10]+ '|' + self.board[11])
        print('_________')
        print(' ' + self.board[12] + '|' +  self.board[13] + '|' + self.board[14]+ '|' + self.board[15])
        
    
    def Reset(self):
        self.board = [' '] * 16
        
        
    def Free_slots(self,state):
        freeslots = [i+1 for i,v in enumerate(state) if v == ' '] 
        return freeslots
    
    
    def Win(self,state):
        if(state[0] == state[1] == state[2] == state[3]!= ' '):
            return state[0] == state[1] == state[2] == state[3]
        elif(state[4] == state[5] == state[6] == state[7] != ' '):
            return state[4] == state[5] == state[6] == state[7]
        elif(state[8] == state[9] == state[10] == state[11] != ' '):
            return state[8] == state[9] == state[10] == state[11]
        elif(state[12] == state[13] == state[14] == state[15] != ' '):
            return state[12] == state[13] == state[14] == state[15]
        elif(state[0] == state[4] == state[8] == state[12] != ' '):
            return state[0] == state[4] == state[8] == state[12]
        elif(state[1] == state[5] == state[9] == state[13] !=  ' '):
            return state[1] == state[5] == state[9] == state[13]
        elif(state[2] == state[6] == state[10] == state[14] != ' '):
            return state[2] == state[6] == state[10] == state[14]
        elif(state[3] == state[7] == state[11] == state[15] != ' '):
            return state[3] == state[7] == state[11] == state[15]
        elif(state[0] == state[5] == state[10] == state[15] != ' '):
            return state[0] == state[5] == state[10] == state[15]
        elif(state[3] == state[6] == state[9] == state[12] != ' '):
            return state[3] == state[6] == state[9] == state[12]
        
        
        
    def Start(self):
        print('\n---------------------------')
        print('Welcome to TicTacToe')
        print('---------------------------')
        print('\n Board and Slot Numbers below')
        print(' '+'1 '+'|'+'2 '+'|'+'3 ''|'+'4')
        print('-------------')
        print(' '+'5 '+'|'+'6 '+'|'+'7 ''|'+'8')
        print('-------------')
        print(' '+'9 '+'|'+'10'+'|'+'11''|'+'12')
        print('-------------')
        print(' '+'13'+'|'+'14'+'|'+'15''|'+'16')
        self.Play()
        
    
    def Play(self):
        self.Reset()
        
        while(True):
            first = input('Wanna go first? (y or n):')
            if(first.lower() == 'y'):
                index = 'X'
                break
            elif(first.lower() == 'n'):
                index = 'O'
                break
            else:
                print('Wrong Input. Please enter either y or n')
  
        while(True):
            if index == 'X':
                print('\nAvailable Slots:' + str(self.Free_slots(self.board)))
                slot = input('Player - Please select your slot number: ')
                if(slot in [str(i) for i in self.Free_slots(self.board)]):                    
                    self.board[int(slot) - 1] = 'X'
                    self.Display_board()
                    if self.Win(self.board):
                        print('\nPlayer won the game')
                        break
                    elif(len(self.Free_slots(self.board)) == 0):
                        print("\nIt's a draw")
                        break
                    else:
                        index = 'O'
                        
                else:
                    print('Slot ' + slot + ' is not available')
                    
            else:
                print('\nComputers turn')
                if(len(self.Free_slots(self.board)) == 16):
                    slot = random.choice(self.Free_slots(self.board))
                elif(len(self.Free_slots(self.board)) == 1):
                    slot = self.Free_slots(self.board)[0]
                else:
                    slot = self.AI()
                self.board[int(slot) - 1] = 'O'
                self.Display_board()
                if self.Win(self.board):
                    print('\nComputer won the game')
                    break
                elif(len(self.Free_slots(self.board)) == 0):
                    print("\nIt's a draw")
                    break
                else:
                    index = 'X'
        self.End()
        
 
    def End(self):
        while(True):
            play = input('Wanna play again? (y or n): ')
            if(play.lower() in ['y','n']):
                break
            else:
                print('Wrong Input. Please enter either y or n')
        if(play.lower() == 'y'):
            self.Reset()
            self.Play()
        else:
            print('Thanks for playing. Have a great day!!!')
            
    
    def AI(self):
        self.children = []
        state = []
        for i in self.board:
            if i == 'X':
                state.append(1)
            elif i == 'O':
                state.append(-1)
            else:
                state.append(i)
                
        for i in self.Free_slots(self.board):
            self.rewards = 0
            self.selections = 0
            s = [i for i in state]
            s[i-1] = -1
            if self.Win(s):
                return i
            else:
                self.Simulation(s,self.Free_slots(s),1)
            self.children.append([self.rewards,self.selections])
            
        return self.Getbest()
    
    
    def Reward(self,turn):
        if turn == -1:
            return 1
        else:
            return 0

 
    def Simulation(self,state,slots,turn):       
        for i in slots:
            if self.selections == self.limit:
                break
            else:
                s = [s for s in state]
                s[i-1] = turn
                if self.Win(s):
                    r = self.Reward(turn)
                    self.rewards = self.rewards + r
                    self.selections = self.selections + 1
    
                elif s.count(' ') == 0:
                    self.rewards = self.rewards + 0.5
                    self.selections = self.selections + 1
    
                else:
                    self.Simulation(s,self.Free_slots(s),turn * -1)
    
    
    def Getbest(self):
        slots = self.Free_slots(self.board)
        best = -1e400
        for i in self.children:
            if i[0] > best:
                best = i[0]
                index = self.children.index(i)
        
        return slots[index]
            
    
if __name__ == '__main__' :
    c = TicTacToe()
    c.Start()
    

