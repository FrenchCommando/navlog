def get_main_info(d):
    info = d['json']
    return info


def compute_stuff():
    return 100


def hour_to_hours_minutes_seconds(hours):
    return f"{int(hours)}", \
           f"{int((hours - int(hours)) * 60)}", \
           f"{int(((hours - int(hours)) * 60 - int((hours - int(hours)) * 60)) * 60)}"
