import numpy as np
from enum import Enum

CRED = '\033[91m'
CEND = '\033[0m'
print(f'{CRED}I am __Xx_LIMDestroyer69_xX__ and I am here to Destroy you!{CEND}')
class Cards(Enum):
    A = {'card': 1, 'value': [1,11]}
    TWO = {'card': 2, 'value': [2]}
    THREE = {'card': 3, 'value': [3]}
    FOUR = {'card': 4, 'value': [4]}
    FIVE = {'card': 5, 'value': [5]}
    SIX = {'card': 6, 'value': [6]}
    SEVEN = {'card': 7, 'value': [7]}
    EIGHT = {'card': 8, 'value': [8]}
    NINE = {'card': 9, 'value': [9]}
    TEN = {'card': 10, 'value': [10]}
    J = {'card': 11, 'value': [10]}
    Q = {'card': 12, 'value': [10]}
    K = {'card': 13, 'value': [10]}


def __getitem__(self, item):
    return self._data['value']

def cards(card):
    #match the card name string to the enum
    return [Cards[x.upper()] for x in card] if isinstance(card, list) else Cards[card.upper()]
#input number of decks being played on the game
while True:
    numofdecks = int(input("Number of decks being used on this game: ")) 
    if numofdecks in [1,2,4,6,8]:
        break


deck = {
    Cards.A: 4*numofdecks,
    Cards.TWO: 4*numofdecks,
    Cards.THREE: 4*numofdecks,
    Cards.FOUR: 4*numofdecks,
    Cards.FIVE: 4*numofdecks,
    Cards.SIX: 4*numofdecks,
    Cards.SEVEN: 4*numofdecks,
    Cards.EIGHT: 4*numofdecks,
    Cards.NINE: 4*numofdecks,
    Cards.TEN: 4*numofdecks,
    Cards.J: 4*numofdecks,
    Cards.Q: 4*numofdecks,
    Cards.K: 4*numofdecks
}


#number of cards in the deck
numofcards = numofdecks * 52
#running count
count = 0
that=0
#track cards that were previusly played on the game
yourhand = []
yourcount=0
yourparts = 0
dealershand = []
dealercount=0


# Start with a count of 0
# When you see an A, K, Q, J, or 10: Subtract 1 from your running count
# When you see a 9: Subtract - 0.5 from your running count
# When you see an 8: Do nothing(Worth 0)
# When you see a 2 or 7: Add 0.5 to your running count
# When you see a 3, 4, 5, or 6: Add 1 to your running count

# def cardcount(dealt,cnt):
#     decksLeft=0
    # if numofcards <= 52:
    #     decksLeft = 1
    # else:
        #decksLeft = int((numofcards / 52))
    # if dealt == Cards.TWO or dealt == Cards.SEVEN:
    #     cnt += 0.5
    # elif dealt == Cards.THREE or dealt == Cards.FOUR or dealt == Cards.SIX:
    #     cnt += 1
    # elif dealt == Cards.FIVE:
    #     cnt += 1.5
    # elif dealt == Cards.NINE:
    #     cnt -= 0.5
    # elif dealt == Cards.A or dealt == Cards.TEN or dealt == Cards.J or dealt == Cards.Q or dealt == Cards.K:
    #     cnt -= 1
    # return float(cnt)/float(decksLeft),cnt

def dothathing(urcount):
    total=0
    parts={}
    for x in deck:
        if x.value["value"][0] <= 21-urcount:
            parts.update({x:(deck[x]/numofcards)*100})
            print(f"| {x.name},{round(parts[x],2)}% |", end="")
            total+=deck[x]
    parts.update({'global':(total/numofcards)*100})
    
    print(f"Total number of viable Cards left {total},{ round(parts['global'],2)}%")
    return parts

def doTheSplit (yourhandz):
    if yourhandz[0] == yourhandz[1]:
        if yourhandz[0] == Cards.A or yourhandz[0] == Cards.EIGHT:
            print("Split That BITCH")
            return True
    return False

def doThatBet(cardcnt):
    if cardcnt >= 2:
        print("BET THE MAX-20")
    elif cardcnt >= 3:
        print("BET THE MAX")
    else:
        print("BET 2 GreenBacks")
def doThatMove(partz,cardcnt):
    return partz['global'] >= 50

def doubleThatDown(urhand, dealerzhand, cardcnt):
    if(dealerzhand==Cards.A): return
    
    urcount=sum([x.value["value"][0] for x in yourhand])
    highcount = sum([x.value["value"][len(x.value["value"])-1] for x in yourhand])
    #change the cardcnt to % based on having a sum > 18 [7,8,9,10,J,Q,K]
    #fix the loop
    if((urcount == 11 or highcount==11) and cardcnt >= 2):
        print("DOUBLE DOWN")
    if (len([x for x in urhand if x == Cards.A]) != 0 and highcount>=16 and highcount<=17):
        print("DOUBLE DOWN!")
    
    
        
    
