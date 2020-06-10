#!/bin/sh


echo Content-type: text/plain
echo
FINDPROCESS=`cat /etc/rc.local  | grep enable`
if [ -n "$FINDPROCESS" ]; then
echo "<input type='button'  onclick='javascript:autostart()' class='btn-pushgreen' value='AUTOSTART'>"
else

echo "<input type='button'  onclick='javascript:autostop()' class='btn-pushred' value='AUTOSTOP'>"
fi
echo " 
<style>
.btn-pushgreen {
	background-color:#44c767;
	border-radius:28px;
	border:1px solid #18ab29;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:17px;
	font-weight:bold;
	padding:4px 14px;
	text-decoration:none;
	text-shadow:0px 1px 0px #2f6627;
}
.btn-pushgreen:hover {
	background-color:#5cbf2a;
}
.btn-pushgreen:active {
	position:relative;
	top:1px;
}


.btn-pushred {
	box-shadow: 3px 4px 0px 0px #8a2a21;
	background:linear-gradient(to bottom, #c62d1f 5%, #f24437 100%);
	background-color:#c62d1f;
	border-radius:18px;
	border:1px solid #d02718;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:17px;
	padding:2px 20px;
	text-decoration:none;
	text-shadow:0px 1px 0px #810e05;
}
.btn-pushred:hover {
	background:linear-gradient(to bottom, #f24437 5%, #c62d1f 100%);
	background-color:#f24437;
}
.btn-pushred:active {
	position:relative;
	top:1px;
}
</style>

"