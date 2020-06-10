#!/bin/ash
echo Content-type: text/html
echo
if [ "$REQUEST_METHOD" = "POST" ]; then
  TMPOUT=/tmp/server.tar.gz
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

echo "<link rel="stylesheet" href="css/style.css">"

rm /tmp/*.ovpn
cd /tmp/
mv server.tar.gz /www/
sleep 1
tar -xzf /www/server.tar.gz -C /tmp/


echo SERVER UPDATE SUCCESS...

cat << EOF



<HTML>

<meta http-equiv="Refresh" content="4; url=http://192.168.1.1/index.html">

</HTML>


