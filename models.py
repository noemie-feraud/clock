def validate_time(t):
    """
    Verify that a tuple (h, m, s) represents a valid time.
    Returns True if valid, False otherwise.
    """

    # Check that t is indeed a tuple of size 3
    if not isinstance(t, tuple) or len(t) != 3:
        return False

    h, m, s = t

    # Check that h, m, s are integers
    if not isinstance(h, int) or not isinstance(m, int) or not isinstance(s, int):
        return False

    # Check the terminals of hours, minutes and seconds
    if h < 0 or h > 23:
        return False
    
    elif m < 0 or m > 59:
        return False
    
    elif s < 0 or s > 59:
        return False
    
    return True

def normalize_mode(mode_str):
    """
    Normalizes the display mode input.
    Returns '12h' or '24h'. By default: '24h'.
    """

    # Clean the chain (lowercase + whitespace removal)
    mode_str = mode_str.strip().lower()

    if mode_str == "12" or mode_str == "12h":
        return "12h"

    if mode_str == "24" or mode_str == "24h":
        return "24h"

    # Default value
    return "24h"
  