#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Andrew Fillenwarth, thanks to Kano and Mike A. for the help! \
              also thanks to Daniel for the study hall"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    paths = os.listdir(dirname)
    special_paths = []
    for filename in paths:
        match = re.search(r'__\w+__', filename)
        if match:
            special_paths.append(os.path.abspath(
                os.path.join(dirname, filename)))
    return special_paths


def copy_to(path_list, dest_dir):
    """ Copy special files to destination directory """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for item in path_list:
        shutil.copy(item, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """zip special files."""
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    print('Command im going to do:')
    print(' '.join(cmd))
    subprocess.check_output(cmd)
    return


def main(args):
    """Main driver code for copyspecial."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='source directory for special files')
    ns = parser.parse_args(args)
    special_paths = get_special_paths(ns.from_dir)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    else:
        print('\n'.join(special_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
