#Program for Implementaing all week days
#MatchCaseEx4.py
wkd=input("Enter the week Name:")
match(wkd.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"MON"|"TUE"|"WED"|"THU"|"FRI":
        print("{} is working Day".format(wkd))
    case "SATURDAY"|"SAT":
        print("{} is Week End".format(wkd))
    case "SUNDAY"|"SUN":
        print("{} is HolyDay".format(wkd))
    case _:
        print("{} is not week day".format(wkd))




