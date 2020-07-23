#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Christian M. Orr
"""

import os
from subprocess import PIPE, run

os.system("module load global/cluster")
os.system("module load dials")


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True,
                 shell=True)
    return result.stdout
    print(result)


resolution = str(0.1)

workingdir = os.getcwd()
dataloc = input("Base path to data: ")
xia_andor_autoPROC = str(
        input("Do you want to run (x)ia2, (a)utoPROC or (b)oth? ").lower)

print("Creating subfolders...")
if xia_andor_autoPROC == "x" or "b":
    if not os.path.exists("xia2_dials"):
        os.mkdir("xia2_dials")
if xia_andor_autoPROC == "x" or "b":
    if not os.path.exists("xia2_xds"):
        os.mkdir("xia2_xds")
if xia_andor_autoPROC == "a" or "b":
    if not os.path.exists("autoPROC"):
        os.mkdir("autoPROC")
print("Done")

os.chdir(dataloc)

here = os.popen("module load autoPROC; find_images -L -r").read()
print(here)
os.chdir(os.path.join(workingdir, "autoPROC"))

# =============================================================================
# with open 
#     for line in here:
#         if line.startswith("  -Id ""):
#             output
# 
# =============================================================================
