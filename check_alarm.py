def check_alarm (current_time, alarm_time): 
    """
    Vérification de la valeur de actuelle par rapport à la valeur de l'alarme
    """
    
    if alarm_time == None:
        return False 
    
    if current_time == alarm_time:
        return True
    else:
        return False