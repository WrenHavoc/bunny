#!/bin/python3
import os, time, multiprocessing
from os import system

def Popups():
    os.system("python3 ./popups.py")

def Bomb():
    os.system("python3 ./bomb.py")

p1 = multiprocessing.Process(name='p1', target=Popups)
p = multiprocessing.Process(name='p', target=Bomb)
p1.start()
time.sleep(10)
p.start()
