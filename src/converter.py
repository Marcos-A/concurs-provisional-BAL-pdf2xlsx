#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from miners import create_df_from_text
    

# Export dataframe as Excel file
def export_text_to_xlsx(text, xlsx_file_full_path):
    df = create_df_from_text(text)
    df.to_excel(xlsx_file_full_path, index=False)
    