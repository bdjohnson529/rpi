-----
Set up RPi as a Wireless AP
-----

Taken from: https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/

THOUGHTS
-----
This setup uses DNSMasq as the DHCP daemon. We disable the DHCPD daemon and enable DNSMasq.

FILES
-----
1. Hostapd
/etc/default/hostapd
	*sets default path for hostapd.conf

/etc/hostapd/hostapd.conf
	*configures hostapd

2. Interfaces
/etc/network/interfaces
	*used by ifdown and ifup
	*bridge is defined here

3. DHCPCD
/etc/dhcpcd.conf
	*defines wlan0 interface
	*tells dhcp daemon to ignore eth0, wlan0

4. DNSMasq
/etc/dnsmasq.conf
	*configures DNSMasq daemon

5. IP Routing
/etc/iptables.ipv4.nat
	*routes IP
