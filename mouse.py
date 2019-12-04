import subprocess
import time


def _get_window_id():
    proc = subprocess.run(["xdotool", "search", "--onlyvisible", "--classname",
                           "mines"], check=True, stdout=subprocess.PIPE,
                          universal_newlines=True)
    return proc.stdout


def _move_mouse(window, x, y):
    subprocess.run(["xdotool", "mousemove", "--clearmodifiers", "--sync",
                    "--window", window, str(x), str(y)],
                   check=True)


def click_mine(x, y):
    output = _get_window_id()
    _move_mouse(output, x, y)
    time.sleep(0.1)
    subprocess.run(["xdotool", "click", "1"],
                   check=True)


def click_flag(x, y):
    output = _get_window_id()
    _move_mouse(output, x, y)
    time.sleep(0.1)
    subprocess.run(["xdotool", "click", "3"],
                   check=True)
