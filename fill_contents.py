import os
import json
from utils.forms_constants import *
from utils.forms_utils import fill_pdf_from_keys, logging, process_logger, map_folders, load_keys, \
    output_pdf_folder, flat_pdf_folder
from pdfrw import PdfReader, PdfWriter
from utils.forms_core import fill_contents
from utils.utils_selenium import flatten_with_chrome


logger = logging.getLogger('fill_contents')
process_logger(logger, file_name='fill_contents')


def fill_pdfs(forms_state, folder):
    map_folders(output_pdf_folder)
    output_folder = os.path.join(output_pdf_folder, folder)
    map_folders(output_folder)

    all_out_files = []
    for f, d_contents in forms_state.items():
        d_mapping = load_keys(os.path.join(forms_folder, f + keys_extension))

        def fill_one_pdf(contents, suffix=""):
            ddd = {k: contents[val[0]] for k, val in d_mapping.items() if val[0] in contents}
            outfile = os.path.join(output_folder, f + suffix + pdf_extension)
            all_out_files.append(outfile)
            fill_pdf_from_keys(
                file=os.path.join(forms_folder, f + pdf_extension),
                out_file=outfile,
                d=ddd,
            )
        if isinstance(d_contents, list):
            for i, one_content in enumerate(d_contents):
                fill_one_pdf(one_content, "_" + str(i))
        elif isinstance(d_contents, dict):
            fill_one_pdf(d_contents)
    return all_out_files


def flatten_pdfs(files, folder_for_chrome):
    for file in files:
        full_file = os.path.join(os.getcwd(), file)
        flatten_with_chrome(file=full_file, folder=folder_for_chrome)


def merge_pdfs(files, out):
    writer = PdfWriter()
    for inpfn in files:
        writer.addpages(PdfReader(inpfn).pages)
    writer.write(out)


def flatten_and_merge(files, outfile):
    folder_for_chrome = os.path.join(os.getcwd(), flat_pdf_folder)
    if not os.path.isdir(folder_for_chrome):
        os.mkdir(folder_for_chrome)
    flatten_pdfs(files=files, folder_for_chrome=folder_for_chrome)
    flat_files = [os.path.join(folder_for_chrome, x) for x in os.listdir(folder_for_chrome)]
    merge_pdfs(files=flat_files, out=outfile)
    for f in flat_files:
        os.remove(f)


def gather_inputs(input_folder):
    input_folder = os.path.join("input_data", input_folder)
    j = json.load(open(os.path.join(input_folder, 'input.json'), 'rb'))

    additional_info = {}

    override_stuff = {}

    data = {}
    data.update(j)
    data.update(additional_info)
    data[override_keyword] = override_stuff

    return data


def main():
    data = gather_inputs(input_folder="stuff")
    formatted_data = fill_contents(data)
    pdf_files = fill_pdfs(formatted_data, "stuff")
    outfile = "forms" + "out" + pdf_extension
    flatten_and_merge(files=pdf_files, outfile=outfile)


if __name__ == "__main__":
    main()
