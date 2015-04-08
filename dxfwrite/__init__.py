#!/usr/bin/env python
#coding:utf-8
# Purpose: write DXF R12 files
# Based on the ideas of Stani Michiels(Stani) sdxf.py and
# Remigiusz Fiedler(migius) dxflibrary133.py
# Created: 14.03.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

from dxfwrite.const import *
from dxfwrite.base import *
from dxfwrite.engine import DXFEngine


version = "0001"
VERSION = "%s"  % version

#archive original author name
#CYEAR = "2010-2012"
#AUTHOR_NAME = "Manfred Moitzi"
#AUTHOR_EMAIL = "mozman@gmx.at"
CYEAR = "2014"
AUTHOR_NAME = "jet"
AUTHOR_EMAIL = "jet@allartburns.org"
LICENSE = "MIT License"

__author__ = "jet <jet@allartburns.org>"
__doc__ = """A Python library to create DXF R12 drawings.

Copyright %s
Version %s
License %s

IMPLEMENTED R12 WRITING:
- POINT
- LINE
- CIRCLE
- ARC
- TEXT
- SOLID
- TRACE
- FACE3D
- POLYLINE (POLYMESH, POLYFACE)
- BLOCK
- INSERT
- ATTDEF
- ATTRIB

NOT IMPLEMENTED:
- DIMENSION (use LinearDimension, AngularDimension, ArcDimension or
             RadialDimension)
original author: Manfred Moitzi, mozman@gmx.at
maintainer of this branch:
""" % (AUTHOR_NAME, VERSION, LICENSE,)
