# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:01:17 2021

@author: justi
"""

# open pgn file

import os
import math
from openpyxl import Workbook


os.chdir("C:\Work\PowerBI\Chess")

#Output to excel
                
workbook = Workbook()
sheet = workbook.active
                
sheet["A1"] = "Year"
sheet["B1"] = "Round"
sheet["C1"] = "White"
sheet["D1"] = "Black"
sheet["E1"] = "Result"
sheet["F1"] = "ECO"
workbook.save(filename="WCh.xlsx")
    
with open ('WorldChampionship.pgn') as f:
    
    #games loop
    gamenumber = 0
    for line in f:
        #print(line)
        if "[" in line:
            if "Event" in line:
                Rapid = 0
                if "Rapid" in line:
                    Rapid = 1
            
            if "Date" in line and "EventDate" not in line:
                year = str(line[7:11])
                cells = "A" + str(gamenumber+2)
                sheet[(cells)] = year
            
            if "Round" in line:
                i = 8
                for j in range(i,len(line)-1):
                    while  line[j] !=  ']':
                       j = j + 1
                       #print ("debug")
                       #print ("line = " + line)
                       #print ("i = " + str(i))
                       #print ("j = " + str(j))
                       #print ("line [i] = " + line[i])
                       #print ("line [j] = " + line[j])
                       #print (line[i:j])
                    Roundnumber = line[i:j-1]
                    if (Rapid == 1):
                        Roundnumber = 'R' + Roundnumber

                #print ("Round = " + Roundnumber)
                cells = "B" + str(gamenumber+2)
                sheet[(cells)] = Roundnumber                     

            if ("[White " in line and "WhiteTitle" not in line):
                i = 8
                for j in range(i,len(line)-1):
                    while  line[j] !=  ']':
                       j = j + 1
                       #print ("debug")
                       #print ("line = " + line)
                       #print ("i = " + str(i))
                       #print ("j = " + str(j))
                       #print ("line [i] = " + line[i])
                       #print ("line [j] = " + line[j])
                       #print (line[i:j])
                    White = line[i:j-1]
                    
                #print ("White = " + White)
                cells = "C" + str(gamenumber+2)
                sheet[(cells)] = White
                
            if ("[Black " in line and "BlackTitle" not in line):
                i = 8
                for j in range(i,len(line)-1):
                    while  line[j] !=  ']':
                       j = j + 1
                       #print ("debug")
                       #print ("line = " + line)
                       #print ("i = " + str(i))
                       #print ("j = " + str(j))
                       #print ("line [i] = " + line[i])
                       #print ("line [j] = " + line[j])
                       #print (line[i:j])
                    Black = line[i:j-1]
                    
                #print ("Black = " + Black)
                cells = "D" + str(gamenumber+2)
                sheet[(cells)] = Black
                
            if "Result" in line:
                i = 9
                for j in range(i,len(line)-1):
                    while  line[j] !=  ']':
                       j = j + 1
                       #print ("debug")
                       #print ("line = " + line)
                       #print ("i = " + str(i))
                       #print ("j = " + str(j))
                       #print ("line [i] = " + line[i])
                       #print ("line [j] = " + line[j])
                       #print ("String = " + line[i:j-1])
                       Result = line[i:j-1]

                #print ("Result = " + Result)
                cells = "E" + str(gamenumber+2)
                sheet[(cells)] = Result
                
            if "ECO" in line:
                i = 6
                for j in range(i,len(line)-1):
                    while  line[j] !=  ']':
                       j = j + 1
                       #print ("debug")
                       #print ("line = " + line)
                       #print ("i = " + str(i))
                       #print ("j = " + str(j))
                       #print ("line [i] = " + line[i])
                       #print ("line [j] = " + line[j])
                       #print ("String = " + line[i:j-1])
                       ECO = line[i:j-1]
           
                #print ("ECO = " + ECO)
                
                cells = "F" + str(gamenumber+2)
                sheet[(cells)] = ECO
                gamenumber = gamenumber + 1

            workbook.save(filename="WCh.xlsx")
              
            #Output to textfile
                #with open ("headers.txt","a") as g:
                    #g.write('Year|' + year + '\n')
                    #g.write('Round|' + str(Roundnumber) + '\n')
                    #g.write('White|' + str(White) + '\n')
                    #g.write('Black|' + str(Black) + '\n')
                    #g.write('Result|' + str(Result) + '\n')
                    #g.write('ECO|' + str(ECO) + '\n')
                #g.close()
                
  
        #moves loop
        plynumber = 0
        movenumber = 1
        
        # first line
        while '1.' in line[0:2]:
            i = 2

            # first move - white
            for j in range(i+1,len(line)):
                #print ("debug")
                #print ("line = " + line)
                #print ("i = " + str(i))
                #print ("j = " + str(j))
                #print ("line [i] = " + line[i:i+1])
                #print ("line [j] = " + line[j:j+1])
                movenumber = 1
                algebraicmove = line[i:j]
                #print('move = ' + str(int(movenumber)) + '.' + algebraicmove)

                if (line[j:j+1] == " "):
                    break
            plynumber = 1
                
            # first move - black
            for k in range(j+2,len(line)):
                #print ("debug")
                #print ("line = " + line)
                #print ("j = " + str(j))
                #print ("k = " + str(k))
                #print ("line [j] = " + line[j:j+1])
                #print ("line [k] = " + line[k:k+1])

                algebraicmove = line[j+1:k]
                #print('move = ' + str(int(movenumber)) + '...' + algebraicmove)

                if (line[k:k+1] == " "):
                    break
            plynumber = plynumber + 1
            movenumber = int(plynumber/2)
            
            if (plynumber%2 == 0):
                    print('move = ' + str(int(movenumber)) + '...' + algebraicmove)
                    
            if (plynumber%2 == 1):
                    print('move = ' + str(int(movenumber)) + '.' + algebraicmove)

            # second move onwards
           
            while len(line)>=4:
                stringremaining = line[k+2:len(line)]
                
                line = stringremaining
                         
                for l in range(k+2,len(line)):
                    # print ("debug")
                    # print ("line = " + line)
                    # print ("k = " + str(k))
                    # print ("l = " + str(l))
                    # print ("line [k] = " + line[k:k+1])
                    # print ("line [l] = " + line[l:l+1])
                
                    algebraicmove = line[k+1:l]
                    # if plynumber = 1
                    # print('move = ' + str(int(movenumber)) + '.' + algebraicmove)
                    # else if plynumber = 0
                    #print('move = ' + str(int(movenumber)) + '....' + algebraicmove)
                    if (line[l:l+1] == " "):
                        break
                
                plynumber = plynumber + 1
                movenumber = int(plynumber/2)
                
                print("stringremaining = " + str(stringremaining))
                
                print("plynumber = " + str(plynumber))
                
                if (plynumber%2 == 0):
                    print('move = ' + str(int(movenumber)) + '...' + algebraicmove)
                    
                if (plynumber%2 == 1):
                    print('move = ' + str(int(movenumber)) + '.' + algebraicmove)
            
            break
        
            # check for promotion
            # if move number contains "="
            # check for promotion piece (text after =)
            
            # check for check
            # if move contains "+"
            
            # check for captures
            # if move contains "x"
            
            # check for castling 
            # if move contains "0-0"
            
            # check for piece/pawn move
            # if first letter in [K, Q, R, B, N]
               # then piece move
            # else pawn move
            
            # check for result
            
            # store result