import os
import json


def sendData():
    f = open('results.txt', 'r')
    lines = f.read()
    print(f.tell())
    for line in lines:
        print(line)


sendData()
