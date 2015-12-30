#!/home/cdieken/applied_python/bin/python


import pyeapi

def main():

    pynet_sw3 = pyeapi.connect_to("pynet-sw3")
    show_int = pynet_sw3.enable("show interfaces")
    show_int = show_int[0]['result']
    interfaces = show_int['interfaces']

    data_stats = {}
    for interface, int_values in interfaces.items():
        int_counters = int_values.get('interfaceCounters', {})
        data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))


    print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
    for intf, octets in data_stats.items():
        print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])

    print




if __name__ == "__main__":
    main()

