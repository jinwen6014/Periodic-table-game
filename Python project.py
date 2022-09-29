import random

def main():
    """Start a periodic table game."""
    print("Guess the matter!")

    symbol = [
        "oxygen",
        "carbon",
        "neon",
        "potassium",
        "zinc",
        "silver",
        "gold",

        ]

    x = random.choice(symbol)
    if x == "oxygen":
        print("It is important to all living organism")
    elif x == "carbon":
        print("It is released when living organism exhale")
    elif x == "neon":
        print("Light gas")
    elif x == "potassium":
        print("Light silverry element")
    elif x == "zinc":
        print("Bluish-white metal")
    elif x == "silver":
        print("Shiny white metal")
    elif x == "gold":
        print("Olympian's Prize")
        
    
    guess = None

    while x != guess:

        guess = str(input("Guess the periodic table: "))
        
     
        if x == guess:
                 print ("congratulations! God bless you and you will got a prize!")
                 break
        else:
                 
            print("nope, sorry, try again!")

main()
