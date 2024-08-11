'''
Create a program capable of displaying questions to the user like KBC.
Note: Use List data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.
'''

questions = [
    [
        "What is the capital of France?", "Paris", "Lyon", "Bordeaux", "Strasbourg", 1
    ], 
    [
        "which language was used to create Facebook ?", "Python", "French", "JavaScript", "None", 4
    ],
    [
        "What is the capital of France?", "Paris", "Lyon", "Bordeaux", "Strasbourg", 1
    ], 
    [
        "which language was used to create Facebook ?", "Python", "French", "JavaScript", "None", 4
    ],
    [
        "What is the capital of France?", "Paris", "Lyon", "Bordeaux", "Strasbourg", 1
    ], 
    [
        "which language was used to create Facebook ?", "Python", "French", "JavaScript", "None", 4
    ],
    [
        "What is the capital of France?", "Paris", "Lyon", "Bordeaux", "Strasbourg", 1
    ], 
    [
        "which language was used to create Facebook ?", "Python", "French", "JavaScript", "None", 4
    ],
    [
        "What is the capital of France?", "Paris", "Lyon", "Bordeaux", "Strasbourg", 1
    ], 
    [
        "which language was used to create Facebook ?", "Python", "French", "JavaScript", "None", 4
    ],
    [
        "What is the capital of France?", "Paris", "Lyon", "Bordeaux", "Strasbourg", 1
    ], 
    [
        "which language was used to create Facebook ?", "Python", "French", "JavaScript", "None", 4
    ], 
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print("Questions for Rs.", levels[i])
    print(question[0])
    print("1.",question[1], "              2.", question[2])
    print("3.",question[3], "           4.", question[4])
    reply = int(input("Enter your answer (1-4) or 0 to quit :"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print("Correct answer, you have won Rs.", levels[i])
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 3200000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer !!")
        break

print("Your take home money is :", money)