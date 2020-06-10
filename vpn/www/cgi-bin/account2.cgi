#!/bin/ash






echo Content-type: text/html
echo


case "$REQUEST_METHOD" in
  POST)
    (


        cat $FILE | busybox sed -n '4p;8p' | busybox sed 's/\r$//' > /etc/openvpn/account.txt
    )

    echo
    ;;

  *)
    echo

esac

/etc/init.d/openvpn stop
rm /tmp/openvpn.log

cat << EOF



<HTML>

<meta http-equiv="Refresh" content="0; url=/index.html">

</HTML>



