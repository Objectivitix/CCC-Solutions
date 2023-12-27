from collections import defaultdict

m = int(input())
stream = (
    tuple(input().split())
    for _ in range(m)
)

messages_pending = {}
curr_msg_receipt_times = {}
wait_times = defaultdict(list)
clock = 0

for cmd, value in stream:
    wait = False

    if cmd == "R":
        messages_pending[value] = True
        curr_msg_receipt_times[value] = clock
    elif cmd == "S":
        messages_pending[value] = False
        wait_times[value].append(clock - curr_msg_receipt_times[value])
    elif cmd == "W":
        wait = True
        clock += int(value) - 1

    if not wait:
        clock += 1

for friend_id, message_pending in messages_pending.items():
    if message_pending:
        wait_times[friend_id].append(float("inf"))

wait_times_sorted = sorted(
    (int(friend_id), sum(wait_times))
    for friend_id, wait_times in wait_times.items()
)

for friend_id, total_wait_time in wait_times_sorted:
    if total_wait_time == float("inf"):
        total_wait_time = -1

    print(friend_id, total_wait_time)
