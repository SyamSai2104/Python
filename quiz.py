questions = ("What is the capital of Japan?: ",
             'Which planet is known as the "Red Planet"?: ',
             "What is the chemical symbol for gold?: ",
             "In tennis, what is a zero score called?: ",
             "In which year did World War II end?: ")
options =(("A.Beijing","B.Seoul","C.Tokyo","D.Bangkok"),
          ("A.Venus","B.Mars","C.Jupiter","D.Saturn"),
          ("A.Ag","B.Au","C.Fe","D.Pb"),
          ("A.Love","B.Nil","C.Zero","D.Duck"),
          ("A.1943","B.1945","C.1950","D.1939"))

answers=("C","B","B","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A,B,C,D): ").upper()
    
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("------------")
        print("correct")
        print("------------")
    else:
        print("------------")
        print("wrong")
        print(f"{answers[question_num]} is the answer")
        print("------------")
    question_num += 1
for answer in answers:
    print(answer,end=" ")
print()
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(score,"%")
