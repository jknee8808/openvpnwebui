#!/bin/sh
echo "Content-type: text/html"
echo 
##coded by jec jec koh







cd /tmp/
tar -czvf  server.tar.gz *.ovpn jquery.min.js TZ logo.png > /dev/null
rm /www/server.tar.gz
mv /tmp/server.tar.gz /www/server.tar.gz

sleep 1





procss=`cat /etc/sysctl.conf | grep tweak`
if [ -n "$procss" ]; then

tweak installed

else
ln -s /tmp/jquery.min.js /www/js/
ln -s /tmp/logo.png /www/


tar -xzvf /www/server.tar.gz -C /tmp/ > /dev/null

echo "
echo "
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

tar -xzvf /www/server.tar.gz -C /tmp/ > /dev/null
rm /etc/rc.button/failsafe
exit 0

" > /etc/rc.local
chmod +x /etc/rc.local


fs.file-max = 51200
net.core.rmem_max = 67108864
net.core.wmem_max = 67108864
net.core.netdev_max_backlog = 250000
net.core.somaxconn = 4096
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.ip_local_port_range = 10000 65000
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_max_tw_buckets = 5000
net.ipv4.tcp_fastopen = 3
net.ipv4.tcp_mem = 25600 51200 102400
net.ipv4.tcp_rmem = 4096 87380 67108864
net.ipv4.tcp_wmem = 4096 65536 67108864
net.ipv4.tcp_mtu_probing = 1
#tweak

" >> /etc/sysctl.conf

echo "PST-8" > /etc/TZ

fi











cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/reboot.html">

</HTML>









