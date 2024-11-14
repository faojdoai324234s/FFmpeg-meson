#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':
    parser = ArgumentParser(description='Copy .rc file to work around RC include precedences')
    parser.add_argument('input', type=Path, help='Input file to patch')

    args = parser.parse_args()

    with args.input.open('r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line.rstrip())
