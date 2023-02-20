#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
sys.path.append(os.path.join(sys.path[0], 'src'))
from converter import export_text_to_xlsx
from reader import extract_text


RESULT_FILEPATH = os.path.join(os.path.join(sys.path[0]), "processed")
RESULT_FILENAME = "llistat.xlsx"
SOURCE_URL = "https://intranet.caib.es/sites/estabilitzacio/f/413838"


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            source = SOURCE_URL
        else:
            source = sys.argv[1]
        raw_text = extract_text(source)
        export_text_to_xlsx(raw_text, os.path.join(RESULT_FILEPATH, RESULT_FILENAME))
        print("Process completed succesfully.")
    except Exception as e:
        print(e)
