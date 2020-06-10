#!/bin/ash
echo Content-type: text/html
echo
echo

USERNAME=${QUERY_STRING#*username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

USERNAME2=${QUERY_STRING#*username2=}
USERNAME2=${USERNAME2%%&*}
USERNAME2=${USERNAME2//+/ }

USERNAME3=${QUERY_STRING#*username3=}
USERNAME3=${USERNAME3%%&*}
USERNAME3=${USERNAME3//+/ }

USERNAME4=${QUERY_STRING#*username4=}
USERNAME4=${USERNAME4%%&*}
USERNAME4=${USERNAME4//+/ }


echo "$USERNAME2" > /www/date.txt


date=`cat /www/date.txt`


echo "$(date $date)"





#CODED BY JECJECKOH

cat << EOF


<HTML>

<meta http-equiv="Refresh" content="1; url=/index.html">

</HTML>