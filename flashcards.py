print("\033c")
class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return f"{self.word} ({self.meaning})"
flash = []
print("Welcome to flashcard maker")
while(True):
    word = input("Enter  the question you want in the flashcard : ")
    meaning = input("Enter the answer : ")
    flash.append( flashcard(word,meaning) )
    option = int(input("Enter 0 if you want to add another flashcard, otherwise enter 1 : "))
    if(option):
        break
print("\nYour Flashcard is ready")
for i in flash:
    print(">",i  )
