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
            self.d = {}
            forms_state[self.key] = self.d

        def push_to_dict(self, key, value, round_i=0):
            if value != 0:
                self.d[key] = round(value, round_i)

        def push_sum(self, key, it):
            self.d[key] = sum(self.d.get(k, 0) for k in it)

        def build(self):
            raise NotImplementedError()

    class FormNavLog(Form):
        def __init__(self):
            Form.__init__(self, k_navlog)

        def build(self):
            self.d.update(main_info)

        def fill_stuff(self):
            self.d["notes_0"] = "VOR Sparta SAX115.70"
            self.d["notes_1"] = "VOR Hughenot HUO116.1"
            self.d["checkpoint_1"] = "KCDW"
            self.d["checkpoint_2"] = "Echo Lake"
            self.d["checkpoint_3"] = "Highland Lake"
            self.d["checkpoint_4"] = "Ridge"
            self.d["checkpoint_5"] = "Pizza42"
            self.d["checkpoint_6"] = "KMSV"

            self.d["check_vfr"] = True
            self.d["aircraft_number"] = "734RP"
            self.d["2aircraft_identification"] = "N734RP"
            self.d["3aircraft_type"] = "C172"
            self.d["4true_airspeed"] = "108"
            self.d["5departure_point"] = "KCDW"
            self.d["6departure_time_proposed"] = "1200Z"
            self.d["6departure_time_actual"] = "1215Z"
            self.d["7cruising_altitude"] = "4500"
            self.d["8route"] = "DCT"
            self.d["9destination"] = "KMSV"
            self.d["10ete_hours"] = "00"
            self.d["10ete_minutes"] = "35"
            self.d["11remarks"] = "StudentPilot cross country with instructor - Century Air"
            self.d["12fuel_hours"] = "04"
            self.d["12fuel_minutes"] = "00"
            self.d["13alternate"] = "N82"
            self.d["14pilot"] = "FrenchCommando 6461112222 KCDW"
            self.d["15num_aboard"] = "2"
            self.d["16color"] = "W"

    navlog_form = FormNavLog()
    navlog_form.build()
    navlog_form.fill_stuff()

    return forms_state
