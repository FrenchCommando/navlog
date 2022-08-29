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
            f.write("aircraft_number\n")
            for i in range(5):
                f.write(f"notes_{i}\n")
            f.write("cas\n")
            for i in range(500):
                f.write(f"stuff_{i}\n")


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
