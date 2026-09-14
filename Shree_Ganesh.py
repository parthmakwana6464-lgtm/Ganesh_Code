from PIL import Image
import turtle
import random
import time

PHRASE = [
    "ॐ",
    "गं",
    "ग",
    "ण",
    "प",
    "त",
    "ये",
    "न",
    "मो",
    "न",
    "मः"
]

image = Image.open("Picture/ganesha.png").convert("L")

# Change this to make the artwork more/less detailed
width = 120

height = int(image.height * width / image.width)

image = image.resize((width, height))
threshold = 150

# Store only the DARK pixels.
pixels = []

for y in range(height):

    for x in range(width):

        pixel = image.getpixel((x, y))

        if pixel < threshold:
            pixels.append((x, y))

screen = turtle.Screen()

screen.setup(
    width=900,
    height=900
)

screen.bgcolor("black")
screen.title("ॐ गणपत्ये नमः")


screen.tracer(0, 0)

t = turtle.Turtle()

t.hideturtle()
t.penup()

# White text
t.color("white")


# ============================================================
# CHARACTER SIZE
# ============================================================

# Increase this if the artwork looks too small.
# Decrease it if characters overlap.

PIXEL_SIZE = 5

start_x = -(width * PIXEL_SIZE) / 2
start_y = (height * PIXEL_SIZE) / 2


# ============================================================
# ANIMATION SPEED
# ============================================================
#
# THIS IS THE MAIN SPEED CONTROL.
#
# Smaller number = FASTER animation
# Larger number  = SLOWER animation
#
# Try:
#
# 0.001  → extremely fast
# 0.003  → very fast
# 0.005  → fast
# 0.010  → normal
# 0.020  → slow
#
# ============================================================

ANIMATION_DELAY = 0.020
PIXELS_PER_FRAME = 8


def draw_animation():

    t.clear()

    pixels_to_draw = pixels.copy()
    random.shuffle(pixels_to_draw)
    for i in range(0, len(pixels_to_draw), PIXELS_PER_FRAME):


        for x, y in pixels_to_draw[i:i + PIXELS_PER_FRAME]:

            pos_x = start_x + x * PIXEL_SIZE
            pos_y = start_y - y * PIXEL_SIZE

            t.goto(pos_x, pos_y)         
            character = random.choice(PHRASE)
            t.write(
                character,
                align="center",
                font=("Noto Sans Devanagari", 8, "normal")
            )

        screen.update()

        time.sleep(ANIMATION_DELAY)

def replay(x, y):
    draw_animation()

screen.onclick(replay)

draw_animation()

screen.mainloop()
