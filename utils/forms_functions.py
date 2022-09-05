from utils.forms_constants import override_keyword


def get_main_info(d):
    info = d['json'][0]
    if override_keyword in d:
        info.update(d[override_keyword])
    return info


def compute_stuff():
    return 100
