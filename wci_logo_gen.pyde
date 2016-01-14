import random

# Defines a SIZE x SIZE square canvas
# Note: SIZE must be a multiple of both COLS and ROWS
SIZE = 180
COLS = 3
ROWS = 6

# Defines the weights of colors to be generated (white, blue, red)
# Note: sum of weights = COLS * ROWS
W_WEIGHT = 6
B_WEIGHT = 6
R_WEIGHT = 6

RECT_WIDTH = SIZE / COLS
RECT_HEIGHT = SIZE / ROWS

# Generates a random sequence of 0, 1 and 2 with the given weightings
def create_freq_seq(w, b, r):
    freqs = []
    for x in range(w):
        freqs.insert(0, 0)
    for y in range(b):
        freqs.insert(0, 1)
    for z in range(r):
        freqs.insert(0, 2)
    random.shuffle(freqs)
    return freqs

# Creates a sequence that determines where to draw squares instead of rectangles
# 9 represents the "default" state, draw rectangle
def create_div_seq(freq_seq):
    divs = []
    for x in range(0, len(freq_seq)-1):
        # If 2 consecutive elements are the same colour and are not the last in the column
        if freq_seq[x] == freq_seq[x+1] and ((x+1) % ROWS) != 0:
            divs.insert(0, freq_seq[x])
        else:
            divs.insert(0, 9)
    divs.insert(0, 9)
    divs.reverse()
    return divs

# Draws a rectangle at (x, y) with color c
# Draws a square instead if s = 1
def draw_rect(x, y, c, s):
    stroke(255, 255, 255)
    strokeWeight(5)
    strokeCap(SQUARE)
    
    # Determine color
    if c == 0:
        fill(255, 255, 255)
    if c == 1:
        fill(64, 89, 163)
    if c == 2:
        fill(246, 68, 75)
    
    # Determine square vs. rectangle
    if s == 0:
        rect(x, y, RECT_WIDTH, RECT_HEIGHT)
    if s == 1:
        rect(x, y, RECT_WIDTH, RECT_WIDTH)

# Generates the random logo
def generate():
    # generates freq and div sequences
    freqs = create_freq_seq(W_WEIGHT, B_WEIGHT, R_WEIGHT)
    divs = create_div_seq(freqs)
    
    # For debugging
    # print freqs
    # print divs
    
    # Draws rectangles
    i = 0
    for x in range(COLS):
        for y in range(ROWS):
            if divs[i] == 9:
                draw_rect(RECT_WIDTH*x, RECT_HEIGHT*y, freqs[i], 0)
            i += 1
    
    # Draws squares in a layer above the rectangles
    i = 0
    for x in range(COLS):
        for y in range(ROWS):
            if divs[i] != 9:
                rand = random.randint(0,2)
                if rand == 0:
                    draw_rect(RECT_WIDTH*x, RECT_HEIGHT*y, freqs[i], 0)
                else:
                    draw_rect(RECT_WIDTH*x, RECT_HEIGHT*y, freqs[i], 1)
            i += 1
            
# Draws default white canvas              
def setup():
    size(SIZE, SIZE)
    background(255)
    generate()