from itertools import islice
from utils.forms_functions import get_main_info, hour_to_hours_minutes_seconds
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
            fuel_time = data["fuel_time"]
            d["notes"] = data["notes"]
            vor1, vor2 = data["vor"]
            d["notes_0"] = vor_dict[vor1]
            d["notes_1"] = vor_dict[vor2]
            d["cas"] = data["cas"]

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
                d[f"dist_leg_{i}"] = leg

                d[f"altitude_{i}"] = data["altitude"]
                d[f"temp_{i}"] = data["temp"]

            d["gph"] = data["gph"]

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
