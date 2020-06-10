#!/bin/ash
echo Content-type: text/html
echo
if [ "$REQUEST_METHOD" = "POST" ]; then
  TMPOUT=/tmp/package.tar.gz
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


echo "<center>$(tar -xzvf /tmp/package.tar.gz -C /tmp/ )</center>"
echo "<center>$(rm /tmp/etc.tar.*)</center>"
echo "<center>installing file 1$(opkg install /tmp/zlib.ipk -d ram)</center>"
echo "<center>installing file 2$(opkg install /tmp/libopenssl.ipk -d ram)</center>"
echo "<center>installing file 3$(opkg install /tmp/stunnel.ipk -d ram)</center>"
echo "<center>cleaning up extra files$(rm /tmp/*.ipk)</center>"

mkdir /etc/stunnel/ 
ln -s /tmp/etc/stunnel/stunnel.conf /etc/stunnel/stunnel.conf 
ln -s /tmp/etc/init.d/stunnel /etc/init.d/stunnel 
 ln -s /tmp/etc/config/stunnel /etc/config/stunnel
ln -s /tmp/usr/bin/stunnel /usr/bin/ 
ln -s /tmp/usr/bin/stunnel /usr/bin/stunnel
ln -s /tmp/usr/lib/*.* /usr/lib/
ln -s /tmp/usr/lib/stunnel/*.* /usr/lib/stunnel/*.*
ln -s /tmp/etc/stunnel/stunnel.conf /etc/stunnel/stunnel.conf
ln -s /tmp/usr/lib/lib* /usr/lib/

echo wait....till the browser stop loading

