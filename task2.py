from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


txt = input("Enter your txt:")
print(
    "1: Tokenize word 2: Tokenize sentence 3: original text  ")
Number = input("choose your number:")
if Number == "1":
    print(word_tokenize(txt))
elif Number == "2":
    print(sent_tokenize(txt))
elif Number == "3":
    print(txt)
else:
    print("This Number is not here")

# Dave Is A High School Student Who Likes To Study Maths