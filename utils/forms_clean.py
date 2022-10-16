import os
import shutil
from utils.forms_constants import keys_extension, key_mapping_folder, \
    fields_mapping_folder, log_extension, json_extension, output_pdf_folder, input_json_name, flat_pdf_folder


def remove_by_extension(extension):
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(extension):
                try:
                    os.remove(os.path.join(root, file))
                except PermissionError as e:
                    print(e)


def remove_folder(folder):
    shutil.rmtree(folder)


def clean():
    # remove input json files
    remove_by_extension(extension=input_json_name)

    # remove log files
    remove_by_extension(extension=log_extension)  # log files are in use, haha
    # remove keys files
    remove_by_extension(extension=keys_extension)

    # remove key_mapping folder
    remove_folder(folder=key_mapping_folder)
    # remove fields_mapping folder
    remove_folder(folder=fields_mapping_folder)
    # remove output folder
    remove_folder(folder=output_pdf_folder)
    remove_folder(folder=flat_pdf_folder)
