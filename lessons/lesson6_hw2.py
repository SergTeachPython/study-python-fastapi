sec_value = int(input("input value seconds from 0 to 8640000: "))
if 0 <= sec_value <= 8640000:
    days = sec_value // 86400
    rest = sec_value % 86400
    hours = rest // 3600
    rest %= 3600
    minutes = rest // 60
    sec = rest % 60

    last_word = days % 10
    if 2 <= last_word <= 4 and not 12<= days <= 14:
        days_word = " дні, "
    elif last_word == 1 and days != 11:
        days_word = " день, "
    else:
        days_word = " днів, "

    result = str(days) + days_word + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(sec).zfill(2)
    print(result)
else:
    print("Second value should be between 0 and 8640000")
