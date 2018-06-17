import random
import time
#to scramble the middle letters
class scramblewords:
    
    def scramble(A):
        wordlen = len(A)
        first = A[0]
        if wordlen <= 3:
            print (A, end = " ")
        elif A[-1] == "." or A[-1]=="," or A[-1]=="?":
            length =wordlen-2
            last = A[length:]
            middle = list(A[1:length])
            random.shuffle(middle)
            print (first+"".join(middle)+last,end = " ")
        else:
            length =wordlen-1
            last = A[length:]
            middle = list(A[1:length])
            random.shuffle(middle)
            print (first+"".join(middle)+last,end = " ")



scrambledwords = " "
file = open("scramble.txt","w")
file.write("Python is an interpreted high-level programming language for \
general-purpose programming. Created by Guido van Rossum and first released \
in 1991, Python has a design philosophy that emphasizes code readability,\
notably using significant whitespace.")
file.close()

file = open("scramble.txt","r")
split = file.read().split(" ")

for i in range(len(split)):
    scramblewords.scramble(split[i])
time.sleep(2)
