#!/bin/sh

# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/html
echo
SET=`cat /www/host.sys`
echo "<select class='y' name='config2'>"
echo "<option>$SET</option>"
cd /tmp/ && ls *.host | busybox sed 's/.host//' | while read LINE; do
     echo "<option>$LINE</option>"
done
echo "</select>"
