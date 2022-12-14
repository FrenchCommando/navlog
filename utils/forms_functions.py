import numpy as np


def get_main_info(d):
    info = d['json']
    for entry in info:
        entry.update(dict(
            pilot="FrenchCommando 6461112222 KCDW",
            aircraft="N172YA",
        ))
    return info


def compute_stuff():
    return 100


def hour_to_hours_minutes_seconds(hours):
    return f"{int(hours)}", \
           f"{int((hours - int(hours)) * 60)}", \
           f"{int(((hours - int(hours)) * 60 - int((hours - int(hours)) * 60)) * 60)}"


def time_str_to_string(ete_h, ete_m, ete_s):
    return f"{ete_h + ':' if ete_h != '0' else ''}{ete_m}:{ete_s}"


def revert_to_hours(str_input):
    tab = str_input.split(":")
    if len(tab) == 3:
        h, m, s = tab
    elif len(tab) == 2:
        m, s = tab
        h = "0"
    else:
        raise ValueError(str_input)
    return (float(h) + float(s) / 60 + float(m)) / 60


def get_wind_correction(
        tc, tas, wind_dir, wind_vel,
):
    radian_conversion = 180 / np.pi
    angle = (wind_dir - tc) / radian_conversion
    lr = np.arcsin(wind_vel * np.sin(angle) / tas)
    other_angle = np.pi - (angle - lr)
    gs = tas * np.sin(other_angle) / np.sin(angle)
    return gs, radian_conversion * lr


if __name__ == '__main__':
    tc_val, tas_val, wind_dir_val, wind_vel_val = 30, 100, 90, 30
    gs_val, lr_val = get_wind_correction(
        tc=tc_val, tas=tas_val, wind_dir=wind_dir_val, wind_vel=wind_vel_val,
    )
    print(gs_val, lr_val)
