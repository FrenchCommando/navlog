# creates fields files to map values from unprocessed keys files
# the fields file then contains the names of the fields to be mapped
# with a clear syntax to describe tables and dollar/cents splits

from utils.forms_utils import *


def create_empty_fields():
    for u in glob.glob(os.path.join(key_mapping_folder, "*")):
        if u.endswith(keys_extension):
            rel = os.path.relpath(u, key_mapping_folder)
            rel_fields = os.path.join(fields_mapping_folder, rel)
            fields_name = os.path.splitext(rel_fields)[0] + fields_extension
            try:
                open(fields_name, 'x')
                logger.info("Created fields file for %s", fields_name)
            except FileExistsError as e:
                logger.debug("Creating fields file for %s -- %s", fields_name, e)
        else:
            logger.info("File ignored %s", u)


def fill_fields_files():
    for u in glob.glob(os.path.join(fields_mapping_folder, "*" + fields_extension)):
        logger.info("Filling fields %s", u)
        with open(u, 'w') as f:
            f.write("checkpoint_1\n")
            f.write("aircraft_number\n")
            f.write("notes\n")
            for i in range(5):
                f.write(f"notes_{i}\n")
            f.write("cas\n")
            f.write("time_off\n")
            f.write("gph\n")
            f.write("departure_ATIScode\n")
            f.write("destination_ATIScode\n")
            f.write("vor_ident_1\n")
            f.write("vor_freq_1\n")
            f.write("wind_dir_1\n")
            f.write("remaining_distance\n")
            f.write("departure_ceiling_visibility\n")
            f.write("destination_ceiling\n")
            f.write("tas_1\n")
            f.write("tc_1\n")
            f.write("th_1\n")
            f.write("wind_vel_1\n")
            f.write("mh_1\n")
            f.write("lr_1\n")
            f.write("ew_1\n")
            f.write("dev_1\n")
            f.write("ch_1\n")
            f.write("dist_leg_1\n")
            f.write("gs_est_1\n")
            f.write("ete_1\n")
            f.write("eta_1\n")
            f.write("fuel_1\n")
            f.write("departure_wind\n")
            f.write("destination_wind\n")
            f.write("checkpoint_2\n")
            f.write("vor_ident_2\n")
            f.write("course_1\n")
            f.write("altitude_1\n")
            f.write("temp_1\n")
            f.write("dist_rem_1\n")
            f.write("gs_act_1\n")
            f.write("ate_1\n")
            f.write("ata_1\n")
            f.write("fuel_rem_1\n")
            f.write("departure_altimeter\n")
            f.write("destination_altimeter\n")
            f.write("vor_freq_2\n")
            f.write("course_2\n")
            f.write("altitude_2\n")
            f.write("wind_dir_2\n")
            f.write("wind_vel_2\n")
            f.write("tas_2\n")
            f.write("tc_2\n")
            f.write("th_2\n")
            f.write("mh_2\n")
            f.write("lr_2\n")
            f.write("vor_ident_3\n")
            f.write("ew_2\n")
            f.write("dev_2\n")
            f.write("ch_2\n")
            f.write("dist_leg_2\n")
            f.write("gs_est_2\n")
            f.write("ete_2\n")
            f.write("eta_2\n")
            f.write("fuel_2\n")
            f.write("departure_approach\n")
            f.write("destination_approach\n")
            f.write("checkpoint_3\n")
            f.write("temp_2\n")
            f.write("dist_rem_2\n")
            f.write("gs_act_2\n")
            f.write("ate_2\n")
            f.write("ata_2\n")
            f.write("fuel_rem_2\n")
            f.write("departure_runway\n")
            f.write("destination_runway\n")
            f.write("vor_freq_3\n")
            f.write("course_3\n")
            f.write("altitude_3\n")
            f.write("wind_dir_3\n")
            f.write("wind_vel_3\n")
            f.write("tas_3\n")
            f.write("tc_3\n")
            f.write("th_3\n")
            f.write("mh_3\n")
            f.write("lr_3\n")
            f.write("ew_3\n")
            f.write("dev_3\n")
            f.write("ch_3\n")
            f.write("dist_leg_3\n")
            f.write("gs_est_3\n")
            f.write("ete_3\n")
            f.write("eta_3\n")
            f.write("fuel_3\n")
            f.write("departure_timecheck\n")
            f.write("checkpoint_4\n")
            f.write("vor_ident_4\n")
            f.write("temp_3\n")
            f.write("dist_rem_3\n")
            f.write("gs_act_3\n")
            f.write("ate_3\n")
            f.write("ata_3\n")
            f.write("fuel_rem_3\n")
            f.write("vor_freq_4\n")
            f.write("course_4\n")
            f.write("altitude_4\n")
            f.write("wind_dir_4\n")
            f.write("wind_vel_4\n")
            f.write("tc_4\n")
            f.write("th_4\n")
            f.write("mh_4\n")
            f.write("lr_4\n")
            f.write("ew_4\n")
            f.write("dev_4\n")
            f.write("ch_4\n")
            f.write("dist_leg_4\n")
            f.write("gs_est_4\n")
            f.write("ete_4\n")
            f.write("eta_4\n")
            f.write("fuel_4\n")
            f.write("checkpoint_5\n")
            f.write("vor_ident_5\n")
            f.write("temp_4\n")
            f.write("tas_4\n")
            f.write("dist_rem_4\n")
            f.write("gs_act_4\n")
            f.write("ate_4\n")
            f.write("ata_4\n")
            f.write("fuel_rem_4\n")

            f.write("departure_name\n")
            f.write("destination_name\n")

            f.write("vor_freq_5\n")
            f.write("course_5\n")
            f.write("altitude_5\n")
            f.write("wind_dir_5\n")
            f.write("wind_vel_5\n")
            f.write("tas_5\n")
            f.write("tc_5\n")
            f.write("th_5\n")
            f.write("mh_5\n")
            f.write("lr_5\n")
            f.write("ew_5\n")
            f.write("dev_5\n")
            f.write("ch_5\n")
            f.write("dist_leg_5\n")
            f.write("gs_est_5\n")
            f.write("ete_5\n")
            f.write("eta_5\n")
            f.write("fuel_5\n")
            f.write("departure_atis\n")
            f.write("destination_atis\n")

            f.write("checkpoint_6\n")
            f.write("vor_ident_6\n")
            f.write("temp_5\n")
            f.write("dist_rem_5\n")
            f.write("gs_act_5\n")
            f.write("ate_5\n")
            f.write("ata_5\n")
            f.write("fuel_rem_5\n")

            f.write("departure_ground\n")
            f.write("destination_ground\n")

            f.write("vor_freq_6\n")
            f.write("course_6\n")
            f.write("altitude_6\n")
            f.write("wind_dir_6\n")
            f.write("wind_vel_6\n")
            f.write("tas_6\n")

            f.write("tc_6\n")
            f.write("th_6\n")
            f.write("mh_6\n")
            f.write("lr_6\n")
            f.write("ew_6\n")
            f.write("dev_6\n")

            f.write("ch_6\n")
            f.write("dist_leg_6\n")
            f.write("gs_est_6\n")
            f.write("ete_6\n")
            f.write("eta_6\n")
            f.write("fuel_6\n")

            f.write("departure_tower\n")
            f.write("destination_tower\n")

            f.write("checkpoint_7\n")
            f.write("vor_ident_7\n")
            f.write("temp_6\n")
            f.write("dist_rem_6\n")
            f.write("gs_act_6\n")
            f.write("ate_6\n")
            f.write("ata_6\n")
            f.write("fuel_rem_6\n")

            f.write("departure_departure\n")
            f.write("destination_ground\n")

            f.write("vor_freq_7\n")
            f.write("course_7\n")
            f.write("altitude_7\n")
            f.write("wind_dir_7\n")
            f.write("wind_vel_7\n")
            f.write("tas_7\n")

            f.write("tc_7\n")
            f.write("th_7\n")
            f.write("mh_7\n")
            f.write("lr_7\n")
            f.write("ew_7\n")
            f.write("dev_7\n")

            f.write("ch_7\n")
            f.write("dist_leg_7\n")
            f.write("gs_est_7\n")
            f.write("ete_7\n")
            f.write("eta_7\n")
            f.write("fuel_7\n")

            f.write("departure_ctaf\n")
            f.write("destination_ctaf\n")

            f.write("checkpoint_8\n")
            f.write("vor_ident_8\n")
            f.write("temp_7\n")
            f.write("dist_rem_7\n")
            f.write("gs_act_7\n")
            f.write("ate_7\n")
            f.write("ata_7\n")
            f.write("fuel_rem_7\n")

            f.write("departure_fss\n")
            f.write("destination_fss\n")

            f.write("vor_freq_8\n")
            f.write("course_8\n")
            f.write("altitude_8\n")
            f.write("wind_dir_8\n")
            f.write("wind_vel_8\n")
            f.write("tas_8\n")

            f.write("tc_8\n")
            f.write("th_8\n")
            f.write("mh_8\n")
            f.write("lr_8\n")
            f.write("ew_8\n")
            f.write("dev_8\n")

            f.write("ch_8\n")
            f.write("dist_leg_8\n")
            f.write("gs_est_8\n")
            f.write("ete_8\n")
            f.write("eta_8\n")
            f.write("fuel_8\n")

            f.write("departure_unicom\n")
            f.write("destination_unicom\n")

            f.write("temp_8\n")

            f.write("checkpoint_9\n")
            f.write("vor_ident_9\n")
            f.write("dist_rem_8\n")
            f.write("gs_act_8\n")
            f.write("ate_8\n")
            f.write("ata_8\n")
            f.write("fuel_rem_8\n")

            f.write("departure_field_elevation\n")
            f.write("destination_field_elevation\n")

            f.write("vor_freq_9\n")

            f.write("total_rem\n")
            f.write("total_act\n")
            f.write("total_ate\n")
            f.write("total_ata\n")
            f.write("total_fuel\n")

            f.write("block_in\n")
            f.write("vFlightPlan\n")
            f.write("block_out\n")
            f.write("log_time\n")

            f.write("weather_departure_reported\n")
            f.write("weather_departure_forecast\n")
            f.write("weather_departure_winds_aloft\n")
            f.write("weather_departure_icing\n")
            f.write("weather_departure_turbulence\n")
            f.write("weather_departure_position\n")

            f.write("weather_enroute_reported\n")
            f.write("weather_enroute_forecast\n")
            f.write("weather_enroute_winds_aloft\n")
            f.write("weather_enroute_icing\n")
            f.write("weather_enroute_turbulence\n")
            f.write("weather_enroute_position\n")

            f.write("weather_destination_reported\n")
            f.write("weather_destination_forecast\n")
            f.write("weather_destination_winds_aloft\n")
            f.write("weather_destination_icing\n")
            f.write("weather_destination_turbulence\n")
            f.write("weather_destination_position\n")

            f.write("weather_alternate_reported\n")
            f.write("weather_alternate_forecast\n")
            f.write("weather_alternate_winds_aloft\n")
            f.write("weather_alternate_icing\n")
            f.write("weather_alternate_turbulence\n")
            f.write("weather_alternate_position\n")

            f.write("check_vfr\n")
            f.write("check_ifr\n")
            f.write("check_dvfr\n")

            f.write("2aircraft_identification\n")
            f.write("3aircraft_type\n")
            f.write("4true_airspeed\n")
            f.write("5departure_point\n")

            f.write("notam_0\n")
            f.write("notam_1\n")

            f.write("6departure_time_proposed\n")
            f.write("6departure_time_actual\n")
            f.write("7cruising_altitude\n")
            f.write("8route\n")

            f.write("notam_2\n")
            f.write("notam_3\n")

            f.write("9destination\n")
            f.write("10ete_hours\n")
            f.write("10ete_minutes\n")
            f.write("11remarks\n")

            f.write("notam_4\n")
            f.write("notam_5\n")

            f.write("12fuel_hours\n")
            f.write("12fuel_minutes\n")

            f.write("13alternate\n")
            f.write("14pilot\n")
            f.write("15num_aboard\n")

            f.write("notam_6\n")
            f.write("notam_7\n")
            f.write("notam_8\n")

            f.write("16color\n")
            f.write("17destination\n")

            f.write("notam_9\n")

            f.write("close_vfr\n")
            f.write("report_conditions\n")


