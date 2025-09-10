# A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:
# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.
def li():
    day1=["adhsgH","fgffG"]
    day2=["adhsgH"]
    day3=["adhsgH"]
    for i in range(len(day1)):
        day1[i]=day1[i].lower()
    s1=set(day1)
    for i in range(len(day2)):
        day2[i]=day2[i].lower()
    s2=set(day2)
    for i in range(len(day3)):
        day3[i]=day3[i].lower()
    s3=set(day3)
    print("unique members are ",s1|s2|s3)
    print("attendees who attended all three days",list(s1&s2&s3))
    print("Exactly on day",list(s1^s2^s3))
    print("pairwise overlap counts",list(s1&s2,s2&s3,s3&s1))

li()

