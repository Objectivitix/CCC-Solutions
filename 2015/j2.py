message = input()

happy = message.count(":-)")
sad = message.count(":-(")

print(
    "none" if happy == 0 and sad == 0 else
    "unsure" if happy == sad else
    "happy" if happy > sad else
    "sad"
)