def build_keys(file, keys_name, keys_orig):
    # file is the "fields" file
    # keys_orig contains the original keys
    # key_name is the new keys file to be created and overridden
    with open(keys_name, "w+") as out:
        with open(file, 'r') as f:
            d = load_keys(keys_orig, out_dict=False)
            it = iter(d)
            try:
                for command in f:
                    if " " not in command:
                        u = next(it)
                        u = command.strip(), u[1], u[2]
                        out.write("\t\t".join(u) + "\n")
                    else:
                        c = command.strip().split(" ")
                        columns = c[1:]
                        for j in columns:
                            u = next(it)
                            n = c[0] + "_" + j
                            u = n, u[1], u[2]
                            out.write("\t\t".join(u) + "\n")
            except StopIteration as e:
                logger.info(f"Key iteration stopped {e}")


def process_fields(file):
    keys_name = os.path.splitext(file)[0] + keys_extension
    keys_orig = os.path.join(key_mapping_folder, os.path.relpath(keys_name, fields_mapping_folder))

    build_keys(file, keys_name, keys_orig)

    pdf_name = os.path.splitext(file)[0] + pdf_extension
    d = load_keys(keys_orig)
    try:
        d.update(load_keys(keys_name))
        logger.info("Loaded fields names from %s", keys_name)
    except FileNotFoundError as e:
        logger.error(f"{e}")
    for k, (v0, v1) in d.items():
        # if v1 == '/Tx':
        #     d[k] = ('yytt', v1)
        if v1 == '/Btn':
            d[k] = (True, v1)
    pdf_orig = os.path.join(key_mapping_folder, os.path.relpath(pdf_name, fields_mapping_folder))
    fill_pdf_from_keys(file=pdf_orig, out_file=pdf_name, d={k: v[0] for k, v in d.items()})


def generate_keys_pdf():
    for u in glob.glob(os.path.join(fields_mapping_folder, "*")):
        if u.endswith(fields_extension):
            logger.info("Processing fields file %s", u)
            process_fields(u)


def move_keys_to_parent():
    for u in glob.glob(os.path.join(fields_mapping_folder, "*")):
        if u.endswith(keys_extension):
            logger.info("Moving keys file %s", u)
            rel = os.path.relpath(u, fields_mapping_folder)
            folder_path = os.path.join(forms_folder, rel)
            try:
                os.rename(u, folder_path)
                logger.info("Moved  %s to %s", u, folder_path)
            except FileExistsError as e:
                logger.warn(f"Already Exists - Not Moved  {u} to {folder_path} - {e}")


def main():
    map_folders(fields_mapping_folder)
    create_empty_fields()
    fill_fields_files()  # run after defining the fields files
    generate_keys_pdf()
    move_keys_to_parent()  # moves the keys files when done


if __name__ == "__main__":
    main()
