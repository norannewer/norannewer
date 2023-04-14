from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

prstem = PorterStemmer()
sbstem = SnowballStemmer(language="english")
txt = input("Enter your txt:")
print(
    "1: Tokenize word 2: Tokenize sentence 3: original text  4.1: Porter stemmer 4.2: Snowball Stemmer"
)
Number = input("choose your number:")
if Number == "1":
    print(word_tokenize(txt))
elif Number == "2":
    print(sent_tokenize(txt))
elif Number == "3":
    print(txt)
elif Number == "4.1":
    print(prstem.stem(txt))
elif Number == "4.2":
    print(sbstem.stem(txt))
else:
    print("This Number is not here")

# Dave Is A High School Student Who Likes To Study Maths
