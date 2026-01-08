from datetime import time
import msvcrt

from models import normalize_mode
from tick_time import tick_time
from format_time import format_time
from display_hour import display_hour
from set_alarm_time import set_alarm_time
from check_alarm import check_alarm
from pause_resume import toggle_pause


def ask_command():
    """
    Lit une commande utilisateur sans bloquer l'exécution.
    Retourne une touche parmi : p, m, a, q ou None.
    """
    if msvcrt.kbhit():
        key = msvcrt.getwch().lower()

        if key in ("p", "m", "a", "q"):
            return key

    return None


def orchestrator():
    """
    Fonction principale qui orchestre le fonctionnement de l'horloge.
    """

    # On affiche le menu (une seule fois) ---
    print("Commandes :")
    print("p : pause / reprise")
    print("m : changer le mode (12h / 24h)")
    print("a : régler l'alarme")
    print("q : quitter")
    print()

    # Initialisation de l'heure réelle
    now = time.localtime()
    current_time = (now.tm_hour, now.tm_min, now.tm_sec)

    # Choix du mode d'affichage 
    mode_input = input("Mode d'affichage (12h / 24h) : ")
    mode = normalize_mode(mode_input)

    # Réglage de l'alarme 
    alarm_time = set_alarm_time()

    paused = False

    # Boucle principale 
    while True:

        # Lecture non bloquante d'une commande
        cmd = ask_command()

        if cmd == "q":
            print("\nFin du programme.")
            break

        if cmd == "p":
            paused = toggle_pause(paused)

        if cmd == "m":
            mode_input = input("\nNouveau mode (12h / 24h) : ")
            mode = normalize_mode(mode_input)

        if cmd == "a":
            alarm_time = set_alarm_time()

        # Mise à jour de l'heure simulée
        if not paused:
            current_time = tick_time(current_time)

        # Formatage de l'heure
        time_str = format_time(current_time, mode)

        if paused:
            time_str += " [PAUSE]"

        # Affichage
        display_hour(time_str)

        # Vérification de l'alarme
        if check_alarm(current_time, alarm_time):
            print("\n ALARME !")
            alarm_time = None

        # Rythme d'une seconde
        time.sleep(1)


def main():
    orchestrator()


if __name__ == "__main__":
    main()
