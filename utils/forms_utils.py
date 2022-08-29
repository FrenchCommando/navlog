import os
import re
import pdfrw
import glob
from utils.forms_constants import *


def map_folders(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    logger.info("Folders created for %s - Done", name)


def load_keys(file, out_dict=True):
    if out_dict:
        d = {}
    else:
        d = []
    with open(file, 'r') as f:
        logger.info("Loading keys from %s", file)
        for l in f:
            if l[0] == '#':  # ignore comments
                continue
            s = re.split(r'[ \t\n]+', l)
            if out_dict:
                d[s[1]] = s[0], s[2]  # some random stuff at the end
            else:
                d.append((s[0], s[1], s[2]))
    return d


def fill_pdf_from_keys(file, out_file, d):
    # file is the pdf file
    # d is the dictionary mapping the annotation fields to values
    template_pdf = pdfrw.PdfReader(file)

    for annotations in template_pdf.pages:
        if ANNOT_KEY in annotations:
            for annotation in annotations[ANNOT_KEY]:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        if key in d.keys():
                            if annotation[ANNOT_FIELD_TYPE_KEY] == ANNOT_FIELD_TYPE_BTN:
                                if d[key]:
                                    annotation.update(pdfrw.PdfDict(AS=next(iter(annotation['/AP']['/N']))))
                                else:
                                    annotation.update(pdfrw.PdfDict(AS='Off'))
                            elif annotation[ANNOT_FIELD_TYPE_KEY] == ANNOT_FIELD_TYPE_TXT:
                                r = d[key]
                                if isinstance(r, float) and r == round(r):
                                    r = int(r)
                                elif isinstance(r, float) and r != round(r, 2):
                                    r = f'{r:.2f}'
                                annotation.update(
                                    pdfrw.PdfDict(V=f'{r}')
                                )
    try:
        pdfrw.PdfWriter().write(out_file, template_pdf)
        logger.info("Exporting PDF file %s succeeded", out_file)
    except OSError as e:
        logger.error("File must be open %s -- %s", out_file, e)
