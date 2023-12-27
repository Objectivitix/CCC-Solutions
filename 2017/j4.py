from bisect import bisect_left
from datetime import datetime, timedelta

ARITHMETIC_SEQUENCE_TIMES_LIST = [
    (0, 34),
    (1, 11),
    (1, 23),
    (1, 35),
    (1, 47),
    (1, 59),
    (2, 10),
    (2, 22),
    (2, 34),
    (2, 46),
    (2, 58),
    (3, 21),
    (3, 33),
    (3, 45),
    (3, 57),
    (4, 20),
    (4, 32),
    (4, 44),
    (4, 56),
    (5, 31),
    (5, 43),
    (5, 55),
    (6, 30),
    (6, 42),
    (6, 54),
    (7, 41),
    (7, 53),
    (8, 40),
    (8, 52),
    (9, 51),
    (11, 11),
]

ARITHMETIC_SEQUENCE_TIMES_IN_12_HOURS = len(
    ARITHMETIC_SEQUENCE_TIMES_LIST
)

ARITHMETIC_SEQUENCE_TIMES_SET = set(
    ARITHMETIC_SEQUENCE_TIMES_LIST
)

# 24-hour clock initialized at 12:00. Date is irrelevant.
# We're only using a datetime object because it supports
# operations with timedelta objects.

NOON = datetime(2017, 1, 1, 12, 0)

d = int(input())

new_time = NOON + timedelta(minutes=d)
new_hour = new_time.hour % 12
new_minute = new_time.minute

ans = 0

# full 12-hour (720-minute) periods passed
ans += (d // 720) * ARITHMETIC_SEQUENCE_TIMES_IN_12_HOURS

# remaining times
ans += bisect_left(ARITHMETIC_SEQUENCE_TIMES_LIST, (new_hour, new_minute))

if (new_hour, new_minute) in ARITHMETIC_SEQUENCE_TIMES_SET:
    ans += 1  # account for end

print(ans)
