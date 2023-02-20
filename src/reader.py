#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import requests
from tika import parser


# Extract contents of PDF file as raw text
def extract_text(source):
    # regex source: https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    try:
        if url_pattern.match(source):
            response = requests.get(source)
            raw = parser.from_buffer(response.content)
        else:
            raw = parser.from_file(source)
        return raw['content']
    except Exception as e:
        print(e)
    