#!/usr/bin/env python3
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
