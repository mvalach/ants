#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: directory-clean-sweep.py
Author: Michal Valach
Date: 2024-12-18
Description: Basic directory cleanup


TODO:
- more usefull and general cleaning rules update
- integrate more file types
- replace hard coding names by cli arguments (parser)
"""

from pathlib import Path
import shutil

while True:
    root_dir = Path(input("Please enter the target direcoty to cleanup: "))

    if root_dir.exists():
        break

    print("Directory does not exist.")

closet_dir = root_dir / "closet"
closet_dir.mkdir(exist_ok=True)

text_dir = closet_dir / "text_file"
text_dir.mkdir(exist_ok=True)

csv_dir = closet_dir / "csv_file"
csv_dir.mkdir(exist_ok=True)

folders_dir = closet_dir / "folders"
folders_dir.mkdir(exist_ok=True)

for item in root_dir.iterdir():
    if item == closet_dir:
        continue
    elif item.suffix == ".txt":
        shutil.move(item, text_dir)
    elif item.suffix == ".csv":
        shutil.move(item, csv_dir)
    elif "temp" in item.name.lower():
        shutil.rmtree(item)
    elif item.is_dir():
        shutil.move(item, folders_dir / item.name)
    else:
        shutil.move(item, closet_dir)

print("Directory cleanup complete!")
