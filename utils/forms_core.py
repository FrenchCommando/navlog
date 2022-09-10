from utils.forms_functions import get_main_info, \
    hour_to_hours_minutes_seconds, get_wind_correction, revert_to_hours
from utils.form_worksheet_names import *
from utils.forms_constants import logger


def fill_contents(d):
    main_info = get_main_info(d)
    forms_state = {}  # mapping name of forms with content

    class Form:
        def __init__(self, key):
            self.key = key

        def build(self):
            raise NotImplementedError()

    class FormNavLog(Form):
        def __init__(self):
            Form.__init__(self, k_navlog)

        def build(self):
            ll = [self.build_one(data=one_info) for one_info in main_info]
            forms_state[k_navlog] = ll

        @staticmethod
        def build_one(data):
            vor_dict = dict(
                SAX="VOR Sparta SAX115.70",
                HUO="VOR Hughenot HUO116.1",
            )
            print(data)
            d = {}
            origin_airport = data["origin"]
            destination_airport = data["destination"]
            aircraft_number = data["aircraft"]
            gph = data["gph"]
            fuel_time = data["fuel"] / gph
            d["notes"] = data["notes"]
            vor1, vor2 = data["vor"]
            d["notes_0"] = vor_dict[vor1]
            d["notes_1"] = vor_dict[vor2]
            d["cas"] = data["cas"]

            wind_dir, wind_vel = data["winds"]

            d["gph"] = gph

            for i, point in enumerate(data["checkpoints"], 1):
                checkpoint, vor1_radial, vor2_radial = point
                d[f"checkpoint_{i}"] = checkpoint
                d[f"vor_ident_{i}"] = vor1_radial
                d[f"vor_freq_{i}"] = vor2_radial

            for i, route in enumerate(data["route"], 1):
                tas, tc, leg = route

                d[f"course_{i}"] = tc
                d[f"tas_{i}"] = tas
                d[f"tc_{i}"] = tc
                d[f"dist_leg_{i}"] = f"{leg:.1f}"

                d[f"wind_dir_{i}"] = wind_dir
                d[f"wind_vel_{i}"] = wind_vel

                gs, lr = get_wind_correction(
                    tc=tc, tas=tas, wind_dir=wind_dir, wind_vel=wind_vel,
                )
                th = tc + lr
                d[f"lr_{i}"] = f"{lr:.0f}"
                d[f"th_{i}"] = f"{th:.0f}"

                ew_value = 12
                dev_value = 0
                d[f"ew_{i}"] = ew_value
                d[f"dev_{i}"] = dev_value

                d[f"mh_{i}"] = f"{th + ew_value:.0f}"
                d[f"ch_{i}"] = f"{th + ew_value + dev_value:.0f}"

                d[f"gs_est_{i}"] = f"{gs:.0f}"

                d[f"altitude_{i}"] = data["altitude"]
                d[f"temp_{i}"] = data["temp"]

                ete_value = leg / gs
                ete_h, ete_m, ete_s = hour_to_hours_minutes_seconds(hours=ete_value)
                d[f"ete_{i}"] = f"{ete_m}:{ete_s}"
                d[f"fuel_{i}"] = f"{gph * ete_value:.1f}"

            total_dist = sum(float(d[f"dist_leg_{i + 1}"]) for i in range(len(data["route"])))
            d["remaining_distance"] = f"{total_dist:.0f}"
            d["total_rem"] = f"{total_dist:.0f}"

            total_time = sum(revert_to_hours(s=d[f"ete_{i + 1}"]) for i in range(len(data["route"])))
            total_time_h, total_time_m, total_time_s = hour_to_hours_minutes_seconds(hours=total_time)

            d["total_ate"] = f"{total_time_m}:{total_time_s}"

            total_fuel = sum(float(d[f"fuel_{i + 1}"]) for i in range(len(data["route"])))
            d["total_fuel"] = f"{total_fuel:.1f}"

            current_dist = total_dist
            current_time = total_time
            current_fuel = data["fuel"]
            for i in range(1, len(data["route"]) + 1):
                current_dist -= float(d[f'dist_leg_{i}'])
                d[f"dist_rem_{i}"] = f"{current_dist:.1f}"

                current_time -= revert_to_hours(s=d[f"ete_{i}"])
                eta_h, eta_m, eta_s = hour_to_hours_minutes_seconds(hours=current_time)
                d[f"eta_{i}"] = f"{eta_m}:{eta_s}"

                current_fuel -= float(d[f'fuel_{i}'])
                d[f"fuel_rem_{i}"] = f"{current_fuel:.1f}"

            time_enroute = 0.55

            d["check_vfr"] = True
            d["aircraft_number"] = aircraft_number[1:]  # without the N
            d["2aircraft_identification"] = aircraft_number
            d["3aircraft_type"] = "C172"
            d["4true_airspeed"] = d["tas_2"]
            d["5departure_point"] = origin_airport
            d["6departure_time_proposed"] = f"{data['time']}Z"
            # d["6departure_time_actual"] = f"{data['time']}Z"
            d["7cruising_altitude"] = d["altitude_2"]
            d["8route"] = "DCT"
            d["9destination"] = destination_airport
            d["10ete_hours"], d["10ete_minutes"], _ = hour_to_hours_minutes_seconds(hours=time_enroute)
            d["11remarks"] = "StudentPilot cross country with instructor - Century Air"
            d["12fuel_hours"], d["12fuel_minutes"], _ = hour_to_hours_minutes_seconds(hours=fuel_time)
            d["13alternate"] = data["alternate"]
            d["14pilot"] = "FrenchCommando 6461112222 KCDW"
            d["15num_aboard"] = "2"
            d["16color"] = "W"
            return d

    navlog_form = FormNavLog()
    navlog_form.build()

    return forms_state
