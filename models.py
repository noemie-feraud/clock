def validate_time(t):
    """
    Vérifie qu'un tuple (h, m, s) représente une heure valide.
    Retourne True si valide, False sinon.
    """

    # Vérifier que t est bien un tuple de taille 3
    if not isinstance(t, tuple) or len(t) != 3:
        return False

    h, m, s = t

    # Vérifier que h, m, s sont des entiers
    if not isinstance(h, int) or not isinstance(m, int) or not isinstance(s, int):
        return False

    # Vérifier les bornes des heures, minutes et secondes
    if h < 0 or h > 23:
        return False
    
    elif m < 0 or m > 59:
        return False
    
    elif s < 0 or s > 59:
        return False
    
    return True

def normalize_mode(mode_str):
    """
    Normalise la saisie du mode d'affichage.
    Retourne '12h' ou '24h'. Par défaut : '24h'.
    """

    # Nettoyer la chaîne (minuscules + suppression des espaces)
    mode_str = mode_str.strip().lower()

    if mode_str == "12" or mode_str == "12h":
        return "12h"

    if mode_str == "24" or mode_str == "24h":
        return "24h"

    # Valeur par défaut
    return "24h"
  