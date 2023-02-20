#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
TODO: 
- Add column indicating if candidate has other specialties
  and his/her ranking position for everyone of them.
- Add column with total available positions by specialty. (?)
"""

import numpy as np
import pandas as pd
from parsers import extract_candidate_name, \
                    extract_candidate_specialty_code_and_name, \
                    extract_candidate_specialty, \
                    extract_candidate_score
from printers import catch_exception, \
                     create_tie_warning_message
                     
from splitters import split_candidates_from_raw_text                 


# Create a dataframe from raw text
def create_df_from_text(text):
    # Create an empy dataframe    
    df = pd.DataFrame(columns = ["nom", "especialitat", "especialitat (codi)", "especialitat (nom)", "puntuació"])
        
    # Fill the dataframe with candidates data
    candidates_list = split_candidates_from_raw_text(text)
    for candidate in candidates_list:
        try:
            candidate_dict = {"nom": extract_candidate_name(candidate),
                              "especialitat": extract_candidate_specialty(candidate),
                              "especialitat (codi)": 
                                  extract_candidate_specialty_code_and_name(candidate)[0],
                              "especialitat (nom)":
                                  extract_candidate_specialty_code_and_name(candidate)[1],
                              "puntuació": extract_candidate_score(candidate)}
            df = pd.concat([df, pd.DataFrame([candidate_dict.values()], columns = df.columns)],
                        ignore_index=True)
        except Exception as e:
            catch_exception(e)
    df = set_df_numeric_data_types(df)
    df = df_sort_by_column_with_non_ascii_chars_and_regular_column(
                            df, "especialitat (nom)", "puntuació", regular_column_ascending=False)
    # Reassign index according to new sorting
    df.reset_index(drop=True, inplace=True)
    df = rank_candidates(df)
    df = add_other_specialties(df)
    df = df.drop("especialitat (codi)", axis=1)
    df = df.drop("especialitat (nom)", axis=1)
    return df


# Assign numeric data types to columns with numeric values
def set_df_numeric_data_types(df):
    try:
        df.loc[:, "especialitat (codi)"] = df.loc[:, "especialitat (codi)"].astype(int)
        df.loc[:, "puntuació"] = df["puntuació"].astype(float)
    except Exception as e:
        print(e)
    return df


# Sort dataframe according to a columns with non-ASCII chars and then to a regular column
def df_sort_by_column_with_non_ascii_chars_and_regular_column(df, non_ascii_chars_column, regular_column,
                                                              non_ascii_chars_column_ascending=True,
                                                              regular_column_ascending=True):
    try:
        # Create new column with normalized non-ASCII chars
        df["especialitat (nom sense accents)"] = df["especialitat (nom)"].str.normalize('NFKD')\
                                                .str.encode('ascii', errors='ignore')\
                                                .str.decode('utf-8')
        # Sort first by columns with normalized non-ASCII chars, then by regular column
        df = df.sort_values(by = ["especialitat (nom sense accents)", "puntuació"],
                            ascending = [True, False])
        # Delete column with normalized non-ASCII chars
        df = df.drop("especialitat (nom sense accents)", axis=1)
    except Exception as e:
        catch_exception(e)
    return df


# Add ranking position for every candidate at each specialty
def rank_candidates(df):
    try:
        # Create a new empty column for the ranking position
        df["posició"] = np.nan
        # Get the list of specialties
        specialties_list = df["especialitat"].unique()
        # Rank candidates for every specialty
        for specialty in specialties_list:
            specialty_df = df.loc[df["especialitat"] == specialty]
            for position, candidate_idx in enumerate(specialty_df.to_dict(orient="index"), start=1):
                df["posició"].iat[candidate_idx] = position
        # Set integer date type to ranking position column
        df["posició"] = df["posició"].astype(int)    
        df = detect_ties(df)
    except Exception as e:
        catch_exception(e)
    return df


# Detect score ties in the same specialty an adds an observation
def detect_ties(df):
    try:
        # Create a new empty column for the tie-related observations
        df["observacions"] = ""
        # Get the list of specialties
        specialties_list = df["especialitat"].unique()
        # For each specialty, check if there exist other candidates with the same score;
        # if so, add an observation
        for specialty in specialties_list:
            specialty_df = df.loc[df["especialitat"] == specialty]
            for candidate_idx in specialty_df.to_dict(orient="index"):
                if (len(specialty_df.loc[specialty_df["puntuació"] == df["puntuació"].iat[candidate_idx]]) > 1):         
                    df["observacions"].iat[candidate_idx] = create_tie_warning_message(
                        len(specialty_df.loc[specialty_df["puntuació"] == df["puntuació"].iat[candidate_idx]]))
    except Exception as e:
        catch_exception(e)
    return df

# Check for other candidate's specialties and add them with his/her rankings
def add_other_specialties(df):
    try:
        # Create a new empty column to include other candidate's specialties
        df["altres especialitats"] = ""
        # Get the list of candidates
        candidates_list = df["nom"].unique()
        for candidate in candidates_list:
            # Get a list of the candidate's specialties if he/she has more than one
            if (len(df.loc[df["nom"] == candidate]) > 1):
                applications_df = df.loc[df["nom"] == candidate]
                applications_idx_list = applications_df.index.values.tolist()
                # Add to every candidate's specialty a comment including his/her other
                # specialties and respective rankings 
                for target_application_idx in applications_idx_list:
                    comment = ""
                    for application_idx in applications_df.to_dict(orient="index"):
                        if (application_idx != target_application_idx):
                            if comment:
                                comment += ", "
                            comment += df.iloc[application_idx]["especialitat"] + \
                                       " (pos. " + str(df.iloc[application_idx]["posició"]) + ")"

                    df["altres especialitats"].iat[target_application_idx] = comment
    except BaseException as e:
        catch_exception(str(e))
    return df
