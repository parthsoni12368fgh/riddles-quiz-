import random
print("welcome to super coders quiz")
print("-"*40)
score = 0
riddles = {}
with open ("riddles.txt", "r") as x:
    ques = x.readlines()
    for question in ques:
        q,a = question.strip().split(":")
        riddles[q] = a
print()

print("maximum questions asked : 5")
print("correct answer  : 2 marks")
print("wrong answer : -1 marks")
q_count = 0
question = list(riddles.keys())
random.shuffle(question)
for q in question:
    print(q)
    ans = input("enter the answer").lower()
    if ans == riddles[q].lower():
        print("correct answer")
        score = score + 2
    else:
        print("you got it wrong")
        score = score - 1
        print("correct answer", riddles[q])
    print(" current score", score)
    q_count = q_count+1
    if q_count== 5:
        break
print("end of the riddles quiz")
print("total score", score)







        





    
    







