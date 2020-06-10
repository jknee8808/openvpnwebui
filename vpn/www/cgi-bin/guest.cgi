#!/bin/ash


echo Content-type: text/html
echo


case "$REQUEST_METHOD" in
  POST)
    (


        cat $FILE | busybox sed -n '4p;8p' | busybox sed 's/\r$//' > /tmp/guest.txt
    )

    echo
    ;;

  *)
    echo

esac

username=`head -1 /tmp/guest.txt`
username2=`awk 'NR==2 {print $1}' /tmp/guest.txt`

echo '/:root:$p$root ' > /etc/httpd.conf

echo "/:$username:$username2" >> /etc/httpd.conf

/etc/init.d/uhttpd restart


#CODED BY JECJECKOH


cat << EOF


<HTML>

<meta http-equiv="Refresh" content="1; url=/index.html">

</HTML>