#!/usr/bin/env python

###########
#
# WORK IN PROGRESS!!!
#
###########

try:
    import psutil
except:
    print("\nYou need to install the 'psutil' library.")
    print("Run the following command at the command line:\n\n\t'pip install psutil'\n")
    quit()

import os
import subprocess as s
from collections import namedtuple

def dictPrint(myDict):
    for key, value in myDict.items():
        print(f'\t{key:18}{value}')

##########
# Memory utilization
##########
mem = psutil.virtual_memory()
mem_dict = dict(mem._asdict())
print("\n=================\nMemory Utilization:\n=================")
dictPrint(mem_dict)

##########
# Swap utilization
##########
swap = psutil.swap_memory()
swap_dict = dict(swap._asdict())
print("\n=================\nSwap Utilization:\n=================")
dictPrint(swap_dict)
##########
# CPU Load Average
##########
loadAvg = psutil.getloadavg()
print("\n=================\nLoad Average:\n=================\n",loadAvg)
##########
# CPU Load Average
##########
cpuCount = psutil.cpu_count(logical=False)
print("\n=================\nCPU Count:\n=================\n",cpuCount)
##########
# CPU Statistics
##########
cpuStats = psutil.cpu_stats()
cpuStatsDict = dict(cpuStats._asdict())
print("\n=================\nCPU Statistics:\n=================")
dictPrint(cpuStatsDict)
##########
# Network Information
##########
IPv4RouteTable = os.popen('netstat -nr -4').read()
print("\n=======================\nIPv4 Routing Table\n=======================\n"+IPv4RouteTable)
IPv6RouteTable = os.popen('netstat -nr -6').read()
print("\n=======================\nIPv6 Routing Table\n=======================\n"+IPv6RouteTable)
IPv4NetInt = os.popen('netstat -ntlp -4').read()
print("\n=======================\nIPv4 Network Interfaces\n=======================\n"+IPv4NetInt)
IPv6NetInt = os.popen('netstat -ntlp -6').read()
print("\n=======================\nIPv6 Network Interfaces\n=======================\n"+IPv6NetInt)
##########
# Disk Utilization Information
##########
diskUtil = psutil.disk_usage('/')
diskUtil_dict = dict(diskUtil._asdict())
print("\n=================\nGeneral Disk Usage Stats\n=================")
dictPrint(diskUtil_dict)

