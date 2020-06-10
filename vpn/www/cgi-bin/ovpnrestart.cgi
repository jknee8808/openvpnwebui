#!/bin/busybox sh
echo Content-type: text/html
echo



procss=`cat /etc/config/network | grep wireguard_wg0`



 

if [ -n "$procss" ]; then

/etc/init.d/network reload
ifdown wg0
ifup wg0

echo wireguard has startetd

else

/etc/init.d/openvpn restart
echo openvpn has restarted

fi