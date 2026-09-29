import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize
text="hello i am the student.i am in it.i am in srmcem."

tokens= sent_tokenize(text)

print("Tokens are")
print(tokens)