#!/bin/busybox sh
echo Content-type: text/html
echo
 

/killall openvpn
/etc/init.d/openvpn stop
rm /tmp/openvpn.log





echo Disconnected.

