__author__ = 'zhazhich'
from distutils.core import setup
import py2exe
setup(console=["calendar_calendar.py"],
      data_files=[('shifts_calendar_result.txt'),( 'conf.conf')])