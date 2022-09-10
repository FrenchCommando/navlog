from itertools import islice
from utils.forms_functions import get_main_info
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
            print(data)
            d = {}
            origin_airport = data["origin"]
            destination_airport = data["destination"]
            d["notes"] = data["notes"]
            d["notes_0"] = "VOR Sparta SAX115.70"
            d["notes_1"] = "VOR Hughenot HUO116.1"
            d["checkpoint_1"] = origin_airport
            d["checkpoint_2"] = "Echo Lake"
            d["checkpoint_3"] = "Highland Lake"
            d["checkpoint_4"] = "Ridge"
            d["checkpoint_5"] = "Pizza42"
            d["checkpoint_6"] = destination_airport

            d["check_vfr"] = True
            d["aircraft_number"] = "734RP"
            d["2aircraft_identification"] = "N734RP"
            d["3aircraft_type"] = "C172"
            d["4true_airspeed"] = "108"
            d["5departure_point"] = origin_airport
            d["6departure_time_proposed"] = "1200Z"
            d["6departure_time_actual"] = "1215Z"
            d["7cruising_altitude"] = "4500"
            d["8route"] = "DCT"
            d["9destination"] = destination_airport
            d["10ete_hours"] = "00"
            d["10ete_minutes"] = "35"
            d["11remarks"] = "StudentPilot cross country with instructor - Century Air"
            d["12fuel_hours"] = "04"
            d["12fuel_minutes"] = "00"
            d["13alternate"] = "N82"
            d["14pilot"] = "FrenchCommando 6461112222 KCDW"
            d["15num_aboard"] = "2"
            d["16color"] = "W"
            return d

    navlog_form = FormNavLog()
    navlog_form.build()

    return forms_state
