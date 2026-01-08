def format_time(t, mode):
    """
    Transforme une heure sous forme de tuple (h, m, s)
    en chaîne de caractères selon le mode d'affichage.
    """

    h, m, s = t

    # Mode 24h
    if mode == "24h":
        return f"{h:02d}:{m:02d}:{s:02d}"

    # Mode 12h
    else:
        if h < 12:
            suffix = "AM"
        else:
            suffix = "PM"

        h12 = h % 12
        if h12 == 0:
            h12 = 12

        return f"{h12:02d}:{m:02d}:{s:02d} {suffix}"

