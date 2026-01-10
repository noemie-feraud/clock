import time
import msvcrt
import os

from models import normalize_mode
from tick_time import tick_time
from format_time import format_time
from display_hour import display_hour
from set_alarm_time import set_alarm_time
from check_alarm import check_alarm
from alarm_sound import init_sound, start_alarm_sound, stop_alarm_sound
from pause_resume import toggle_pause


def ask_command(): 
    """
    Non-blocking key reading (Windows).
    Return: "p", "m", "a", "s" or None.
    """
    if msvcrt.kbhit():
        key = msvcrt.getwch().lower()
        if key in ("p", "m", "a", "s"):
            return key
    return None


def format_alarm_display(alarm_time):
    """
    Readable display of the alarm.
    """
    if alarm_time is None:
        return "--:--:--"
    h, m, s = alarm_time
    return f"{h:02d}:{m:02d}:{s:02d}"


def print_header():
    """
    Display the fixed interface (once only).
    """
    print()
    print("╔════════════════════════════════════════════════════╗")
    print("║                   GRANDMA'S CLOCK                  ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║  p : pause / resume                                ║")
    print("║  m : switch mode (12h / 24h)  | default = 24h      ║")
    print("║  a : set the alarm            | default = none     ║")
    print("║  s : stop                                          ║")
    print("╚════════════════════════════════════════════════════╝")
    print()  # empty line before the line that updates


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def orchestrator():
    # Fixed interface
    print_header()
    init_sound()

    # actual time at te launch
    now = time.localtime()
    current_time = (now.tm_hour, now.tm_min, now.tm_sec)

    # default mode
    mode = "24h"

    # no alarm at launch
    alarm_time = None

    paused = False

    # status 'alar in progress'
    alarm_ringing = False

    # counter for small flashing effect
    tick = 0

    while True:
        tick += 1
        cmd = ask_command()

        if cmd == "s":
            stop_alarm_sound()
            print("\nEnd of grandma’s clock.")
            break

        # if the alarm sounds, 'p' is used to stop it (and we do not touch the pause)
        if alarm_ringing and cmd == "p":
            alarm_ringing = False
            stop_alarm_sound()
            clear_terminal()
            print_header()
            cmd = None  # avoids also activating pause/resume

        if cmd == "p":
            paused = toggle_pause(paused)

        if cmd == "m":
            # We move to the line to avoid breaking the display
            mode_input = input("\nNew mode (12h / 24h) : ")
            mode = normalize_mode(mode_input)
            clear_terminal()
            print_header()

        if cmd == "a":
            # Alarm input + terminal cleaning 
            alarm_time = set_alarm_time()
            clear_terminal()
            print_header()

        # Advance the simulated time
        if not paused:
            current_time = tick_time(current_time)

        # trigger without print() (otherwise it creates lines)
        if (not alarm_ringing) and check_alarm(current_time, alarm_time):
            alarm_ringing = True
            alarm_time = None  # no more programmed alarm after triggering
            start_alarm_sound()

        # Build the display line
        clock_str = format_time(current_time, mode)
        alarm_str = format_alarm_display(alarm_time)

        # priority status ALARM if it rings
        state_str = "ALARM" if alarm_ringing else ("PAUSE" if paused else "ACTIVE")

        line = f"{clock_str} | Mode : {mode} | Alarm : {alarm_str} | Status : {state_str}"

        # visible alarm message on the SAME line + stop command
        if alarm_ringing:
            flash = "!! ALARM !!" if (tick % 2 == 0) else "  ALARM   "
            line += f"   {flash} (p to stop the alarm)"

        display_hour(line)

        time.sleep(1)


def main():
    orchestrator()


if __name__ == "__main__":
    main()
