#!/bin/ash






echo Content-type: text/html
echo


case "$REQUEST_METHOD" in
  POST)
    (


        cat $FILE | busybox sed -n '4p;8p' | busybox sed 's/\r$//' > /tmp/pass.txt
    )

    echo
    ;;

  *)
    echo

esac

pass=`busybox head -1 /tmp/pass.txt`

echo -e  "$pass\n$pass" | passwd  root
echo '/:root:$p$root' > /etc/httpd.conf
echo password has beed added



cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/reboot.html">

</HTML>




