# Search if the word "learning" exists in the file or not.

def checkForWord():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("The word 'learning' exists in the file.")
        else:
            print("Not Found")

checkForWord()