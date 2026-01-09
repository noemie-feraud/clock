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
    Lecture de touche non bloquante (Windows).
    Retourne: "p", "m", "a", "q" ou None.
    """
    if msvcrt.kbhit():
        key = msvcrt.getwch().lower()
        if key in ("p", "m", "a", "q"):
            return key
    return None


def format_alarm_display(alarm_time):
    """
    Affichage lisible de l'alarme.
    """
    if alarm_time is None:
        return "--:--:--"
    h, m, s = alarm_time
    return f"{h:02d}:{m:02d}:{s:02d}"


def print_header():
    """
    Affiche l'interface fixe (une seule fois).
    """
    print()
    print("╔════════════════════════════════════════════════════╗")
    print("║                    HORLOGE MAMIE                   ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║  p : pause / reprise                               ║")
    print("║  m : changer mode (12h / 24h)  | défaut = 24h      ║")
    print("║  a : régler l'alarme           | défaut = aucune   ║")
    print("║  q : quitter                                       ║")
    print("╚════════════════════════════════════════════════════╝")
    print()  # ligne vide avant la ligne qui s'actualise


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def orchestrator():
    # Interface fixe
    print_header()
    init_sound()

    # Heure réelle au lancement
    now = time.localtime()
    current_time = (now.tm_hour, now.tm_min, now.tm_sec)

    # Mode par défaut
    mode = "24h"

    # Pas d'alarme au lancement
    alarm_time = None

    paused = False

    # état "alarme en cours"
    alarm_ringing = False

    # compteur pour petit effet clignotant
    tick = 0

    while True:
        tick += 1
        cmd = ask_command()

        if cmd == "q":
            stop_alarm_sound()
            print("\nFin du programme.")
            break

        # si l'alarme sonne, 'p' sert à l'arrêter (et on ne touche pas au pause)
        if alarm_ringing and cmd == "p":
            alarm_ringing = False
            stop_alarm_sound()
            clear_terminal()
            print_header()
            cmd = None  # évite d'activer aussi pause/reprise

        if cmd == "p":
            paused = toggle_pause(paused)

        if cmd == "m":
            # On passe à la ligne pour ne pas casser l'affichage
            mode_input = input("\nNouveau mode (12h / 24h) : ")
            mode = normalize_mode(mode_input)
            clear_terminal()
            print_header()

        if cmd == "a":
            # Saisie alarme + nettoyage terminal 
            alarm_time = set_alarm_time()
            clear_terminal()
            print_header()

        # Avancer l'heure simulée
        if not paused:
            current_time = tick_time(current_time)

        # déclenchement sans print() (sinon ça crée des lignes)
        if (not alarm_ringing) and check_alarm(current_time, alarm_time):
            alarm_ringing = True
            alarm_time = None  # plus d'alarme programmée après déclenchement
            start_alarm_sound()

        # Construire la ligne d'affichage
        clock_str = format_time(current_time, mode)
        alarm_str = format_alarm_display(alarm_time)

        # état prioritaire ALARME si ça sonne
        state_str = "ALARME" if alarm_ringing else ("PAUSE" if paused else "ACTIF")

        line = f"{clock_str} | Mode : {mode} | Alarme : {alarm_str} | Etat : {state_str}"

        # message d'alarme visible sur la MÊME ligne + commande stop
        if alarm_ringing:
            flash = "!! ALARME !!" if (tick % 2 == 0) else "  ALARME   "
            line += f"   {flash} (p pour arrêter)"

        display_hour(line)

        time.sleep(1)


def main():
    orchestrator()


if __name__ == "__main__":
    main()
