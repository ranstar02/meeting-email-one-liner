"""One hilarious line about a meeting that should have been an email.

The joke works because the punchline turns the complaint into the
crime: after an hour of everyone agreeing the meeting should have
been an email, the meeting's only output is scheduling a SECOND
meeting just to compose that email. The turn lands on "to write it"
— the email never gets written in this meeting, it just earns
another meeting. Anyone who has ever been trapped in a follow-up
meeting recognises it instantly.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "We spent an hour agreeing the meeting should've been an email \u2014 then booked a follow-up to write it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
