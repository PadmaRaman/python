import random
import time

word = ["orange","banana","watermelon","mango","jackfruit","lychee","apple","pomogranate"]
random.shuffle(word)

word_list=list(word[1])

output = []
output.extend(word_list)
guesses = len(output)+2

for i in range(len(output)):
    output[i] = '_'
print (output)
    
while guesses>0:
    guess = input("Guess a word (Hint:Fruits)")
    guess = guess.lower()
    for i in range(len(word_list)):
        if guess in word_list[i]:
            output[i] = guess
    guesses-=1
            
    print ("You have %d guesses left" %(guesses))
    print (output)
    if " ".join(output) in " ".join(word_list):
          print ("You guessed it")
          time.sleep(5)
          break
##    else:
##          print ("You haven't guessed it")
##          time.sleep(5)


if " ".join(output) not in " ".join(word_list):
    print ("You haven't guessed it")
    time.sleep(5)



    
    
    


