#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re


# Split raw text into a list of pages according to the original PDF
def split_pages(text):
    # Split text into pages
    page_pattern = re.compile("ANNEX \d+: ADMESOS Pàg. \d+")
    pages_list = page_pattern.split(text)
    # Remove empty list elements
    non_empty_pattern = re.compile("[A-Za-zÀ-ú0-9]+")
    clean_pages_list = [page for page in pages_list
                        if non_empty_pattern.search(page)]
    return clean_pages_list


# Split page text into a list of candidates
def split_candidates_from_pages(page_text):
    # Split candidates
    candidate_pattern = re.compile("AP. 232 [0-9]{2}\.[0-9]{4}")
    candidates_list = candidate_pattern.split(page_text)
    # Remove empty list elements
    non_empty_pattern = re.compile("[A-Za-zÀ-ú0-9]+")
    clean_candidates_list = [candidate for candidate in candidates_list
                             if non_empty_pattern.search(candidate)]
    return clean_candidates_list


# Spit raw text into a list of candidates
def split_candidates_from_raw_text(text):
    # Split pages
    pages_list = split_pages(text)
    # Split candidates
    candidates_list = []
    for page in pages_list:
        candidates_list.extend(split_candidates_from_pages(page))
    return candidates_list
