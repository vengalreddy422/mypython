#Program for Implementaing all week days
#MatchCaseEx3.py
wkd=input("Enter the week Name:")
match(wkd.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is working Day".format(wkd))
    case "SATURDAY":
        print("{} is Week End".format(wkd))
    case "SUNDAY":
        print("{} is HolyDay".format(wkd))
    case _:
        print("{} is not week day".format(wkd))




