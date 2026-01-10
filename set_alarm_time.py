from models import validate_time

def parse_time_str(time_str):
    """
    Convertir une heure sous forme de texte en tuple (h, m, s).
    Formats acceptés : 
    - "HH:MM"
    - "HH:MM:SS"
    Retourne None si le format est invalide
    """
    # On nettoie la chaine
    time_str = time_str.strip()

    # Si elle est vide -> None
    if time_str == "":
        return None

    # On fait le découpage avec ":"
    parts = time_str.split(":")

    # On construit le tuple selon le nombre de parties
    try:
        if len(parts) == 2:
            h = int(parts[0])
            m = int(parts[1])
            s = 0
            t = (h, m, s)

        elif len(parts) == 3:
            h = int(parts[0])
            m = int(parts[1])
            s = int(parts[2])
            t = (h, m, s)

        else:
            return

    except ValueError:
        # C'est le cas où int(...) échoue (exemple: "aa:bb")
        return None

    # On fait la validation 
    if validate_time(t) is True:
        return t
    else:
        return None
    
def set_alarm_time():
    """
    Prompts the user for an alarm time (HH:MM or HH:MM:SS) or "none".

    Returns:
    - a tuple (h, m, s) if the time is valid
    - None if the user does not want an alarm
    """
    while True:
        user_input = input("Alarm time (HH:MM or HH:MM:SS) or 'none : ").strip().lower()

        # If the input is 'none' or empty, then there is no alarm.
        if user_input == "" or user_input == "none":
            return None

        t = parse_time_str(user_input)

        if t is not None:
            return t

        print("Invalid format. Examples: 07:30 | 07:30:00 | none")
