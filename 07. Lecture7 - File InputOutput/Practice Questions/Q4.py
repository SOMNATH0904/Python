# WAF to find in which line of the file does the word "learning" occur first.
# Print-1 if the word not found.

def checkForLine():
    word = "programming"
    data = True
    lineNo = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineNo)
            lineNo += 1
    return -1

checkForLine()