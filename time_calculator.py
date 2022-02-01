def add_time(start, duration, day="none"):
    # x is list of time and period ex: [2:40,AM] -> assign to variable
    x = start.split()
    start_ = x[0]
    period = x[1]

    # splitting the time (2:00), etc..
    start__list = start_.split(":")
    duration_list = duration.split(":")
    # add hour and minutes
    new_hour = int(start__list[0]) + int(duration_list[0])
    new_min = int(start__list[1]) + int(duration_list[1])

    # re calculate time
    while new_min >= 60:
        new_min = new_min - 60
        new_hour = new_hour + 1
    # days passed
    days_passed = 0
    while new_hour >= 12:
        new_hour -= 12
        if period == "AM":
            period = "PM"
            continue
        if period == 'PM':
            period = "AM"
            days_passed += 1

    if day != "none":
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = 0
        for _ in days:
            if day.lower() == _.lower():
                index = days.index(_) + days_passed
        while index > 6:
            index -= 7
        day = days[index]

    # string stuff-----------------------------------------
    if int(new_min) < 10:
        new_min = "0" + str(new_min)[0:]
    if int(new_hour) == 0:
        new_hour = "12"

    new_time = None
    # without day
    if days_passed > 0 and day == "none":
        if days_passed == 1:
            new_time = str(new_hour) + ":" + str(new_min) + " " + \
                       period + " (next day)"
        else:
            new_time = str(new_hour) + ":" + str(new_min) + " " + \
                       period + " (" + str(days_passed) + ' days later)'
    elif days_passed == 0 and day == "none":
        new_time = str(new_hour) + ":" + str(new_min) + " " + \
                   period
    # with day
    elif days_passed > 0 and day != "none":
        if days_passed == 1:
            new_time = str(new_hour) + ":" + str(new_min) + " " + \
                       period + ", " + str(day) + " (next day)"
        else:
            new_time = str(new_hour) + ":" + str(new_min) + " " + \
                       period + ", " + str(day) + " (" + str(days_passed) + ' days later)'
    elif days_passed == 0 and day != "none":
        new_time = str(new_hour) + ":" + str(new_min) + " " + \
                   period + ", " + str(day)

    return new_time
