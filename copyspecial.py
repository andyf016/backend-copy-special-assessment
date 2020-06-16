#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Andrew Fillenwarth, thanks to Kano and Mike A. for the help!"

import re
import os
import sys
import shutil
import subprocess
import argparse

special_files = []


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    special_pattern = re.compile(r'__\w+__')
    with os.scandir(dirname) as entries:
        for entry in entries:
            if special_pattern.findall(entry.path):
                special_files.append(os.path.abspath(entry.path))
    return special_files


def copy_to(path_list, dest_dir):
    """ Copy special files to destination directory """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for item in path_list:
        shutil.copy(item, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """ Combine special files into a .zip"""
    commands_with_paths = ['zip', '-j', dest_zip] + path_list
    subprocess.run(commands_with_paths)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--fromdir', help='source directory for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    dest_dir = ns.todir
    dest_zip = ns.tozip
    source_dir = ns.fromdir
    files = get_special_paths(source_dir)
    if dest_dir:
        copy_to(files, dest_dir)
    if dest_zip:
        zip_to(files, dest_zip)
    else:
        for item in special_files:
            print(item)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
