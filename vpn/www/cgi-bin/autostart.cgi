#!/bin/sh

echo Content-type: text/html
echo

echo " " > /etc/rc.local

echo "


# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

tar -xzvf /www/server.tar.gz -C /tmp/ > /dev/null
rm /etc/rc.button/failsafe
exit 0




"  > /etc/rc.local

echo vpn autostart is enable