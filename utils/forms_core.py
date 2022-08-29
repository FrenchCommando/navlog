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
            self.d["navlogkey"] = "Blah"

    FormNavLog().build()
    return forms_state
