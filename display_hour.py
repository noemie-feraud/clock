def display_hour(time_str):
    """
    Affiche l'heure dans le terminal en mettant à jour
    une seule ligne (sans réécrire tout l'écran).
    """

    # \r permet de revenir au début de la ligne
    # end="" évite le retour à la ligne
    # flush=True force l'affichage immédiat
    print(f"\r{time_str}", end="", flush=True)
