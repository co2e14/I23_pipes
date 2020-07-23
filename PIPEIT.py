#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Christian M. Orr
"""

import os


os.system("module load global/cluster")
os.system("module load dials")
os.system("module load autoPROC")

resolution = str(0.1)

dataloc = input("Base path to data: ")
xia_andor_autoPROC = str(input("Do you want to run (x)ia2, (a)utoPROC or (b)oth? ").lower)
os.system("cd "+dataloc+"; module load autoPROC; find_images -L -r")


print("Creating subfolders...")
if xia_andor_autoPROC == "x" or "b":
    if not os.path.exists("xia2_dials"):
        os.system("mkdir xia2_dials")
if xia_andor_autoPROC == "x" or "b":
    if not os.path.exists("xia2_xds"):
        os.system("mkdir xia2_xds")
if xia_andor_autoPROC == "a" or "b":
    if not os.path.exists("autoPROC"):
        os.system("mkdir autoPROC")
print("Done")

