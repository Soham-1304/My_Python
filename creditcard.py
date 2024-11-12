
global card
def check(card):
    if (card.isdigit() and len(card)==12):
        return card
    if (card.isdigit()):
        pass 
    else:
        print("Enter Digits")
        card=input()
        return check(card)
    if(len(card)>12 or len(card)<12):
        print("Enter the Correct Length ")
        card=input ()
    return check(card)
    
print("enter the card number")
card=input ()
if len(card)>12 or len(card)<12 or (not card.isdigit()):
    card=check(card)
print (f"the card number is########{card[-4:]}")