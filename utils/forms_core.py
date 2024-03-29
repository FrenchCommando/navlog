import re

from utils.forms_functions import get_main_info, \
    hour_to_hours_minutes_seconds, get_wind_correction, revert_to_hours, time_str_to_string
from utils.form_worksheet_names import *
from utils.forms_constants import logger


vor_dict = dict(
    SAX="VOR Sparta SAX115.70 ... - .--",
    HUO="VOR Hughenot HUO116.1 .... ..- ---",
    STW="VOR Stillwater STW109.6 ... - .--",
    BWZ="VOR Broadway BWZ114.2 -... .-- --..",
    PTW="VOR Pottstown PTW116.5 .--. - .--",
    SBJ="VOR Solberg SBJ112.9 ... _... .___",
    LVZ="VOR Wilkes-Barre LVZ111.6 .-.. ...- --..",
    ETX="VOR EastTexas ETX110.2 . - -..-",
    LRP="VOR Lancaster LRP117.3 ._.. ._. .__.",
    IWA="VOR Willie IWA113.3 .. .__ ._",
    TFD="VOR Stanfield TFD114.8 _ .._. _..",
    TUS="VOR Tucson TUS116.0 _ .._ ...",
    GBN="VOR GilaBend GBN116.6 __. _... _."
)
airport_info = dict(
    KCDW=dict(
        atis=135.5,
        ground=121.9,
        tower=119.8,
        elevation=172.3,
        runway="4/22(45)-10/28(37)",
        tpa=1200,
    ),
    KMSV=dict(
        atis=124.725,
        ctaf=122.8,
        elevation=1403.1,
        runway="15/33(62)",
        tpa=2400,
    ),
    N82=dict(
        ctaf=122.8,
        atis=119.275,
        elevation=548.4,
        tpa=1600,
        runway="5/23(35)"
    ),
    KMMU=dict(
        elevation=186.6,
        tower=118.1,
        ground=134.2,
        atis=124.25,
        tpa=1200,
        runway="5/23(59) 13/31(39)"
    ),
    KCKZ=dict(
        elevation=567.6,
        ctaf=123.0,
        atis=126.325,
        tpa=1400,
        runway="8/26(42)",
    ),
    KUKT=dict(
        elevation=525.1,
        ctaf=122.725,
        atis=119.475,
        tpa=1600,
        runway="11/29(32)",
    ),
    KAVP=dict(
        elevation=961.7,
        tower=120.1,
        ground=121.9,
        atis=111.6,
        unicom=122.95,
        tpa=2000,
        runway="4/22(75) 10/28(43)",
    ),
    KMPO=dict(
        elevation=1915.2,
        ctaf=122.7,
        atis=120.275,
        tpa=3000,
        runway="12/31(50) 5/23(39)",
    ),
    N89=dict(
        elevation=292,
        ctaf=122.8,
        atis="MGJ119.275",
        tpa=1300,
        runway="4/22(38) 22R",
    ),
    KCXY=dict(
        elevation=347,
        ctaf=119.5,
        atis=134.95,
        ground=121.9,
        tpa=1847,
        runway="8/26(50) 12/30(37)",
    ),
    k58N=dict(
        elevation=489,
        ctaf=122.8,
        atis="MUI124.175",
        tpa=1500,
        runway="13/31(19)",
    ),
    KFFZ=dict(
        atis=118.25,
        ground=121.3,
        tower=124.6,
        elevation=1394,
        runway="4L/22R(51)-4R/22L(38)",
        tpa=2400,
        approach="Phoenix120.7"
    ),
    KRYN=dict(
        ctaf=125.8,
        ground=118.2,
        tower=125.8,
        atis="AWOS-3:133.35",
        elevation=2418.9,
        runway="6L/24R(right)(49)-6R(right)/24L(55)",
        tpa=3218.9,
        approach="Tucson128.5"
    ),
    KIWA=dict(
        atis=133.5,
        ground=128.25,
        tower=120.6,
        elevation=1384.1,
        runway="12L/30R(102)-12R(right)/30L(104)",
        tpa=2602.1,
        approach="Phoenix124.9"
    ),
    kE63=dict(
        ctaf=122.8,
        elevation=788.7,
        runway="4/22(52)",
        tpa=1588.7,
    ),
    KSEZ=dict(
        atis="AWOS-3PT 118.525",
        ctaf=123.0,
        elevation=4830,
        runway="3/21(51)",
        tpa=6000.0,
    ),
    KPAN=dict(
        atis="AWOS-3PT 119.325",
        ctaf=122.8,
        elevation=5156,
        runway="6/24(55)",
        tpa=6200.0,
    ),

)

