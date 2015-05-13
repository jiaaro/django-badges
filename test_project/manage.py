#!/usr/bin/env python
import os
import sys
from os.path import dirname, abspath, join

PROJECT_ROOT = abspath(dirname(__file__))
sys.path.insert(0, join(PROJECT_ROOT, '..'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
