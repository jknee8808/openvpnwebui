#!/bin/ash


echo Content-type: text/html
echo


case "$REQUEST_METHOD" in
  POST)
    (


        cat $FILE | busybox sed -n '4p;8p' | busybox sed 's/\r$//' > /tmp/wifi.txt
    )

    echo
    ;;

  *)
    echo

esac

username=`head -1 /tmp/wifi.txt`
username2=`awk 'NR==2 {print $1}' /tmp/wifi.txt`
echo "$username" > /www/wifiname.txt
echo "$username2" > /www/wifipass.txt

PASS=`cat /www/wifipass.txt`
NAME=`cat /www/wifiname.txt`


uci set wireless.@wifi-iface[0].key="$PASS"
uci set wireless.@wifi-iface[0].ssid="$NAME"
uci set wireless.@wifi-iface[0].encryption="psk"
uci set wireless.@wifi-iface[1].key="$PASS"
uci set wireless.@wifi-iface[1].ssid="enjoylifevpn"
uci set wireless.@wifi-iface[1].encryption="psk"


uci commit wireless
wifi reload
uci set wireless.@wifi-device[1].disabled=0
uci set wireless.@wifi-device[0].disabled=0; uci commit wireless; wifi

#CODED BY JECJECKOH


cat << EOF


<HTML>

<meta http-equiv="Refresh" content="1; url=/index.html">

</HTML>