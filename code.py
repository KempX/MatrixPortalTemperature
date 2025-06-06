# --- Imports ---
import time, os, board
from adafruit_matrixportal.matrixportal import MatrixPortal

# --- Configuration ---
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
DISPLAY_ROTATION = 180
DISPLAY_COLOR_ORDER = "BRG"
FONT_FILE = "fonts/RobotoSemiCondensed-Medium-75.bdf"
ROUND_VALUE = 1
UPDATE_INTERVAL = 60

# --- Environment variables ---
DATA_SOURCE = os.getenv("DATA_SOURCE")
DATA_LOCATION = os.getenv("DATA_LOCATION")

# --- Display setup ---
matrixportal = MatrixPortal(width = DISPLAY_WIDTH,
                            height = DISPLAY_HEIGHT,
                            rotation = DISPLAY_ROTATION,
                            color_order = DISPLAY_COLOR_ORDER, 
                            status_neopixel = board.NEOPIXEL,
                            url = DATA_SOURCE,
                            json_path = DATA_LOCATION, 
                            debug = True)

# --- Text setup ---
matrixportal.add_text(
    text_font = FONT_FILE,
    text_position = ((matrixportal.graphics.display.width // 2) - 1, 0),
    text_scale = 1,
    line_spacing = 1,
    text_anchor_point = (0.5,0),
)

# --- Main loop ---
while True:
    value = matrixportal.fetch()
    rounded = round(value, ROUND_VALUE)
    # print("Response: ", value)
    matrixportal.set_text("Temperatur: \n{}°C".format(rounded))
    matrixportal.set_text_color("090147")
    time.sleep(UPDATE_INTERVAL)
