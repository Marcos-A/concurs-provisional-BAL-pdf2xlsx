#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re


# Get candidate's name
def extract_candidate_name(candidate_text):
    name_pattern = re.compile(
        "[A-Za-zÀ-ú-]+\s*[A-Za-zÀ-ú-]*,\s+[A-Za-zÀ-úª\.-]+\s*[A-Za-zÀ-úª\.-]*\s*[A-Za-zÀ-úª\.-]*\s*[A-Za-zÀ-úª\.-]*(?<=[A-Za-zÀ-úª\.-])")
    name = name_pattern.search(candidate_text).group()
    return name


# Get candidate's teaching specialty code and name
def extract_candidate_specialty(candidate_text):
    specialty_pattern = re.compile("[0-9]+\s-\s[A-ZÀ-Ú\s,·']+(?<=[A-ZÀ-Ú])[^\s'REG.']")
    specialty = specialty_pattern.search(candidate_text).group()
    return specialty


# Get candidate's teaching specialty code and name from the candidate specialty
def extract_code_and_name_from_candidate_specialty(candidate_specialty):
    specialty_code = candidate_specialty.split(" - ")[0]
    specialty_name = candidate_specialty.split(" - ")[1]
    return [specialty_code, specialty_name]


# Get candidate's teaching specialty code and name from the raw candidate text
def extract_candidate_specialty_code_and_name(candidate_text):
    specialty = extract_candidate_specialty(candidate_text)
    return extract_code_and_name_from_candidate_specialty(specialty)


# Get candidate's score
def extract_candidate_score(candidate_text):
    score_pattern = re.compile("PUNTS TOTALS\s+([0-9]{2}[\.][0-9]{4})")
    score = score_pattern.findall(candidate_text)[0]
    return score
