import bluetooth

print("Scanning surronding for hidden devices:")
devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)

for addr, name, device_class in devices:
    print("\n\n")
    print("Device Name: %s" % (name))
    print("Device MAC Address: %s" % (addr))
    print("Device Class: %s" % (device_class))
