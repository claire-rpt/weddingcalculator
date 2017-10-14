#application developed by managerclaire to test out ceremony time scenarios
def consistent():
    print("All times should be entered in minutes.")
    gu_valid = False
    b_valid = False
    h_valid = False
    m_valid = False
    d_valid = False
    dtc_valid = False
    precs_valid = False
    c_valid = False
    postcs_valid = False
    dtr_valid = False
    r_valid = False
    while gu_valid == False:
        try:
            gettingup = int(input("How long will it take to get up in the morning? "))
            gu_valid = True
        except ValueError:
            gu_valid = False
    while b_valid == False:
        try:
            breakfast = int(input("How long will eating breakfast take? "))
            b_valid = True
        except ValueError:
            b_valid = False
    while h_valid == False:
        try:
            hair = int(input("How long will hair take? "))
            h_valid = True
        except ValueError:
            h_valid = False
    while m_valid == False:
        try:
            makeup = int(input("How long will makeup take? "))
            m_valid = True
        except ValueError:
            m_valid = False
    while d_valid == False:
        try:
            dress = int(input("How long will getting dressed take? "))
            d_valid = True
        except ValueError:
            d_valid = False
    while dtc_valid == False:
        try:
            drive_to_ceremony = int(input("How long will the drive to the ceremony take? "))
            dtc_valid = True
        except ValueError:
            dtc_valid = False
    while precs_valid == False:
        try:
            preceremony_shots = int(input("How many pre-ceremony pictures do you want to take? "))
            precs_valid = True
        except ValueError:
            precs_valid = False
    preceremony_picture_time = preceremony_shots*5
    while c_valid == False:
        try:
            ceremony = int(input("How long will the ceremony take? "))
            c_valid = True
        except ValueError:
            c_valid = False
    while postcs_valid == False:
        try:
            postceremony_shots = int(input("How many post-ceremony pictures do you want to take? "))
            postcs_valid = True
        except ValueError:
            postcs_valid = False
    postceremony_picture_time = postceremony_shots*5
    while dtr_valid == False:
        try:
            drive_to_reception = int(input("How long will the drive to the reception take? "))
            dtr_valid = True
        except ValueError:
            dtr_valid = False
    while r_valid == False:
        try:
            reception = int(input("How long will the reception be? "))
            r_valid = True
        except ValueError:
            r_valid = False
    preceremony_duration = gettingup + breakfast + hair + makeup + dress + drive_to_ceremony + preceremony_picture_time
    postceremony_duration = postceremony_picture_time + drive_to_reception
    ceremony_variable(preceremony_duration,ceremony,postceremony_duration,reception)

def ceremony_variable(preceremony,ceremony,postceremony,reception):
    #ceremony start time in military
    a_valid = False
    ceremonystart = input("Ceremony start time: ")
    ceremonystart = time_handle(ceremonystart,preceremony,ceremony,postceremony,reception)
    wakeup = ceremonystart - preceremony
    leave = ceremonystart + ceremony + postceremony + reception
    wakeup = time_format(wakeup)
    leave = time_format(leave)
    print("Wake up at " + wakeup + ".")
    print("Reception ends at " + leave + ".")
    while a_valid == False:
        try:
            acceptable = int(input("Enter 1 to end application or 2 to try the scenario again: "))
            if acceptable == 1:
                a_valid = True
                return
            elif acceptable == 2:
                a_valid = True
                ceremony_variable(preceremony,ceremony,postceremony,reception)
        except ValueError:
            a_valid = False

def time_handle(time_var,preceremony,ceremony,postceremony,reception):
    h_valid = False
    m_valid = False
    militime = time_var
    hours, minutes = militime.split(":")
    while h_valid == False:
        try:
            hours = int(hours)
            if hours <= 24:
                h_valid = True
            else:
                ceremony_variable(preceremony,ceremony,postceremony,reception)
        except ValueError:
            ceremony_variable(preceremony,ceremony,postceremony,reception)
    while m_valid == False:
        try:
            minutes = int(minutes)
            if minutes <60:
                m_valid = True
            else:
                ceremony_variable(preceremony,ceremony,postceremony,reception)
        except ValueError:
            ceremony_variable(preceremony,ceremony,postceremony,reception)
    time_value = hours*60 + minutes
    return time_value

def time_format(time_var):
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

consistent()