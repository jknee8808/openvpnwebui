#!/bin/sh
echo Content-type: text/html
echo
case "$REQUEST_METHOD" in
POST)
(
FILE=`cat`
FILENAME=`echo "$FILE" | grep filename | busybox awk -F\" '{print $4}'`
echo "$FILE" | busybox sed '1,4d' | busybox sed '$d' | busybox sed '$d' | busybox sed '$d' | busybox sed '$d' | busybox sed '$d' | busybox sed 's/\r$//' > "/tmp/$FILENAME"
)
;;
*)
esac


cat << EOF



<HTML>

<meta http-equiv="Refresh" content="0; url=/index.html">

</HTML>