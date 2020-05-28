# main.py
import datetime as dt
import random


def today_message():
    now = dt.datetime.now()
    random.seed(now.year * 100 + now.month * 10 + now.day)
    activity = random.choice(
        [
            "fishing",
            "sleeping",
            "eating",
            "sports",
            "walking",
            "reading",
            "biking",
            "traveling",
            "gardening",
            "cleaning",
            "experimenting",
            "thinking",
            "cooking",
            "playing",
        ]
    )
    return f"Today is good for {activity}."


def main():
    print(today_message())


if __name__ == "__main__":
    main()
