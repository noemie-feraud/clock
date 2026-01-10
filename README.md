# Grandma Clock 

A robust, terminal-based digital clock written in Python. It simulates time ticking, handles alarms with sound, and offers a user-friendly interface.

## Features

* **Real-time Display:** Updates every second in `HH:MM:SS` format.
* **Alarm System:** Set an alarm time. Visual notifications and **audio playback** (MP3) when triggered.
* **Custom Modes:** Switch between **12h (AM/PM)** and **24h** formats.
* **Pause/Resume:** Temporarily stop the clock update mechanism.
* **Non-blocking Input:** Interacts with the user without freezing the time display (Windows `msvcrt`).

---

## Getting Started

### Prerequisites

* **OS:** Windows (required for non-blocking key reads).
* **Python 3.x**
* **Dependencies:** `pygame` (for audio).

### Installation

1.  Clone the repository or download the files.
2.  Install the required audio library:
    ```bash
    pip install pygame
    ```
3.  Ensure `alarm.mp3` is in the same directory as `main.py`.

### Commandes :
```
p : pause / resume (if alarm rings : p stop it and cut the sound)

m : switch mode (12h / 24h)

a : set the alarm (HH:MM or HH:MM:SS, or none)

s : stop
```


### Structure du projet : 
.
├──  alarm.mp3           # Audio file for the alarm
├──  alarm_sound.py      # Audio management (Pygame)
├──  check_alarm.py      # Logic to trigger the alarm
├──  display_hour.py     # Refreshes the terminal line
├──  format_time.py      # Handles 12h/24h formatting
├──  main.py             # Entry point / Orchestrator
├──  models.py           # Data validation & logic
├──  pause_resume.py     # Toggles pause state
├──  set_alarm_time.py   # User input parsing
└──  tick_time.py        # Simulates time passing (1s)

---

## [![Made by](https://img.shields.io/badge/R%C3%89ALIS%C3%89-PAR-orange?style=for-the-badge)](https://forthebadge.com)

**Antuat Abdallah** | **Ahamada Assmine** | **Noémie Feraud**