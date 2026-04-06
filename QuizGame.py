name = input("And your name is... ")
print(f"Welcome to the quiz, {name}, let's start!")
score = 0

Question_1 = ("Which is the largest river in the world?")

print(f"Question number 1: {Question_1}")
#Posibles answers for question 1
Answers_1 = ("a: Nilo \nb: Manzanares \nc: Amazonas \nd: Tajo")
print (f"The posibles answers are:\n{Answers_1}")
Your_Answer_1 = input("And your answer is... ")
if Your_Answer_1 == "a" : 
     score +=1
     print (f"You are right! \nYour score now is {score}, good boy")
else: score -=1
print (f"You failed, keep trying! \n Your score now is: {score}")