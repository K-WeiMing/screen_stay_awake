"""
This python script utilises PyAutoGUI to prevent the display from going to sleep
"""
import time
import datetime
import random
import pyautogui
import yaml
from yaml import SafeLoader

START_TIME = datetime.datetime.now()

with open("config.yml", "r", encoding="utf-8") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=SafeLoader)


def win_stay_awake():
    """
    Uses the config parameters to prevent display sleep
    """

    while True:
        move_interval = random.randint(
            cfg["config"]["move_interval_start"], cfg["config"]["move_interval_end"]
        )
        key_interval = random.uniform(
            cfg["config"]["key_press_interval_start"],
            cfg["config"]["key_press_interval_end"],
        )

        print(
            f"Time to next action: \
            {START_TIME + datetime.timedelta(seconds= move_interval)}, \
            key_interval: {key_interval}"
        )
        time.sleep(move_interval)

        pyautogui.press(keys=cfg["config"]["keys"], interval=key_interval)
        print(f"Action completed\nTime elapsed: {datetime.datetime.now() - START_TIME}")


if __name__ == "__main__":
    win_stay_awake()
