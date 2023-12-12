day_mapping = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

day_names = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def add_time(start_time, duration, specified_day=""):
    [start_hours, start_minutes] = parse_time(start_time)
    [duration_hours, duration_minutes] = parse_duration(duration)

    total_minutes = start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes

    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    am_pm_indicator = "AM"

    days_later = new_hours // 24
    new_hours %= 24

    if new_hours > 12:
        new_hours %= 12
        am_pm_indicator = "PM"

    if new_hours == 12:
        am_pm_indicator = "PM"

    if new_hours == 0:
        new_hours = 12
        am_pm_indicator = "AM"

    if specified_day == "":
        if days_later == 0:
            return "{}:{:02d} {}".format(new_hours, new_minutes, am_pm_indicator)
        elif days_later == 1:
            return "{}:{:02d} {} (next day)".format(new_hours, new_minutes, am_pm_indicator)
        else:
            return "{}:{:02d} {} ({} days later)".format(new_hours, new_minutes, am_pm_indicator, days_later)
    else:
        specified_day = specified_day.lower()
        specified_day = specified_day[0].upper() + specified_day[1:]
        end_day = day_names[(day_mapping[specified_day] + days_later) % 7]

        if days_later == 0:
            return "{}:{:02d} {}, {}".format(new_hours, new_minutes, am_pm_indicator, end_day)
        elif days_later == 1:
            return "{}:{:02d} {}, {} (next day)".format(new_hours, new_minutes, am_pm_indicator, end_day)
        else:
            return "{}:{:02d} {}, {} ({} days later)".format(new_hours, new_minutes, am_pm_indicator, end_day, days_later)

def parse_time(time_str):
    [time, am_pm] = time_str.split()
    [hours, minutes] = parse_duration(time)
    if am_pm != 'AM':
        hours += 12
    return [hours, minutes]

def parse_duration(duration_str):
    return map(lambda s: int(s), duration_str.split(":"))
