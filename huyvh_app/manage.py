#!/usr/bin/env python
import os
import sys
from configurations import Configuration
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python.settings")
    #from django.core.management import execute_from_command_line
    from configurations.management import execute_from_command_line
    execute_from_command_line(sys.argv)