climb_performance = {
    0: dict(Time=0, Fuel=0, Distance=0),
    2000: dict(Time=3, Fuel=0.6, Distance=4),
    2500: dict(Time=4, Fuel=0.8, Distance=5),
    3500: dict(Time=6, Fuel=1.2, Distance=7.5),
    4500: dict(Time=8, Fuel=1.6, Distance=10),
    5500: dict(Time=10, Fuel=2, Distance=12.5),
    6500: dict(Time=12.5, Fuel=2.4, Distance=16),
    7500: dict(Time=15.5, Fuel=2.85, Distance=20),
    8000: dict(Time=17, Fuel=3.1, Distance=22),
    9000: dict(Time=20, Fuel=3.6, Distance=26),
    10000: dict(Time=24, Fuel=4.2, Distance=32),
}
climb_performance_time = {alt: v["Time"] for alt, v in climb_performance.items()}
climb_performance_fuel = {alt: v["Fuel"] for alt, v in climb_performance.items()}
climb_performance_distance = {alt: v["Distance"] for alt, v in climb_performance.items()}


def interpolate(ts, value):
    if value in ts:
        return ts[value]
    left = 0
    right = 0
    for t, v in ts.items():
        right = t
        if t < value:
            left = t
        else:
            break
    return ts[left] + (value - left) * (ts[right] - ts[left]) / (right - left)


def get_dev_value(mh):
    deviation_card = {
        0: 0,
        30: 0,
        60: 1,
        90: 1,
        120: 0,
        150: 0,
        180: 0,
        210: 0,
        240: 1,
        270: 2,
        300: 2,
        330: 0,
        360: 0,
    }
    return interpolate(deviation_card, mh)


def get_climb_performance(prev_altitude, default=None):
    if prev_altitude is None:
        return get_climb_performance(prev_altitude=default)
    return dict(
        Time=interpolate(ts=climb_performance_time, value=prev_altitude),
        Fuel=interpolate(ts=climb_performance_fuel, value=prev_altitude),
        Distance=interpolate(ts=climb_performance_distance, value=prev_altitude),
    )


