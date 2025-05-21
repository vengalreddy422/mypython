#Program for Implementaing all week days
#MatchCaseEx2.py
wkd=input("Enter the week Name:")
match(wkd):
    case "MONDAY":
        print("{} is working".format(wkd))
    case "TUESDAY":
        print("{} is working".format(wkd))
    case "WEDNESDAY":
        print("{} is working".format(wkd))
    case "THURSDAY":
        print("{} is working".format(wkd))
    case "FRIDAY":
        print("{} is working".format(wkd))
    case "SATURDAY":
        print("{} is Week End".format(wkd))
    case "SUNDAY":
        print("{} is HolyDay".format(wkd))
    case _:
        print("{} is not week day".format(wkd))




