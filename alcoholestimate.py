#application developed by managerclaire
def alcoholestimate():
    estguest = int(input("Expected guests: "))
    underage = int(input("Guests under 21: "))
    overage = estguest - underage
    ampm = int(input("Enter 1 if your reception starts before noon or 2 if it starts after: "))
    #wedtime expects integer, morning/afternoon handled by ampm
    wedtime = int(input("Reception start time: "))
    alcstat = int(input("Enter 1 if you are serving beer and wine or 2 if having a full bar: "))
    #dur expects duration in integer
    dur = int(input("Length of reception: "))
    if alcstat == 1:
        beerwine(overage,ampm,wedtime,dur)
    elif alcstat == 2:
        fullbar(overage,ampm,wedtime,dur)
    else:
        print("Error")
        return

def beerwine(overage,ampm,wedtime,dur):
    if ampm == 1:
        servings = overage
    elif ampm == 2:
        if wedtime <= 4:
            servings = overage*(dur/2)
        else:
            servings = overage*dur
    beerservings = servings*.25
    wineservings = servings*.75
    beertotal = int(beerservings)
    winetotal = int(wineservings/4)
    print("You will need {} bottles of beer.".format(beertotal))
    print("You will need {} bottles of wine.".format(winetotal))

def fullbar(overage,ampm,wedtime,dur):
    if ampm == 1:
        servings = overage
    elif ampm == 2:
        if wedtime <= 4:
            servings = overage*(dur/2)
        else:
            servings = overage*dur
    beerservings = servings*.2
    wineservings = servings*.5
    liquorservings = servings*.3
    beertotal = int(beerservings)
    winetotal = int(wineservings/4)
    liquortotal = int(liquorservings/18)
    print("You will need {} bottles of beer.".format(beertotal))
    print("You will need {} bottles of wine.".format(winetotal))
    print("You will need {} bottles of liquour.".format(liquortotal))

alcoholestimate()