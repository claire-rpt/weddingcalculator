#application developed by managerclaire
def logistics():
    #expects military time in hh:mm format
    ceremonystart = raw_input("Ceremony start time: ")
    return ceremonystart
    
def timeformat(time_var):
    militime = time_var
    hours, minutes = militime.split(":")
    hours, minutes = int(hours),int(minutes)
    setting = "AM"
    if hours >= 12:
        setting = "PM"
        if hours == 12:
            hours = 12
        else:
            hours -= 12
    time_f = ("%02d:%02d " + setting) % (hours, minutes)
    return time_f

def dayoftimeline_calc():
    ceremonystart = logistics()
    preceremony(ceremonystart)
    ceremonystart_f = timeformat(ceremonystart)
    print("Ceremony: " + ceremonystart_f)

def preceremony(ceremonyst):
    #durations in hours
    morning = float(input("How long will it to get ready for prep? "))
    if ceremonyst >= 9:
        breakfast = float(input("Breakfast duration: "))
    if ceremonyst >= 14:
        lunch = float(input("Lunch duration: "))
    else:
        lunch = 0
    makeup = float(input("Make up duration: "))
    hair = float(input("Hair duration: "))
    dressed = float(input("Getting dressed duration: "))
    travel = float(input("Travel time to ceremony: "))
    pictures (int("Enter 1 if you are taking pictures before the ceremony or 2 if you are not: "))
    if pictures == 1:
        shots = int(input("How many shot sets are being taken before the ceremony? "))
        shot_duration = shots*5
    else:
        shot_duration = 0
    if lunch == 0:
        pictures_t = ceremonyst-shot_duration
        travel_t = pictures_t-travel
        dressed_t = travel_t-dressed
        hair_t = dressed_t-hair
        makeup_t = hair_t-makeup
        breakfast_t = makeup_t-breakfast
        wakeup_t = breakfast_t-morning
        strwake = str(wakeup_t)
        
    
#dayoftimeline_calc()