# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:38:45 2021

@author: justi
"""

import os
import math

path = "C:\Work\PowerBI\Chess"
os.chdir(path)
for file in os.listdir(path):
    if (file[0:7] == "headers"):
        os.remove(file)
    if (file[0:4] == "game"):
        os.remove(file)

