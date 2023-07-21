"""Count Words in a Sentence:
Description: Write a program that counts the number of words in a given sentence.
Example:
Input: "Hello, how are you?"
Output: 4"""

string = "My, name is Sohit?"
count = 1
for i in string:
    if i == ' ':
        count = count+1
print(count)
