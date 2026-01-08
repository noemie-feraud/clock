def tick_time(t):
    """
    Fait avancer une heure simulée d'une seconde.

    Paramètre :
    - t : tuple (h, m, s)

    Retour :
    - nouveau tuple (h, m, s)
    """

    h, m, s = t

    # Ajouter une seconde
    s = s + 1

    # Gestion du dépassement des secondes
    if s == 60:
        s = 0
        m = m + 1

    # Gestion du dépassement des minutes
    if m == 60:
        m = 0
        h = h + 1

    # Gestion du dépassement des heures
    if h == 24:
        h = 0

    return (h, m, s)
