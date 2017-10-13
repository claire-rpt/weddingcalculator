#application developed by managerclaire
def totalguests():
    guests_in = int(input("In-town guests invited: "))
    guests_out = int(input("Out-of-town guests invited: "))
    totalg = guests_in + guests_out
    attendance = .65*guests_out + .9*guests_in
    attendance = int(attendance)
    print("Approximately " + attendance + " guests will attend.")
    pct_attend = (float(attendance)/float(totalg))*100
    print("Your attendance rate will be about " + pct_attend + "%.")

totalguests()
