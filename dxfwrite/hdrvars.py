#!/usr/bin/env python
#coding:utf-8
# Purpose: header variables factory
# Created: 20.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

__author__ = "mozman <mozman@gmx.at>"

from functools import partial
from dxfwrite.base import DXFString, DXFInt, DXFFloat, DXFPoint2D, DXFPoint3D

Factory = {
    '$ACADVER': partial(DXFString, group_code=1),
    '$ANGBASE': partial(DXFFloat, group_code=50),
    '$ANGDIR': partial(DXFInt, group_code=70),
    '$ATTDIA': partial(DXFInt, group_code=70),
    '$ATTMODE': partial(DXFInt, group_code=70),
    '$ATTREQ': partial(DXFInt, group_code=70),
    '$AUNITS': partial(DXFInt, group_code=70),
    '$AUPREC': partial(DXFInt, group_code=70),
    '$AXISMODE': partial(DXFInt, group_code=70),
    '$AXISUNIT': DXFPoint2D,
    '$BLIPMODE': partial(DXFInt, group_code=70),
    '$CECOLOR': partial(DXFInt, group_code=62),
    '$CELTYPE': partial(DXFString, group_code=6),
    '$CHAMFERA': partial(DXFFloat, group_code=40),
    '$CHAMFERB': partial(DXFFloat, group_code=40),
    '$CLAYER': partial(DXFString, group_code=8),
    '$COORDS': partial(DXFInt, group_code=70),
    '$DIMALT': partial(DXFInt, group_code=70),
    '$DIMALTD': partial(DXFInt, group_code=70),
    '$DIMALTF': partial(DXFFloat, group_code=40),
    '$DIMAPOST': partial(DXFString, group_code=1),
    '$DIMASO': partial(DXFInt, group_code=70),
    '$DIMASZ': partial(DXFFloat, group_code=40),
    '$DIMBLK': partial(DXFString, group_code=2),
    '$DIMBLK1': partial(DXFString, group_code=1),
    '$DIMBLK2': partial(DXFString, group_code=1),
    '$DIMCEN': partial(DXFFloat, group_code=40),
    '$DIMCLRD': partial(DXFInt, group_code=70),
    '$DIMCLRE': partial(DXFInt, group_code=70),
    '$DIMCLRT': partial(DXFInt, group_code=70),
    '$DIMDLE': partial(DXFFloat, group_code=40),
    '$DIMDLI': partial(DXFFloat, group_code=40),
    '$DIMEXE': partial(DXFFloat, group_code=40),
    '$DIMEXO': partial(DXFFloat, group_code=40),
    '$DIMGAP': partial(DXFFloat, group_code=40),
    '$DIMLFAC': partial(DXFFloat, group_code=40),
    '$DIMLIM': partial(DXFInt, group_code=70),
    '$DIMPOST': partial(DXFString, group_code=1),
    '$DIMRND': partial(DXFFloat, group_code=40),
    '$DIMSAH': partial(DXFInt, group_code=70),
    '$DIMSCALE': partial(DXFFloat, group_code=40),
    '$DIMSE1': partial(DXFInt, group_code=70),
    '$DIMSE2': partial(DXFInt, group_code=70),
    '$DIMSHO': partial(DXFInt, group_code=70),
    '$DIMSOXD': partial(DXFInt, group_code=70),
    '$DIMSTYLE': partial(DXFString, group_code=2),
    '$DIMTAD': partial(DXFInt, group_code=70),
    '$DIMTFAC': partial(DXFFloat, group_code=40),
    '$DIMTIH': partial(DXFInt, group_code=70),
    '$DIMTIX': partial(DXFInt, group_code=70),
    '$DIMTM': partial(DXFFloat, group_code=40),
    '$DIMTOFL': partial(DXFInt, group_code=70),
    '$DIMTOH': partial(DXFInt, group_code=70),
    '$DIMTOL': partial(DXFInt, group_code=70),
    '$DIMTP': partial(DXFFloat, group_code=40),
    '$DIMTSZ': partial(DXFFloat, group_code=40),
    '$DIMTVP': partial(DXFFloat, group_code=40),
    '$DIMTXT': partial(DXFFloat, group_code=40),
    '$DIMZIN': partial(DXFInt, group_code=70),
    '$DWGCODEPAGE': partial(DXFInt, group_code=3),
    '$DRAGMODE': partial(DXFInt, group_code=70),
    '$ELEVATION': partial(DXFFloat, group_code=40),
    '$EXTMAX': DXFPoint3D,
    '$EXTMIN': DXFPoint3D,
    '$FILLETRAD': partial(DXFFloat, group_code=40),
    '$FILLMODE': partial(DXFInt, group_code=70),
    '$HANDLING': partial(DXFInt, group_code=70),
    '$HANDSEED': partial(DXFString, group_code=5),
    '$INSBASE': DXFPoint3D,
    '$LIMCHECK': partial(DXFInt, group_code=70),
    '$LIMMAX': DXFPoint2D,
    '$LIMMIN': DXFPoint2D,
    '$LTSCALE': partial(DXFFloat, group_code=40),
    '$LUNITS': partial(DXFInt, group_code=70),
    '$LUPREC': partial(DXFInt, group_code=70),
    '$MAXACTVP': partial(DXFInt, group_code=70),
    '$MENU': partial(DXFString, group_code=1),
    '$MIRRTEXT': partial(DXFInt, group_code=70),
    '$ORTHOMODE': partial(DXFInt, group_code=70),
    '$OSMODE': partial(DXFInt, group_code=70),
    '$PDMODE': partial(DXFInt, group_code=70),
    '$PDSIZE': partial(DXFFloat, group_code=40),
    '$PELEVATION': partial(DXFFloat, group_code=40),
    '$PEXTMAX': DXFPoint3D,
    '$PEXTMIN': DXFPoint3D,
    '$PLIMCHECK': partial(DXFInt, group_code=70),
    '$PLIMMAX': DXFPoint2D,
    '$PLIMMIN': DXFPoint2D,
    '$PLINEGEN': partial(DXFInt, group_code=70),
    '$PLINEWID': partial(DXFFloat, group_code=40),
    '$PSLTSCALE': partial(DXFInt, group_code=70),
    '$PUCSNAME': partial(DXFString, group_code=2),
    '$PUCSORG': DXFPoint3D,
    '$PUCSXDIR': DXFPoint3D,
    '$PUCSYDIR': DXFPoint3D,
    '$QTEXTMODE': partial(DXFInt, group_code=70),
    '$REGENMODE': partial(DXFInt, group_code=70),
    '$SHADEDGE': partial(DXFInt, group_code=70),
    '$SHADEDIF': partial(DXFInt, group_code=70),
    '$SKETCHINC': partial(DXFFloat, group_code=40),
    '$SKPOLY': partial(DXFInt, group_code=70),
    '$SPLFRAME': partial(DXFInt, group_code=70),
    '$SPLINESEGS': partial(DXFInt, group_code=70),
    '$SPLINETYPE': partial(DXFInt, group_code=70),
    '$SURFTAB1': partial(DXFInt, group_code=70),
    '$SURFTAB2': partial(DXFInt, group_code=70),
    '$SURFTYPE': partial(DXFInt, group_code=70),
    '$SURFU': partial(DXFInt, group_code=70),
    '$SURFV': partial(DXFInt, group_code=70),
    '$TDCREATE': partial(DXFFloat, group_code=40),
    '$TDINDWG': partial(DXFFloat, group_code=40),
    '$TDUPDATE': partial(DXFFloat, group_code=40),
    '$TDUSRTIMER': partial(DXFFloat, group_code=40),
    '$TEXTSIZE': partial(DXFFloat, group_code=40),
    '$TEXTSTYLE': partial(DXFString, group_code=7),
    '$THICKNESS': partial(DXFFloat, group_code=40),
    '$TILEMODE': partial(DXFInt, group_code=70),
    '$TRACEWID': partial(DXFFloat, group_code=40),
    '$UCSNAME': partial(DXFString, group_code=2),
    '$UCSORG': DXFPoint3D,
    '$UCSXDIR': DXFPoint3D,
    '$UCSYDIR': DXFPoint3D,
    '$UNITMODE': partial(DXFInt, group_code=70),
    '$USERI1': partial(DXFInt, group_code=70),
    '$USERI2': partial(DXFInt, group_code=70),
    '$USERI3': partial(DXFInt, group_code=70),
    '$USERI4': partial(DXFInt, group_code=70),
    '$USERR1': partial(DXFFloat, group_code=40),
    '$USERR2': partial(DXFFloat, group_code=40),
    '$USERR3': partial(DXFFloat, group_code=40),
    '$USERR4': partial(DXFFloat, group_code=40),
    '$USERR5': partial(DXFFloat, group_code=40),
    '$USRTIMER': partial(DXFInt, group_code=70),
    '$VISRETAIN': partial(DXFInt, group_code=70),
    '$WORLDVIEW': partial(DXFInt, group_code=70),
}