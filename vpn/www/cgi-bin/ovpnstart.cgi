#!/bin/sh

echo Content-type: text/html
echo

procss=`ps | grep openvpn`



 

if [ -n "$procss" ]; then



/etc/init.d/openvpn start
echo openvpn has tarted

else
echo pls select a server and save

fi

