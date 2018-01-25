from scapy.all import *
from optparse import OptionParser
import sys
def main():
    usage = "Usage: [-i interface] [-t targetip] [-g gatewayip]"
    parser = OptionParser(usage)
    parse.add_option('-i',dest='interface')
