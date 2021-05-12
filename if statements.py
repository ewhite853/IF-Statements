# Elliot White 05/02.2021
# Using IF... Statements

# Display splash message
print("***Welcome to H. Wenleydale chhes Emporium***")
print("would you like some cheese?")

# Get user input
wantsCheese = input("Enter (y)es, (m)aybe or (n)o: ")

if wantsCheese == "y":
    print("Camembert?")
    wantsCamembert = input("Enter (y)es or (n)o ")
    if wantsCambert == "y":
        print("Sorry, the cats eaten it...")
    else:
        print("Thats good, the cats eaten it...")
elif wantsCheese:
    print("Well, enjoy the music while you decide...")
else:
    print("Thats good, we dont have any")
