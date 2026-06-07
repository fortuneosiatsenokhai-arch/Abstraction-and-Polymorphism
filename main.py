class Ghana:
    def Accra(self):
        print("Accra is the capital city of ghana")
    def language (self):
        print("the most spoken language in ghana is Twi and Ga")

class England:
    def London(self):
        print("London is the capital city of England")
    def language(self):
            print("the most spoken language in England is english")

object1=Ghana()
object2=England()
for country in(object1,object2):
    country.language()