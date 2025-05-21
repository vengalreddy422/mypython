#Program for Implementaing all week days
#MatchCaseEx4.py
wkd=input("Enter the week Name:").strip()
if(wkd.upper() in ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY",
                   "SATURDAY","SUNDAY","MON","TUE","WED","THU",
                   "FRI","SAT","SUN"]):
    match(wkd.upper()[0:3]):
        case "MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is working Day".format(wkd))
        case "SATURDAY"|"SAT":
            print("{} is Week End".format(wkd))
        case "SUNDAY"|"SUN":
            print("{} is HolyDay".format(wkd))
else:
    print("{} is not week day".format(wkd))





