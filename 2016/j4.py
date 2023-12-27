from bisect import bisect_right
from datetime import datetime, timedelta

def is_in_rush_hour(h, m):
    return (
        (7, 0) <= (h, m) < (10, 0)
        or (15, 0) <= (h, m) < (19, 0)
    )

def find_next(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return a[0]

TIMES = [
    (7, 0),
    (10, 0),
    (15, 0),
    (19, 0),
]

hours, minutes = map(int, input().split(":"))
departure = datetime(2023, 1, 1, hours, minutes)

# CASE 1: depart during RH, arrive during RH
# There exists only one such case.
if (hours, minutes) == (15, 0):
    duration_minutes = 240

# CASE 2: depart during NH, span RH, arrive during NH
# There exists only one such case.
elif (hours, minutes) == (6, 40):
    duration_minutes = 210

elif not is_in_rush_hour(hours, minutes):

    # CASE 3: depart during NH, arrive during NH
    # We never reach RH, so the commute time remains 2 hours.
    if not is_in_rush_hour((hours + 2) % 24, minutes):
        duration_minutes = 120

    # CASE 4: depart during NH, arrive during RH
    # Notice such cases cannot cross midnight.
    else:
        next_rh_h, next_nh_m = find_next(TIMES, (hours, minutes))

        to_rh = (datetime(2023, 1, 1, next_rh_h, next_nh_m) - departure) / timedelta(minutes=1)
        remaining = 2 * (120 - to_rh)

        duration_minutes = to_rh + remaining

# CASE 5: depart during RH, arrive during NH
else:
    next_nh_h, next_nh_m = find_next(TIMES, (hours, minutes))

    to_nh = (datetime(2023, 1, 1, next_nh_h, next_nh_m) - departure) / timedelta(minutes=1)
    remaining = 120 - to_nh / 2

    duration_minutes = to_nh + remaining

duration = timedelta(minutes=duration_minutes)

arrival = departure + duration

print(f"{arrival.hour:02}:{arrival.minute:02}")


