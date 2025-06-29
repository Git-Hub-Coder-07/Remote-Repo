import curses
import time

def draw_heart(stdscr, y, x, size):
    heart = [
        "  ***   ***  ",
        " ***** ***** ",
        "*************",
        " *********** ",
        "  *********  ",
        "   *******   ",
        "    *****    ",
        "     ***     ",
        "      *      "
    ]
    
    for i, line in enumerate(heart):
        stdscr.addstr(y + i, x, line[:size], curses.color_pair(1))

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Pink color

    stdscr.clear()
    height, width = stdscr.getmaxyx()

    size = 1
    while True:
        stdscr.clear()
        y = height // 2 - 5
        x = width // 2 - 7
        draw_heart(stdscr, y, x, size)
        stdscr.refresh()
        time.sleep(0.1)
        size = size + 1 if size < 13 else 1

if __name__ == "__main__":
    curses.wrapper(main)