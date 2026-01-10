def display_hour(time_str):
    """
    Displays the time in the terminal by updating
    a single line (without rewriting the entire screen).
    """

    # \r allows to return to the beginning of the line
    # end="" avoids the line break
    # flush=True forces the immediate display
    print(f"\rHorloge : {time_str}    ", end="", flush=True)

