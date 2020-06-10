#!/bin/sh

echo Content-type: text/html
echo
echo

FILE=`cat`
case "$REQUEST_METHOD" in
  POST)
    (
	
        #echo "$FILE" | busybox sed -n '3p' | busybox sed 's/\r$//' > /tmp/cfg.sys
	#echo "$FILE" | busybox sed -n '5p' | busybox sed 's/\r$//' >> /tmp/cfg.sys

		echo "$FILE" | busybox sed -n '4p' | busybox sed 's/\r$//' > /www/cfg.sys
		#echo "$FILE" | busybox sed -n '8p' | busybox sed 's/\r$//' > /www/host.sys
SSLOCATE=`cat /www/cfg.sys`
#HOST=`cat /www/host.sys`
SSLPORT=`cat /tmp/$SSLOCATE.ovpn | grep "remote " | busybox awk '{print $2}'`
#PAYLOAD=`cat /tmp/$HOST.host | grep "host " | busybox awk '{print $2}'`
	
		cat /tmp/$SSLOCATE.ovpn > /etc/openvpn/server.ovpn

procss=`cat /etc/openvpn/server.ovpn | grep stunnel`
if [ -n "$procss" ]; then
PORT=`cat /etc/openvpn/server.ovpn | grep -m1 "remote"`
SNI=`cat /etc/openvpn/server.ovpn | grep -m1 "http-proxy-option CUSTOM-HEADER Host"`
echo "$PORT" > /www/ssl.txt
echo "$SNI" > /www/sni.txt
SSL2=`awk '{$1= ""; print $2}' /www/ssl.txt`
SNI2=`awk '{$1= ""; print $4}' /www/sni.txt`
sed -i 's/remote/#remote /g' /etc/openvpn/server.ovpn
echo "route $SSL2 255.255.255.255 net_gateway " >> /etc/openvpn/server.ovpn

		echo "client = yes" > /etc/stunnel/stunnel.conf
		echo "output = /tmp/stunnel.log" >> /etc/stunnel/stunnel.conf
		echo "debug = 7" >> /etc/stunnel/stunnel.conf
		echo "[openvpn]" >> /etc/stunnel/stunnel.conf
              	echo "connect = $SSL2:443" >> /etc/stunnel/stunnel.conf
		echo "accept = 127.0.0.1:9999" >> /etc/stunnel/stunnel.conf
		echo "TIMEOUTclose = 0" >> /etc/stunnel/stunnel.conf
		echo "verify = 0" >> /etc/stunnel/stunnel.conf
		echo "sni = $SNI2" >> /etc/stunnel/stunnel.conf
		echo "remote 127.0.0.1 9999" >> /etc/openvpn/server.ovpn
sed -i 's/http-proxy/#http-proxy /g' /etc/openvpn/server.ovpn
		
fi

sed -i 's/auth-user-pass/ /g' /etc/openvpn/server.ovpn
echo "auth-user-pass /etc/openvpn/account.txt " >> /etc/openvpn/server.ovpn
echo "log /tmp/openvpn.log " >> /etc/openvpn/server.ovpn
 



    )


    echo
    ;;

  *)

    echo

esac


cd /tmp/
tar -czvf  server.tar.gz *.ovpn jquery.min.js TZ logo.png > /dev/null
rm /www/server.tar.gz
mv /tmp/server.tar.gz /www/server.tar.gz


/etc/init.d/openvpn stop
rm /tmp/openvpn.log
killall stunnel


cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=/index.html">

</HTML>




