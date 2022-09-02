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
            f.write("vN\n")
            f.write("notes\n")
            for i in range(5):
                f.write(f"notes_{i}\n")
            f.write("cas\n")
            f.write("vTime\n")
            f.write("gph\n")
            f.write("departure_atis\n")
            f.write("vATIS\n")
            f.write("vor_ident_1\n")
            f.write("vCheckPoints_1\n")
            f.write("wind_dir_1\n")
            f.write("remaining_distance\n")
            f.write("departure_ceiling_visibility\n")
            f.write("vCeiling\n")
            f.write("tas_1\n")
            f.write("vLR_1\n")
            f.write("vEW_1\n")
            f.write("wind_vel_1\n")
            f.write("vDev_1\n")
            f.write("vLR_2\n")
            f.write("vEW_2\n")
            f.write("vDev_2\n")
            f.write("ch_1\n")
            f.write("dist_leg_1\n")
            f.write("gs_est_1\n")
            f.write("ete_1\n")
            f.write("eta_1\n")
            f.write("fuel_1\n")
            f.write("departure_wind\n")
            f.write("vWind\n")
            f.write("vCheckPoints_2\n")
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
            f.write("vAltimeter\n")
            f.write("vor_freq_2\n")
            f.write("course_2\n")
            f.write("altitude_2\n")
            f.write("wind_dir_2\n")
            f.write("wind_vel_2\n")
            f.write("tas_2\n")
            f.write("vLR_3\n")
            f.write("vEW_3\n")
            f.write("vDev_3\n")
            f.write("vLR_4\n")
            f.write("vor_ident_3\n")
            f.write("vEW_4\n")
            f.write("vDev_4\n")
            f.write("ch_2\n")
            f.write("dist_leg_2\n")
            f.write("gs_est_2\n")
            f.write("ete_2\n")
            f.write("eta_2\n")
            f.write("fuel_2\n")
            f.write("departure_approach\n")
            f.write("vApproach\n")
            f.write("vCheckPoints_3\n")
            f.write("temp_2\n")
            f.write("dist_rem_2\n")
            f.write("gs_act_2\n")
            f.write("ate_2\n")
            f.write("ata_2\n")
            f.write("fuel_rem_2\n")
            f.write("departure_runway\n")
            f.write("vRunway\n")
            f.write("vor_freq_3\n")
            f.write("course_3\n")
            f.write("altitude_3\n")
            f.write("wind_dir_3\n")
            f.write("wind_vel_3\n")
            f.write("tas_3\n")
            f.write("vLR_5\n")
            f.write("vEW_5\n")
            f.write("vDev_5\n")
            f.write("vLR_6\n")
            f.write("vEW_6\n")
            f.write("vDev_6\n")
            f.write("ch_3\n")
            f.write("dist_leg_3\n")
            f.write("gs_est_3\n")
            f.write("ete_3\n")
            f.write("eta_3\n")
            f.write("fuel_3\n")
            f.write("departure_timecheck\n")
            f.write("vCheckPoints_4\n")
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
            f.write("vLR_7\n")
            f.write("vEW_7\n")
            f.write("vDev_7\n")
            f.write("vLR_8\n")
            f.write("vEW_8\n")
            f.write("vDev_8\n")
            f.write("ch_4\n")
            f.write("dist_leg_4\n")
            f.write("gs_est_4\n")
            f.write("ete_4\n")
            f.write("eta_4\n")
            f.write("fuel_4\n")
            f.write("vCheckPoints_5\n")
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
            f.write("vLR_9\n")
            f.write("vEW_9\n")
            f.write("vDev_9\n")
            f.write("vLR_10\n")
            f.write("vEW_10\n")
            f.write("vDev_10\n")
            f.write("ch_5\n")
            f.write("dist_leg_5\n")
            f.write("gs_est_5\n")
            f.write("ete_5\n")
            f.write("eta_5\n")
            f.write("fuel_5\n")
            f.write("departure_atis\n")
            f.write("destination_atis\n")

            f.write("vCheckPoints_6\n")
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

            f.write("vLR_11\n")
            f.write("vEW_11\n")
            f.write("vDev_11\n")
            f.write("vLR_12\n")
            f.write("vEW_12\n")
            f.write("vDev_12\n")

            f.write("ch_6\n")
            f.write("dist_leg_6\n")
            f.write("gs_est_6\n")
            f.write("ete_6\n")
            f.write("eta_6\n")
            f.write("fuel_6\n")

            f.write("departure_tower\n")
            f.write("destination_tower\n")

            f.write("vCheckPoints_7\n")
            f.write("vor_ident_7\n")
            f.write("temp_6\n")
            f.write("dist_rem_6\n")
            f.write("gs_act_6\n")
            f.write("ate_6\n")
            f.write("ata_6\n")
            f.write("fuel_rem_6\n")

            for i in range(500):
                f.write(f"{i}\n")


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
