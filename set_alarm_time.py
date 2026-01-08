from models import validate_time

def parse_time_str(time_str):
    """
    Convertir une heure sous forme de texte en tuple (h, m, s).
    Formats acceptés : 
    - "HH:MM"
    - "HH:HH:SS"
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
    Demande à l'utilisateur une heure d’alarme (HH:MM ou HH:MM:SS) ou "none".
    Retourne :
    - un tuple (h, m, s) si l'heure est valide
    - None si l’utilisateur ne veut pas d’alarme
    """
    while True:
        user_input = input("Heure d'alarme (HH:MM ou HH:MM:SS) ou 'none' : ").strip().lower()

        # Si on a "none" ou vide alors il n'y a pas d'alarme
        if user_input == "" or user_input == "none":
            return None

        t = parse_time_str(user_input)

        if t is not None:
            return t

        print("Format invalide. Exemples: 07:30 | 07:30:00 | none")
