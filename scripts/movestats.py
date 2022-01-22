# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:37:03 2021

@author: justi
"""

import os
from itertools import islice
import re
import math

path = "C:\Work\PowerBI\Chess1"  
    
gamestats = 'stats'
stats = open(gamestats + '.csv', 'w')  
stats.writelines('Gamenumber, Round, Result, White, Black, Number of moves, Pawn moves, White pawn moves, Black pawn moves, Knight moves, White knight moves, Black knight moves, Bishop moves, White bishop moves, Black bishop moves, Rook moves, White rook moves, Black rook moves, Queen moves, White queen moves, Black queen moves, King moves, White king moves, Black king moves, Captures, White captures, Black captures, Castling moves, White castling moves, Black castling moves')
stats.writelines('\n')

stats.close()

for gamenumber in range(1075):
    
    headersfile = 'headers' + str(gamenumber+1) + '.txt'
    gamefile = 'game' + str(gamenumber+1) + '.txt'
    gamenumber = gamenumber + 1
    
    h = open(headersfile, 'r')
    g = open(gamefile, 'r')
    
    #variable headers
    
    head = h.readlines()
    
    pawnmove = 0
    whitepawnmove = 0
    blackpawnmove = 0
    knightmove = 0
    whiteknightmoves = 0
    blackknightmoves = 0
    bishopmove = 0
    whitebishopmoves = 0
    blackbishopmoves = 0
    rookmove = 0
    whiterookmoves = 0
    blackrookmoves = 0
    queenmove = 0
    whitequeenmoves = 0
    blackqueenmoves = 0
    kingmove= 0
    whitekingmoves = 0
    blackkingmoves= 0
    promotedknightmove = 0
    promotedbishopmove = 0
    promotedrookmove = 0
    promotedqueenmove = 0
    whitepromotions = 0
    blackpromotions = 0
    whitequeenpromotions = 0
    blackqueenpromotions = 0
    whiterookpromtions = 0
    blackrookpromotions = 0
    whitebishoppromotions = 0
    blackbishoppromotions = 0
    whiteknightpromotions = 0
    blackknightpromotions = 0
    capturecount = 0
    whitecapturecount = 0
    blackcapturecount = 0
    checkcount = 0
    whitewin = 0
    blackwin = 0
    draw = 0
    castlecount = 0
    whitecastling = 0
    blackcastling = 0
    
    for line in head:
        header = line.split('\"')
      
        if (header[0] == "[Site "):
            Site = header[1]
            printSite = Site
           # print('Site = ' + printSite)
         
        if (header[0] == "[Round "):
            Round = header[1]
            printRound = Round       
            #print('Round = ' + printRound)
     
        if (header[0] == "[White "):
            White = header[1]  
            printWhite = White
            printWhite = printWhite.split(',')
            printWhite1 = printWhite[0] + printWhite[1]  
            #print('White = ' + printWhite1)
 
        if (header[0] == "[Black "):
            Black = header[1]
            printBlack = Black
            printBlack = printBlack.split(',')
            printBlack1 = printBlack[0] + printBlack[1]
            #print('Black = ' + ' ' + printBlack1)            
   
        if (header[0] == "[WhiteElo "):
            WhiteElo = str(header[1])
            printWhiteElo = WhiteElo
            #print('WhiteElo = ' + printWhiteElo)
         
        if (header[0] == "[BlackElo "):
            BlackElo = str(header[1])
            printBlackElo = BlackElo
            #print('BlackElo = ' + printBlackElo)
 
        if (header[0] == "[ECO "):
            ECO = str(header[1])
            printECO = ECO
            #print('ECO = ' + printECO)

        if (header[0] == "[Date "): 
            Date = str(header[1])
            printDate = Date
            #print('Date = ' + printDate)
 
        if (header[0] == "[Result "):
            Result = str(header[1])
            printResult = Result
            #print('Result = ' + printResult)        
        
        if (header[0] == "[Opening "):
            Opening = str(header[1])  
            printOpening = Opening
            #print('Opening = ' + ' ' + printOpening)
      
        if (header[0] ==  "[EventDate "):
            Eventdate = str(header[1])
            printEventdate = Eventdate
            #print('EventDate = ' + printEventdate)  
    
    moves = []
    
    for line in g:
        linemoves = line.split(' ')
        actualmoves = []
        newmoves = []
        newline = []
        for move in linemoves:
            dot = move.find('.')
            if (dot > 0):
                newmove = move[dot+1:]
            else:
                newmove = move
            newmove = newmove.replace('\n','')
            if (newmove != ''):
                newline.append(newmove)
 
        moves = moves + newline
      
    if ('1-0' in moves):
        moves.remove('1-0')
    if ('0-1' in moves):
        moves.remove('0-1')
    if ('1/2-1/2' in moves):
        moves.remove('1/2-1/2')
    if ('\x1a' in moves):
        moves.remove('\x1a')
        
    movenumber = 0
    
    for move in moves:
        if (White == 'Carlsen, Magnus' and Black == 'Caruana, Fabiano' and Round == '1'):
            print('move = ' + move[0:4])
        movenumber = movenumber + 1
        if (move[0] == 'N' and movenumber%2 == 0):
            knightmove = knightmove + 1
            whiteknightmoves = whiteknightmoves + 1
        if (move[0] == 'N' and movenumber%2 == 1):
            knightmove = knightmove + 1
            blackknightmoves = blackknightmoves + 1
        if (move[0] == 'B' and movenumber%2 == 0):
            bishopmove = bishopmove + 1
            whitebishopmoves = whitebishopmoves + 1
        if (move[0] == 'B' and movenumber%2 == 1):
            bishopmove = bishopmove + 1
            blackbishopmoves = blackbishopmoves + 1
        if (move[0] == 'R' and movenumber%2 == 0):
            rookmove = rookmove + 1
            whiterookmoves = whiterookmoves + 1
        if (move[0] == 'R' and movenumber%2 == 1):
            rookmove = rookmove + 1
            blackrookmoves = blackrookmoves + 1
        if (move[0] == 'Q' and movenumber%2 == 0):
            queenmove = queenmove + 1
            whitequeenmoves = whitequeenmoves + 1
        if (move[0] == 'Q' and movenumber%2 == 1):
            queenmove = queenmove + 1
            blackqueenmoves = blackqueenmoves + 1         
        if (move[0] == 'K' and movenumber%2 == 0):
            kingmove = kingmove + 1
            whitekingmoves = whitekingmoves + 1
        if (move[0] == 'K' and movenumber%2 == 1):
            kingmove = kingmove + 1
            blackkingmoves = blackkingmoves + 1            
        if (('O-O' in move) and ('O-O-O' not in move) and (movenumber%2 == 0)):
            kingmove = kingmove + 1
            castlecount = castlecount + 1
            whitekingmoves = whitekingmoves + 1
            whitecastling = whitecastling + 1
            whitecastlingmovenumber = math.floor(int(movenumber)/2)
            print (move)
            print ('white castling')
        if (('O-O' in move) and ('O-O-O' not in move) and (movenumber%2 == 1)):
            kingmove = kingmove + 1
            castlecount = castlecount + 1
            blackkingmoves = blackkingmoves + 1
            blackcastling = blackcastling + 1
            blackcastlingmovenumber = math.floor(int(movenumber)/2)
            print (move)
            print ('black castling')
        if (('O-O-O' in move) and ('O-O' not in move) and (movenumber%2 == 0)):
            kingmove = kingmove + 1
            castlecount = castlecount + 1
            whitekingmoves = whitekingmoves + 1
            whitecastling = whitecastling + 1
            whitecastlingmovenumber = math.floor(int(movenumber)/2)
            print (move)
            print ('white castling')
        if (('O-O-O' in move) and ('O-O' not in move) and (movenumber%2 == 1)):
            kingmove = kingmove + 1
            castlecount = castlecount + 1
            blackkingmoves = blackkingmoves + 1
            blackcastling = blackcastling + 1
            blackcastlingmovenumber = math.floor(int(movenumber)/2)
            print (move)
            print ('black castling')

        if (move[0] == 'a' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'a' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1
        if (move[0] == 'b' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'b' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1        
        if (move[0] == 'c' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'c' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1
        if (move[0] == 'd' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'd' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1
        if (move[0] == 'e' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'e' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1
        if (move[0] == 'f' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'f' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1  
        if (move[0] == 'g' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'g' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1  
        if (move[0] == 'h' and movenumber%2 == 0):
            pawnmove = pawnmove + 1
            whitepawnmove = whitepawnmove + 1
        if (move[0] == 'h' and movenumber%2 == 1):
            pawnmove = pawnmove + 1
            blackpawnmove = blackpawnmove + 1  
            
        if ('x' in move and movenumber%2 == 0):
            whitecapturecount = whitecapturecount + 1
            capturecount = capturecount + 1
        if ('x' in move and movenumber%2 == 1):
            blackcapturecount = blackcapturecount + 1
            capturecount = capturecount + 1
        if ('=N' in move and movenumber%2 == 0):
            promotedknightmove = promotedknightmove + 1
            whitepromotions = whitepromotions + 1
            whiteknightpromotions = whiteknightpromotions + 1
        if ('=N' in move and movenumber%2 == 1):
            promotedknightmove = promotedknightmove + 1
            blackpromotions = blackpromotions + 1
            blackknightpromotions = blackknightpromotions + 1
        if ('=B' in move and movenumber%2 == 0):
            promotedbishopmove = promotedbishopmove + 1
            whitepromotions = whitepromotions + 1
            whitebishoppromotions = whitebishoppromotions + 1
        if ('=B' in move and movenumber%2 == 1):
            promotedbishopmove = promotedbishopmove + 1
            blackpromotions = blackpromotions + 1
            blackbishoppromotions = blackbishoppromotions + 1
        if ('=R' in move and movenumber%2 == 0):
            promotedrookmove = promotedrookmove + 1
            whitepromotions = whitepromotions + 1
            whiterookpromtions = whiterookpromtions + 1
        if ('=R' in move and movenumber%2 == 1):
            promotedrookmove = promotedrookmove + 1
            blackpromotions = blackpromotions + 1
            blackrookpromotions = blackrookpromotions + 1
        if ('=Q' in move and movenumber%2 == 0):
            promotedqueenmove = promotedqueenmove + 1
            whitepromotions = whitepromotions + 1
            whitequeenpromotions = whitequeenpromotions + 1
        if ('=Q' in move and movenumber%2 == 1):
            promotedqueenmove = promotedqueenmove + 1
            blackpromotions = blackpromotions + 1
            blackqueenpromotions = blackqueenpromotions + 1
          
    #print(moves)
    
    stats = open('stats.csv', 'a')
    stats.writelines(str(gamenumber) + ',' + str(Round) + ',' + str(Result) + ',' + str(printWhite1) + ',' + str(printBlack1) + ',' + str(movenumber) + ',' + str(pawnmove) + ',' + str(whitepawnmove) + ',' + str(blackpawnmove) + ',' + str(knightmove) + ',' + str(whiteknightmoves) + ',' + str(blackknightmoves) + ',' + str(bishopmove) + ',' + str(whitebishopmoves) + ',' + str(blackbishopmoves) + ',' + str(rookmove) + ',' + str(whiterookmoves) + ',' + str(blackrookmoves) + ',' + str(queenmove) + ',' + str(whitequeenmoves) + ',' + str(blackqueenmoves) + ',' + str(kingmove) + ',' + str(whitekingmoves) + ',' + str(blackkingmoves) + ',' + str(capturecount) + ',' + str(whitecapturecount) + ',' + str(blackcapturecount) + ',' + str(castlecount) + ',' + str(whitecastling) + ',' + str(blackcastling) + '\n')
    stats.close()
    #+ ',' + str(whitecaptures) + ',' + str(blackcaptures))
                     #, White castling moves, Black castling moves, Captures, White captures, Black captures')
    #+ ',' + str(capturecount))
    #+ ',' + str(whitecapturecount) + ',' + str(blackcapturecount) + ',' + str(castling) + ',' + str(whitecastling) + ',' + str(blackcastling) + '\n')
    
    #stats.writelines('Number of moves,' + str(math.floor(int(movenumber)/2)) + '\n')
    #stats.writelines('Pawn moves,' + str(pawnmove) + '\n')  
    #stats.writelines('Knight moves,' + str(knightmove) + '\n')
    #stats.writelines('Bishop moves,' + str(bishopmove) + '\n')
    #stats.writelines('Rook moves,' + str(rookmove) + '\n')
    #stats.writelines('Queen moves,' + str(queenmove)+ '\n')
    
    #stats.writelines('White pawn moves,' + str(whitepawnmove) + '\n')
    #stats.writelines('Black pawn moves,' + str(blackpawnmove) + '\n')
    
    #stats.writelines('White knight moves,' + str(whiteknightmoves) + '\n')
    #stats.writelines('Black knight moves,' + str(blackknightmoves) + '\n')
    #stats.writelines('White bishop moves,' + str(whitebishopmoves) + '\n')
    #stats.writelines('Black bishop moves,' + str(blackbishopmoves) + '\n')
    #stats.writelines('White rook moves,' + str(whiterookmoves) + '\n')
    #stats.writelines('Black rook moves,' + str(blackrookmoves) + '\n')
    
    #stats.writelines('White queen moves,' + str(whitequeenmoves) + '\n')
    #stats.writelines('Black queen moves,' + str(blackqueenmoves) + '\n')
        
    #stats.writelines('White king moves,' + str(whitekingmoves) + '\n')
    #stats.writelines('Black king moves,' + str(blackkingmoves) + '\n')
    
    #stats.writelines('White captures,' + str(whitecapturecount) + '\n')
    #stats.writelines('Black captures,' + str(blackcapturecount) + '\n')
    
    #stats.writelines('White castling,' + str(whitecastling) + '\n')
    #stats.writelines('Black castling,' + str(blackcastling) + '\n')
    
    #if (str(whitecastling) == "1"):
        #stats.writelines('White castling move number,' + str(whitecastlingmovenumber) + '\n')
    #else:
        #stats.writelines('White castling move number,' + 'N/A' + '\n')
        
    #if (str(blackcastling) == "1"):
        #stats.writelines('Black castling move number,' + str(blackcastlingmovenumber) + '\n')
    #else:
        #stats.writelines('Black castling move number,' + 'N/A' + '\n')
    
    #stats.writelines('White promotions,' + str(whitepromotions) + '\n')
    #stats.writelines('Black promotions,' + str(blackpromotions) + '\n')
    #stats.writelines('White knight promotions,' + str(whiteknightpromotions) + '\n')
    #stats.writelines('Black knight promotions,' + str(blackknightpromotions) + '\n')
    
    #stats.writelines('White bishop promotions,' + str(whitebishoppromotions) + '\n')
    #stats.writelines('Black bishop promotions,' + str(blackbishoppromotions) + '\n')
    #stats.writelines('White rook promotions,' + str(whiterookpromtions) + '\n')
    #stats.writelines('Black rook promotions,' + str(blackrookpromotions) + '\n')
    
    #stats.writelines('White queen promotions,' + str(whitequeenpromotions) + '\n')
    #stats.writelines('Black queen promotions,' + str(blackqueenpromotions) + '\n')

stats.close()