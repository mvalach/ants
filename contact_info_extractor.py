#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: contact_info_extractor.py
Author: Michal Valach
Date: 2025-01-22
Description: Script extracts phone numbers (US only), contact emails and 
websites from plain text file (e.g. exported emails to .txt) and writes them
to three separate file (.txt)


TODO:
- tune more general regex pattern for phone numbers
- integrate more effective list processing (sets, list comprehention)
- replace hard coding names by cli arguments (parser)
"""

import re

phone_pattern = r'\(?\d{3}\)?[- ]\d{3}[- ]\d{4}'
email_pattern = r'([\w\.]+@\w+\.(com|net|org))'
website_pattern = r'(\s|^)(\w+\.(com|net|org))'

with open('example_email.txt', 'r', encoding="utf-8") as f:
    content = f.read()

phone_matches = re.findall(phone_pattern, content)
email_matches = re.findall(email_pattern, content, re.IGNORECASE)
website_matches = re.findall(website_pattern, content, re.IGNORECASE)

phone_list = []

for phone in phone_matches:
    line = phone + '\n'

    if line not in phone_list:
        phone_list.append(line)

with open('phone_numbers.txt', 'w') as f:
    f.writelines(phone_list)

email_list = []

for email in email_matches:
    line = email[0] + '\n'

    if line not in email_list:
        email_list.append(line)

with open('emails.txt', 'w') as f:
    f.writelines(email_list)

website_list = []

for website in website_matches:
    line = website[1] + '\n'

    if line not in website_list:
        website_list.append(line)

with open('websites.txt', 'w') as f:
    f.writelines(website_list)