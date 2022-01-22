# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:47:41 2021

@author: justi
"""

import os
import math
import re

os.chdir("C:\Work\PowerBI\Chess1")

with open ('WorldChampionship.txt') as f:
    
    z = f.readlines()
    data = f.readlines()
    datafile = open('data.txt','w')
    for line in data:
        datafile.write(line)
    filenumber = 1
    
    headersfile = 'headers1'
    gamefile = 'game1'
    
    headernumber = 1
    gamenumber = 0
    
    h = open(headersfile + '.txt', 'w')
    g = open(gamefile + '.txt', 'w')
    
    #print(z)
    
    for item in z:
                                                            
        if (str(item)[0] == '['):
            print('headers result headernumber = ' + str(headernumber))
            h = open(headersfile + '.txt', 'a')
            item.replace('\n','')
            h.writelines(item)
            lastchar = 'h'
            
        elif (item != '\n'):  
            print('game result gamenumber = ' + str(gamenumber))
            #item.replace('\n',' ')
            print('item = ' + item)
            if (item.isspace() == True and re.search(r"\w+",item) == False):
                print('error is space')
                break
            
            g = open(gamefile + '.txt', 'a')
            g.writelines(item)
            lastchar = 'g'                   
                           
        elif (item == '\n'):
            print ('blankline')
            #print ('\n')
            #print ('filenumber = ' + str(filenumber))
            #print ('gamefile = ' + gamefile)
            
            g.close()
            h.close()
       
            print('gamefile ' + str(gamefile))
            print('headerfile ' + str(headersfile))
                        
            if(lastchar == 'h'):
                #next game
                gamenumber = gamenumber + 1
                print ('gamenumber = ' + str(gamenumber))
                print ('headernumber = ' + str(headernumber))
                
            if(lastchar == 'g'):
                #next header
                headernumber = headernumber + 1
                print ('gamenumber = ' + str(gamenumber))
                print ('headernumber = ' + str(headernumber))
                
            if (abs(gamenumber-headernumber) > 1):
                print ('game mismatch') 
                print ('gamenumber = ' + str(gamenumber))
                print ('headernumber = ' + str(headernumber))
                break
            
            if (gamenumber>headernumber):
                print ('game mismatch') 
                print ('gamenumber = ' + str(gamenumber))
                print ('headernumber = ' + str(headernumber))
                break
                
            headersfile = 'headers' + str(headernumber) 
            gamefile = 'game' + str(gamenumber)
            lastchar = 'o'
            
            g = open(gamefile + '.txt', 'a')
            h = open(headersfile + '.txt', 'a')
            
        else:
            print('error')
            print('item = ' + item)
            print('str(item[0]) = ' + str(item[0]))

 
                    

               