def fill_contents(dict_input):
    main_info = get_main_info(d=dict_input)
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
            ll_overflow = [one for item in ll for one in self.build_overflown(item)]
            forms_state[k_navlog] = ll + ll_overflow

        @staticmethod
        def build_one(data):
            d = {}
            origin_airport = data["origin"]
            destination_airport = data["destination"]
            aircraft_number = data["aircraft"]
            gph = data["gph"]
            fuel_time = data["fuel"] / gph
            d["notes"] = data["notes"]
            d["notes_0"] = "    ".join(f"{vor_dict[vor_single]}" for vor_single in data["vor"])
            d["notes_1"] = f"TPA for {origin_airport}:\t{airport_info[origin_airport]['tpa']}''         " \
                           f"TPA for {destination_airport}:\t{airport_info[destination_airport]['tpa']}''"

            alternate = data["alternate"]
            d["notes_2"] = f"Alternate {alternate} {airport_info[alternate]}"

            transition_list = data.get("transition", [])
            for index, airport in zip(["notes_3", "notes_4"], transition_list):
                d[index] = f"Transition {airport}{airport_info[airport]}"

            d["cas"] = data["cas"]

            wind_dir, wind_vel = data["winds"]

            d["gph"] = gph

            for i, point in enumerate(data["checkpoints"], 1):
                checkpoint, vor1_radial, vor2_radial = point
                d[f"checkpoint_{i}"] = checkpoint
                d[f"vor_ident_{i}"] = vor1_radial
                d[f"vor_freq_{i}"] = vor2_radial

            prev_altitude = None
            for i, route in enumerate(data["route"], 1):
                tas, tc, leg, altitude = route

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

                ew_value = -10
                d[f"ew_{i}"] = ew_value

                mh_value = th + ew_value
                d[f"mh_{i}"] = f"{mh_value:.0f}"

                dev_value = get_dev_value(mh=mh_value)
                d[f"dev_{i}"] = dev_value
                d[f"ch_{i}"] = f"{mh_value + dev_value:.0f}"

                d[f"gs_est_{i}"] = f"{gs:.0f}"

                d[f"altitude_{i}"] = altitude
                d[f"temp_{i}"] = data["temp"]

                if prev_altitude is None:
                    taxi_fuel = 1.1
                else:
                    taxi_fuel = 0

                if prev_altitude is None or prev_altitude < altitude:
                    prev_altitude_perf = get_climb_performance(
                        prev_altitude,
                        default=airport_info[origin_airport]['tpa']
                    )
                    altitude_perf = get_climb_performance(altitude)
                    climb_distance, climb_time, climb_fuel = \
                        altitude_perf["Distance"] - prev_altitude_perf["Distance"], \
                        (altitude_perf["Time"] - prev_altitude_perf["Time"]) / 60, \
                        altitude_perf["Fuel"] - prev_altitude_perf["Fuel"]
                else:
                    climb_distance, climb_time, climb_fuel = 0, 0, 0

                time_not_climb = (leg - climb_distance) / gs
                ete_value = time_not_climb + climb_time
                fuel_value = gph * time_not_climb + climb_fuel + taxi_fuel
                ete_h, ete_m, ete_s = hour_to_hours_minutes_seconds(hours=ete_value)
                d[f"ete_{i}"] = time_str_to_string(ete_h=ete_h, ete_m=ete_m, ete_s=ete_s)
                d[f"fuel_{i}"] = f"{fuel_value:.1f}"
                prev_altitude = altitude

            total_dist = sum(float(d[f"dist_leg_{i + 1}"]) for i in range(len(data["route"])))
            d["remaining_distance"] = f"{total_dist:.0f}"
            d["total_rem"] = f"{total_dist:.0f}"

            total_time = sum(revert_to_hours(str_input=d[f"ete_{i + 1}"]) for i in range(len(data["route"])))
            total_time_h, total_time_m, total_time_s = hour_to_hours_minutes_seconds(hours=total_time)

            d["total_ate"] = time_str_to_string(ete_h=total_time_h, ete_m=total_time_m, ete_s=total_time_s)

            total_fuel = sum(float(d[f"fuel_{i + 1}"]) for i in range(len(data["route"])))
            d["total_fuel"] = f"{total_fuel:.1f}"

            current_dist = total_dist
            current_time = total_time
            current_fuel = data["fuel"]
            for i in range(1, len(data["route"]) + 1):
                current_dist -= float(d[f'dist_leg_{i}'])
                d[f"dist_rem_{i}"] = f"{current_dist:.1f}"

                current_time -= revert_to_hours(str_input=d[f"ete_{i}"])
                eta_h, eta_m, eta_s = hour_to_hours_minutes_seconds(hours=current_time)
                d[f"eta_{i}"] = time_str_to_string(ete_h=eta_h, ete_m=eta_m, ete_s=eta_s)

                current_fuel -= float(d[f'fuel_{i}'])
                d[f"fuel_rem_{i}"] = f"{current_fuel:.1f}"

            departure_info = airport_info[origin_airport]
            destination_info = airport_info[destination_airport]
            d["departure_name"] = origin_airport
            d["destination_name"] = destination_airport
            d["departure_atis"] = departure_info.get("atis", "")
            d["departure_ground"] = departure_info.get("ground", "")
            d["departure_tower"] = departure_info.get("tower", "")
            d["departure_ctaf"] = departure_info.get("ctaf", "")
            d["departure_field_elevation"] = departure_info.get("elevation", "")
            d["destination_atis"] = destination_info.get("atis", "")
            d["destination_tower"] = destination_info.get("tower", "")
            d["destination_ground"] = destination_info.get("ground", "")
            d["destination_ctaf"] = destination_info.get("ctaf", "")
            d["destination_field_elevation"] = destination_info.get("elevation", "")

            d["departure_runway"] = departure_info.get("runway", "")
            d["destination_runway"] = destination_info.get("runway", "")

            d["check_vfr"] = True
            d["aircraft_number"] = aircraft_number[1:]  # without the N
            d["2aircraft_identification"] = aircraft_number
            d["3aircraft_type"] = "C172"
            d["4true_airspeed"] = d["tas_2"]
            d["5departure_point"] = origin_airport
            d["6departure_time_proposed"] = f"{data['time']}Z"
            d["7cruising_altitude"] = d["altitude_2"]
            d["8route"] = "DCT"
            d["9destination"] = destination_airport
            d["10ete_hours"], d["10ete_minutes"], _ = hour_to_hours_minutes_seconds(hours=total_time)
            d["11remarks"] = "StudentPilot cross country with instructor - Century Air"
            d["12fuel_hours"], d["12fuel_minutes"], _ = hour_to_hours_minutes_seconds(hours=fuel_time)
            d["13alternate"] = alternate
            d["14pilot"] = data["pilot"]
            d["15num_aboard"] = "2"
            d["16color"] = "W"
            return d

        @staticmethod
        def build_overflown(item):
            checkpoint_indices = [
                int(re.match(
                    pattern=r"checkpoint_(?P<value>.*)",
                    string=key,
                ).groupdict()['value'])
                for key in item.keys() if re.match(
                    pattern=r"checkpoint_(?P<value>.*)",
                    string=key,
                ) is not None
            ]
            numbered_keys_to_copy_point = [
                'checkpoint',
                'vor_ident',
                'vor_freq',
            ]
            numbered_keys_to_copy_leg = [
                'course', 'tas', 'tc',
                'dist_leg', 'wind_dir', 'wind_vel',
                'lr', 'th', 'ew', 'dev', 'mh', 'ch',
                'gs_est', 'altitude',
                'temp', 'ete', 'fuel',
                'dist_rem', 'fuel_rem', 'eta',
            ]
            max_checkpoint = max(checkpoint_indices)
            last_printed_checkpoint = min(max_checkpoint, 9)
            out_data = []
            while max_checkpoint > last_printed_checkpoint:
                data_d = item.copy()
                index_shift = last_printed_checkpoint - 1
                for i in range(1, 10):
                    for key in numbered_keys_to_copy_point:
                        point_index = index_shift + i
                        data_d[f"{key}_{i}"] = "" if point_index > max_checkpoint else data_d[f"{key}_{point_index}"]
                for i in range(1, 9):
                    for key in numbered_keys_to_copy_leg:
                        leg_index = index_shift + i
                        data_d[f"{key}_{i}"] = "" if leg_index >= max_checkpoint else data_d[f"{key}_{leg_index}"]
                last_printed_checkpoint += 8
                out_data.append(data_d)
            return out_data

    navlog_form = FormNavLog()
    navlog_form.build()

    return forms_state
