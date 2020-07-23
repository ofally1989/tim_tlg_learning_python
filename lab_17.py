ipchk = "192.168.0.1"
if ipchk:
    print("Looks like the IP address was set: " + ipchk)

ipchk = input("Apply an IP address: ")
if ipchk:
    print("looks like the ip address was set: " + ipchk)
else:
    print("You did not provide input.")
if ipchk == "192.168.70.1":
    print("You have used the gateway address for the IP address " + ipchk + " You can not do this.")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input.")
