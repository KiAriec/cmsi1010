import random
import re


templates = [
    {"text": "The :color :animal :action over the :adjective :plant.", "author": "A. L. Harper"},
    {"text": "At dawn, the :adjective :profession woke up and :verb with a :noun.", "author": "M. Rivera"},
    {"text": "A :adjective :creature stole my :noun and hid it in the :place.", "author": "T. Brooks"},
    {"text": "Our :adjective spaceship is :verb through the :place with a :color :object.", "author": "N. Patel"},
    {"text": "The :animal in the :place sang :adverb while eating :food.", "author": "L. Nguyen"},
    {"text": "During the :adjective storm, a :character :verb under the :object.", "author": "C. Morris"},
    {"text": "My :adjective robot loves to :verb on the :place every :day.", "author": "J. Alvarez"},
    {"text": "The :color dragon was :adverb :verb across the :adjective :place.", "author": "R. Kim"},
    {"text": "A :noun by the :place made the :animal :verb when the :color moon rose.", "author": "S. Lee"},
    {"text": "The :adjective wizard whispered a secret to the :animal and then :verb.", "author": "E. Ross"},
    {"text": "On the :adjective island, the :profession discovered a :color :object.", "author": "D. Bennett"},
    {"text": "The :animal with the :adjective hat decided to :verb in the :place.", "author": "F. Hassan"},
]

yes_answers = {
    "yes", "y", "yeah", "yep", "sure", "ok", "okay", "affirmative",
    "si", "sí", "oui", "ja", "yea", "certainly", "absolutely"
}


def get_word(prompt_text):
    while True:
        answer = input(prompt_text).strip()
        if 1 <= len(answer) <= 30:
            return answer
        print("Please enter a word between 1 and 30 characters long.")


def fill_template(template_text):
    placeholders = re.findall(r":([A-Za-z_]+)", template_text)
    values = {}
    for placeholder in placeholders:
        values[placeholder] = get_word(f"Enter a word for '{placeholder}': ")
    return re.sub(r":([A-Za-z_]+)", lambda match: values[match.group(1)], template_text)


while True:
    current_template = random.choice(templates)
    completed_story = fill_template(current_template["text"])
    print("\n" + completed_story)
    print()
    print(f"Author: {current_template['author']}")
    print()
    print()
    again = input("Want to play again? ").strip().lower()
    if again not in yes_answers:
        print("No")
        print("Thanks for playing!")
        break
