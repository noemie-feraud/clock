def format_time(t, mode):
    """
    Transform an hour into a tuple (h, m, s)
    in a string according to the display mode.
    """

    h, m, s = t

    # 24h mode
    if mode == "24h":
        return f"{h:02d}:{m:02d}:{s:02d}"

    # 12h mode
    else:
        if h < 12:
            suffix = "AM"
        else:
            suffix = "PM"

        h12 = h % 12
        if h12 == 0:
            h12 = 12

        return f"{h12:02d}:{m:02d}:{s:02d} {suffix}"

