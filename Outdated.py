import re                                                               #   import librery to read paterns
from Date_Data import month_for_Outdated, dates_for_Outdated            #   import date and month dictionary


def main():
    while True:                                #    initiate while loop for rpeat ask to user date if input will be wrong
        user = input("Date: ")                 #    get user input
        user = formatedText(user)              #    send user text to format
        if checkPattern(user) == 1:            #    check user input by pattern 1
            print(datebyPattern1(user))        #    get result and break loop
            break
        elif checkPattern(user) == 2:          #    check user input by pattern 2
            print(datebyPattern2(user))        #    get result and break loop
            break
        elif checkPattern(user) == 3:          #    check user input by pattern 3
            print(datebyPattern3(user))        #    get result and break loop
            break
        elif checkPattern(user) == False:      #    check if any pattern is not matched to user input return to biginning and ask new date again
            continue


def formatedText(txt):
    txt = txt.lower().strip()
    return txt


def checkPattern(txt):                                              #   function for detect specified pattern and got the format
    #   pattern for detect date format like d/m/yyyy dd/mm/yyyy d.m.yyyy dd.mm.yyyy d-m-yyyy dd-mm-yyyy
    pattern = (r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
    #   pattern for detect date format like mmmm d, yyyy mmmm d. yyyy
    pattern2 = (r"^[a-z]+\s(0?[1-9]|[12][0-9]|3[01])(\.|,|\s)\s[0-9]+$")
    #   pattern for detect date format like dd-mmm-yyyy dd.mmm.yyyy dd.mmmm.yyyy d.mmmm.yyyy
    pattern3 = (r"^(([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|\s)(jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august|sep|september|oct|october|nov|november|dec|december)(\.|-|\s)((19|20)\d{2}))$")
    if re.compile(pattern).search(txt):                             #   if matches on pattern 1 return 1
        return 1
    elif re.compile(pattern2).search(txt):                          #   if matches on pattern 2 return 2
        return 2
    elif re.compile(pattern3).search(txt):                          #   if matches on pattern 3 return 3
        return 3
    else:
        return False                                                #   in else case return false


def datebyPattern1(txt):                            #   edit user text if it is for pattern 1
    delimiters = "/.-"                              #   take all possible non number symbols for pattern 1
    delimiter = ""                                  #   initiate blank string
    for i in txt:                                   #   run for loop for identify what non number symbol is in users string
        if i in delimiters:
            delimiter = i                           #   get non number symbol as string delimiter
    txt = txt.split(delimiter)                      #   split text by delimiter
    date=[]                                         #   get empty list
    date.append(txt[2])                             #   append year
    if txt[1] in dates_for_Outdated():              #   check month number
        date.append(dates_for_Outdated()[txt[1]])   #   if month number is less then 10 and it is without 0 take month value from dictionary and append
    else:
        date.append(txt[1])                         #   else append month
    if txt[0] in dates_for_Outdated():              #   if day number is less then 10 and it is without 0 take day value from dictionary and append
        date.append(dates_for_Outdated()[txt[0]])
    else:
        date.append(txt[0])                         #   else append month
    return "-".join(date)                           #   return final result


def datebyPattern2(txt):
    delimiters = "/.-,"
    for i in delimiters:
        if i in txt:
            txt = txt.replace(i,"")
    txt = txt.split()
    date=[]
    date.append(txt[2])
    date.append(month_for_Outdated()[txt[0]])
    if txt[1] in dates_for_Outdated():
        date.append(dates_for_Outdated()[txt[1]])
    else:
        date.append(txt[1])
    return "-".join(date)


def datebyPattern3(txt):
    delimiters = "/.-, "
    for i in delimiters:
        if i in txt:
            txt = txt.replace(i,")")
    txt = txt.split(")")
    date=[]
    date.append(txt[2])
    date.append(month_for_Outdated()[txt[1]])
    if txt[0] in dates_for_Outdated():
        date.append(dates_for_Outdated()[txt[0]])
    else:
        date.append(txt[0])
    return "-".join(date)


if __name__ == "__main__":
    main()
