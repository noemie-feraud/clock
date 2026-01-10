def check_alarm (current_time, alarm_time): 
    """
    Checking the current time value against the alarm value
    """
    
    if alarm_time == None:
        return False 
    
    if current_time == alarm_time:
        return True
    else:
        return False