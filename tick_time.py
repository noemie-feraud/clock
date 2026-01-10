def tick_time(t):
    """
    Advances a simulated time by one second.

    Parameter:
    - t: tuple (h, m, s)

    Returns:
    - new tuple (h, m, s)
    """

    h, m, s = t

    # Add one second
    s = s + 1

    # Handle seconds overflow
    if s == 60:
        s = 0
        m = m + 1

    # Handle minutes overflow
    if m == 60:
        m = 0
        h = h + 1

    # Hangle hours overflow
    if h == 24:
        h = 0

    return (h, m, s)
