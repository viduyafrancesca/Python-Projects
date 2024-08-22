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

print(palindrome("raceca"))