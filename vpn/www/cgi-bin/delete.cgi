#!/bin/sh
PRINT=`cat`
FILENAME=`echo "$PRINT" | busybox sed -n '4p' | busybox sed 's/\r$//'`
rm "/tmp/$FILENAME.ovpn"
SET=`cat /www/cfg.sys`

if [ "$SET" = "$FILENAME" ]; then 

rm "/www/cfg.sys"


fi
cd /tmp/
tar -czvf  server.tar.gz *.ovpn jquery.min.js TZ logo.png > /dev/null
rm /www/server.tar.gz
mv /tmp/server.tar.gz /www/server.tar.gz
cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=/index.html">

</HTML>