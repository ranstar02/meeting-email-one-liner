"""One hilarious line about a meeting that should have been an email.

The line: an hour of agreeing the meeting should have been an email,
and the meeting's only output is scheduling a SECOND meeting just to
write that email. The turn lands on the last two words, and anyone who
has ever been trapped in a follow-up meeting recognises it instantly.
"""

import os

LINE = "We spent an hour agreeing the meeting should've been an email \u2014 then booked a follow-up to write it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