#update the deck with the cards drawn
def updatedeck(cards):
    global numofcards
    if isinstance(cards, list):
        numofcards-=len(cards)
        for x in cards:
            deck[x]-=1
            if deck[x]<0:print(f"{CRED}WARNING: {x.name} is less than 0{CEND}")
    else:
        numofcards-=1
        deck[cards]-=1
        if deck[cards]<0:print(f"{CRED}WARNING: {cards.name} is less than 0{CEND}")
      
    print(f"Number of Cards left {numofcards}")

while True: #Round Loop
    doThatBet(that)
    while True: #input error check
        temp = input("Initial User Cards: ").split()
        
        if(all(x in [member.name for member in Cards] for x in temp)):
            yourhand=cards(temp)
            break
    updatedeck(yourhand)
    # for x in yourhand:
    #     that,count=cardcount(x,count)
    yourcount=sum([x.value["value"][0] for x in yourhand])
    if (yourcount == 21 or sum([x.value["value"][len(x.value["value"])-1]for x in yourhand])==21):
        print("WE WIN")
        continue

    other=[]
    while True:   #input error check
        temp = input("Other Cards: ").split()
        if(all(x in [member.name for member in Cards] for x in temp)):
            other=cards(temp)
            break
    
    updatedeck(other)
    # for x in other:
    #     that,count=cardcount(x,count)

    while True:   #input error check
        temp= input("Initial Dealer Card: ")
        if temp in [member.name for member in Cards]:
            dealershand=[cards(temp)]
            break
    updatedeck(dealershand)
    # for x in dealershand:
    #     that, count = cardcount(x, count)
    dealercount = sum([x.value["value"][0] for x in dealershand])

    yourparts = dothathing(yourcount)
    doubleThatDown(yourhand,dealershand,that)
    Split=doTheSplit(yourhand)
    if(Split):
        Splithand=[yourhand[0]]
        Splitcount = sum([x.value["value"][0] for x in Splithand])
        Splitparts = dothathing(Splitcount)
        yourhand=[yourhand[0]]
        yourcount = sum([x.value["value"][0] for x in yourhand])
        yourparts = dothathing(yourcount)
    # print(f"The advantage we have is {that}")
    # cardcount(dealt)
    while doThatMove(yourparts, that) and yourcount < 21 and sum([x.value["value"][len(x.value["value"])-1] for x in yourhand]) < 17:
        print("hit")
        while True:  # input error check
            temp = input("Your Card: ")
            if temp in [member.name for member in Cards]:
                temp = cards(temp)
                break
            
        updatedeck(temp)
        # that,count=cardcount(temp,count)
        yourhand+=[temp]
        yourcount=sum([x.value["value"][0] for x in yourhand])
        yourparts = dothathing(yourcount)
    print('stand')
    if (Split):
        while doThatMove(Splitparts, that) and Splitcount<21 and sum([x.value["value"][len(x.value["value"])-1] for x in Splithand])<17:
            print("hit")
            while True:  # input error check
                temp = input("Your Other Card: ")
                if temp in [member.name for member in Cards]:
                    temp = cards(temp)
                    break

            updatedeck(temp)
            #that, count = cardcount(temp, count)
            Splithand += [temp]
            Splitcount = sum([x.value["value"][0] for x in Splithand])
            Splitparts = dothathing(Splitcount)
        print('stand')
    other = []
    while True:  # input error check
        temp = input("Other Cards: ").split()
        if (all(x in [member.name for member in Cards] for x in temp)):
            other = cards(temp)
            break

    updatedeck(other)
    # for x in other:
    #     that, count = cardcount(x, count)

    while True:  # input error check
        temp = input("Dealer Cards: ").split()
        if (all(x in [member.name for member in Cards] for x in temp)):
            dealershand += cards(temp)
            break

    updatedeck(dealershand)
    # for x in dealershand:
    #     that, count = cardcount(x, count)
    dealercount = sum([x.value["value"][0] for x in dealershand])

    print("First hand: ",end="")
    highcount = sum([x.value["value"][len(x.value["value"])-1]for x in yourhand])
    if yourcount == 21 or highcount == 21:
        print("haha I won, be gone loser")
    elif (yourcount > dealercount and yourcount < 21) or (highcount > dealercount and highcount < 21):
        print("I WOOOOOOOOOON _x69x_")
    elif yourcount == dealercount or highcount == dealercount:
        print("Tie like a shoelace")
    else:
        print("shit Ive busted")
    
    if(Split):
        highcount = sum([x.value["value"][len(x.value["value"])-1]for x in Splithand])
        print("Second hand: ", end="")
        if Splitcount == 21 or highcount == 21:
            print("haha I won, be gone loser")
        elif (Splitcount > dealercount and Splitcount < 21) or (highcount > dealercount and highcount < 21):
            print("I WOOOOOOOOOON _x69x_")
        elif Splitcount == dealercount or highcount == dealercount:
            print("Tie like a shoelace")
        else:
            print("shit Ive busted")

        
        