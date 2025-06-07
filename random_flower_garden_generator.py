from graphics import Canvas
import random
import math

CANVAS_WIDTH = 640
CANVAS_HEIGHT = 400
DOT_RADIUS = 15

VOWEL_COLORS = {
    'a': ['red', 'orange'],
    'e': ['yellow'],
    'i': ['#e6ffe6'],
    'o': ['skyblue'],
    'u': ['indigo', 'violet']
}

CONSONANT_COLORS = {
    'b': 'peachpuff',
    'c': 'cornflowerblue',
    'd': 'orchid',
    'f': 'salmon',
    'g': 'mediumseagreen',
    'h': 'deeppink',
    'j': 'limegreen',
    'k': 'plum',
    'l': 'lightcoral',
    'm': 'goldenrod',
    'n': 'seagreen',
    'p': 'mistyrose',
    'q': 'mediumorchid',
    'r': 'thistle',
    's': 'burlywood',
    't': 'aquamarine',
    'v': 'wheat',
    'w': 'cadetblue',
    'x': 'lightsteelblue',
    'y': 'mediumturquoise',
    'z': 'rosybrown'
}

def draw_flower(canvas, x, y, color):
    petal_width = DOT_RADIUS + random.uniform(2, 4)
    petal_height = DOT_RADIUS + random.uniform(6, 9)
    flower_radius = DOT_RADIUS * 1.5
    num_petals = 8

    for i in range(num_petals):
        angle = math.radians(i * (360 / num_petals) + random.uniform(-5, 5))
        offset_x = int(flower_radius * math.cos(angle))
        offset_y = int(flower_radius * math.sin(angle))
        canvas.create_oval(
            x + offset_x - petal_width / 2,
            y + offset_y - petal_height / 2,
            x + offset_x + petal_width / 2,
            y + offset_y + petal_height / 2,
            color
        )

    canvas.create_oval(
        x - DOT_RADIUS,
        y - DOT_RADIUS,
        x + DOT_RADIUS,
        y + DOT_RADIUS,
        color
    )


def draw_art(word):
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, '#ccffcc')
    word = word.lower()

    for letter in word:
        if letter in VOWEL_COLORS:
            color = random.choice(VOWEL_COLORS[letter])
        else:
            color = CONSONANT_COLORS.get(letter, 'gray')

        num_dots = random.randint(5, 10)
        for _ in range(num_dots):
            x = random.randint(0, CANVAS_WIDTH)
            y = random.randint(0, CANVAS_HEIGHT)

            if letter in VOWEL_COLORS:
                draw_flower(canvas, x, y, color)
            else:
                canvas.create_oval(
                    x - 0.5 * DOT_RADIUS,
                    y - 0.5 * DOT_RADIUS,
                    x + 0.5 * DOT_RADIUS,
                    y + 0.5 * DOT_RADIUS,
                    color
                )


def main():
    word = input("Enter a text to generate art. Long texts will likely cause longer generation time: ").strip()
    if word:
        draw_art(word)

main()
