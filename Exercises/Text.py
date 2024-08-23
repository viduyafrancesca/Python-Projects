# Ex 1: Print "FizzBuzz" 100 times, "FizzBuzz" for multiples of both 3 and 5, "Fizz" for multiple of 3, "Buzz" for multiple of 5
def fizz_buzz():
    for x in range(100):
        if x%3 == 0 and x%5 == 0:
            return "FizzBuzz"
        elif x%3 == 0:
            return "Fizz"
        elif x%5 == 0:
            return "Buzz"

# Ex 2: Reverse given string        
def reverse_string(string):
    return string[::-1]

# Ex 3: Pig Latin: Push consonant to the back of string and add "ay", if first letter is vowel add "yay" to the end
def pig_latin(string):
    vowel = ['a', 'e', 'i', 'o' ,'u', 'A','E','I','O','U']
    transpose = ""
    firstLetter = string[0]
    counter = 0
    if string[0] in vowel:
        return string+"-yay"
    else:
        # Rule for Y: If y is at the end of 2-letter word or if at end of consonant cluster, treat it as vowel
        if 'y' in string or 'Y' in string:
            if len(string) == 2:
                if string[1] == 'Y' or string[1] == 'y':
                    return string[1]+"-"+string[0]+"ay"
            else:
                if firstLetter == 'y' or firstLetter == 'Y':
                    return string[1:]+"-"+string[0]+"ay"
                else:
                    while not (firstLetter == 'Y' or firstLetter == 'y'):
                        transpose += string[counter]
                        counter += 1
                        firstLetter = string[counter]
                    return string[counter:]+"-"+transpose+"ay"

        else:
            while firstLetter not in vowel:
                transpose += string[counter]
                counter += 1
                if counter >= len(string):
                    break
                firstLetter = string[counter]
            return string[counter:]+"-"+transpose+"ay"
    
# Ex 4: Print number of vowels in string
def number_of_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    output = dict.fromkeys(vowels,0)
    for x in string:
        if x in vowels:
            output[x] += 1

    return output

# Ex 5: Palindrome checker
def palindrome(string):
    return True if string[::-1] == string else False

# Ex 6: Count words in a string, read from a text file and generate summary
import re
def count_words(string):
    filePath = "Exercises/"+string
    count = 0
    try:
        file = open(filePath,"r")
        for x in file.readlines():
            count += len(re.split(r"[.,;:!?\s]\s*", x.strip())) #Split including period, comma, semicolon, colon, exclamation, question mark, spaces
    except OSError as e:
        return "File not found"
    return count

# Ex 7: Text editor: Notepad that can open, edit, and save text documents
def notepad():
    userChoice = 0
    userCreatedFilenames = []
    userChoice = int(input("[1]View Files\n[2]Read File\n[3]Edit File\n[4]Create File\n[0]Exit "))
    
    while userChoice >=1:
        if userChoice == 1:
            print(printFilenames(userCreatedFilenames))
        elif userChoice == 2:
            checkExistingFiles = printFilenames(userCreatedFilenames)
            print(checkExistingFiles)
            if checkExistingFiles != "No files created yet":
                try:
                    fileName = "Exercises/"+input("Enter filename to read: ")
                    file = open(fileName,"r")
                    for x in file.readlines():
                        print(x)
                except OSError as e:
                    print("File not found")
        elif userChoice == 3:
            checkExistingFiles = printFilenames(userCreatedFilenames)
            print(checkExistingFiles)
            if checkExistingFiles != "No files created yet":
                editFile = input("Enter name of file to edit: ")
                appendOrOverwite = input("Choose action:\n[1]Append\n[2]Overwrite")
                fileName = "Exercises/"+editFile
                file = open(fileName,"r") #read the file first
                for x in file.readlines():
                    print(x)
                newLines = []
                while True:
                    line = input()
                    if not line:
                        break
                    newLines.append(line+"\n")
                
                if appendOrOverwite == 1:
                    file = open(fileName, "a")
                    for x in newLines:
                        print(x)
                        file.write(x)
                elif appendOrOverwite == 2:
                    file = open(fileName, "w")
                    for x in newLines:
                        file.write(x)
        elif userChoice == 4:
            fileName = input("Enter filename with .txt extension: ")
            filePath = "Exercises/"+fileName
            print("Enter contents of file below and double enter once done")
            contents = []
            while True:
                line = input()
                if not line:
                    break
                contents.append(line+"\n")
            
            file = open(filePath, "w")
            for x in contents:
                print(x)
                file.write(x)
            userCreatedFilenames.append(fileName)
        userChoice = int(input("[1]View Files\n[2]Read File\n[3]Edit File\n[4]Create File\n[0]Exit "))
    
    return "Program Terminated"


def printFilenames(userCreatedFilenames):
    if len(userCreatedFilenames) == 0:
        return "No files created yet"
    return [x for x in userCreatedFilenames]

print(notepad())