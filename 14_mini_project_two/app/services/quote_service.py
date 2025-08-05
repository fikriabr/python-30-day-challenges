from app.models.quote import Quote
import random

# Dummy Data
QUOTES = [
    Quote(1, "Stay hungry, stay foolish.", "Steve Jobs"),
    Quote(2, "Code is like humor. When you have to explain it, it’s bad.", "Cory House"),
    Quote(3, "First, solve the problem. Then, write the code.", "John Johnson"),
    Quote(4, "Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
    Quote(5, "In order to be irreplaceable, one must always be different.", "Coco Chanel"),
    Quote(6, "Simplicity is the soul of efficiency.", "Austin Freeman"),
    Quote(7, "The best way to predict the future is to invent it.", "Alan Kay"),
    Quote(8, "Do not be afraid of falling. Fear instead if you never try to climb.", "Buya Hamka"),
    Quote(9, "The only way to do great work is to love what you do.", "Steve Jobs"),
    Quote(10, "Knowledge will elevate you, but character will make people respect you.", "Buya Hamka")
]

def get_random_quote():
    return random.choice(QUOTES)