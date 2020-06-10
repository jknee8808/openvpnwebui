

$(function(){ //ready function
    $('#myHref').click(function(){ //click event
         return confirm('Are you sure you want to update?');
    });
})

$(function(){ //ready function
    $('#myHref10').click(function(){ //click event
         return confirm('Are you sure you want to update?');
    });
})

$(function(){ //ready function
    $('#myHref6').click(function(){ //click event
         return confirm('Are you sure you want to continue?');
    });
})

$(function(){ //ready function
    $('#myHref7').click(function(){ //click event
         return confirm('Are you sure you want to continue?');
    });
})




$("#myHref1").on('click', function() {
  return confirm(' are you sure!!! want ot have an updgrade?');
  
});

$("#myHref2").on('click', function() {
  return confirm(' upload local file here for offline update');
  
});

$("#myHref3").on('click', function() {
  return confirm(' be sure your device has bigger space?');
  
});

$("#myHref4").on('click', function() {
  return confirm(' deleting files and reboot?');
  
});

$("#myHref5").on('click', function() {
  return confirm('protect device?');
  
});






setInterval(function () {
	$("#ovpnbutton").load("/cgi-bin/openvpnbutton.cgi")
}, 1000);

setInterval(function () {
	$("#autostartbutton").load("/cgi-bin/autostartbutton.cgi")
}, 1000);


            setInterval(function() {
                $('#logs').load('/cgi-bin/ovpnlogs.cgi');
            }, 1000);
setInterval(function() {
                $('#ssllogs').load('/cgi-bin/ssllogs.cgi');
            }, 1000);
  setInterval(function() {
                $('#infos').load('/cgi-bin/head');
            }, 1000);
            function connect() {
                $.get('/cgi-bin/connect.cgi', function(data) {
                    alert(data);
                });
            }
			
			function ovpnstart() {
                $.get('/cgi-bin/ovpnstart.cgi', function(t) {
                   "" != t && alert(t)
                });
			}
	
            function ovpnstop() {
                $.get('/cgi-bin/ovpnstop.cgi', function(t) {
                    "" != t && alert(t)
                });
            }

function autostart() {
                $.get('/cgi-bin/autostart.cgi', function(t) {
                   "" != t && alert(t)
                });
			}
	
            function autostop() {
                $.get('/cgi-bin/autostop.cgi', function(t) {
                    "" != t && alert(t)
                });
            }


 function update() {
                $.get('/cgi-bin/update', function(data) {
                    alert(data);
                });
            }

            function addstartup() {
                $.get('/cgi-bin/addstartup.cgi', function(data) {
                    alert(data);
                });
            }

  function stunnel() {
                $.get('/cgi-bin/stunnel', function(data) {
                    alert(data);
                });
            }


            function removestartup() {
                $.get('/cgi-bin/removestartup.cgi', function(data) {
                    alert(data);
                });
            }

 function sslstop() {
                $.get('/cgi-bin/sslstop.cgi', function(data) {
                    alert(data);

                });
            }

 function sslstart() {
                $.get('/cgi-bin/ssltart.cgi', function(data) {
                    alert(data);

                });
            }
            window.setInterval(function() {
                var elem = document.getElementById('logs');
                elem.scrollTop = elem.scrollHeight;
            }, 100);
		 window.setInterval(function() {
                var elem = document.getElementById('ssllogs');
                elem.scrollTop = elem.scrollHeight;
            }, 100);




	$(document).ready(function () {
	var t = $("#wifiname").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/wifiname.cgi",
		success: function (t) {
			$("#name").val(t)
		}
	})
});
$(document).ready(function () {
	var t = $("#wifipass").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/wifipass.cgi",
		success: function (t) {
			$("#pass").val(t)
		}
	})
});

$(document).ready(function () {
	var t = $("#Username00").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/username",
		success: function (t) {
			$("#username").val(t)
		}
	})
});

$(document).ready(function () {
	var t = $("#Password00").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/userpass",
		success: function (t) {
			$("#userpass").val(t)
		}
	})
});

   
$(document).ready(function () {
	var t = $("#datetime").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/datetime.cgi",
		success: function (t) {
			$("#date").val(t)
		}
	})
});

function userpassword() {
  var x = document.getElementById("userpass");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function wifipassword() {
  var x = document.getElementById("pass");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}




$(document).ready(function () {
	$('input').keydown(function (event) {
		if (event.keyCode == 13) {
			event.preventDefault();
			return false;
		}
	});
});