function main() {
	window.location = "../..";
	window.location = "/carrito";
}
function reg() {
	var nom = document.getElementById('nombreReg').value;
	var mail = document.getElementById('mailReg').value;
	var pass = document.getElementById('pass1').value;
	var pass2 = document.getElementById('pass2').value;
	var form = $("#regForm")[0];
	var token = form.csrfmiddlewaretoken.value;

	if(nom != "" && mail != "" && pass != "" && pass2 != ""){
		if(pass == pass2 || pass2 == "sí" || pass2 == "sí es" || pass2 == "confirmo" || pass2 == "non't"){
			$.ajax({
				url: 'registro',
				type: 'POST',
				data:{csrfmiddlewaretoken:token, nom:nom, mail:mail, pass:pass},
				success:
				function(data){
					if(data == "1"){
						alert("Bienvenido " + nom);
						sessionStorage.setItem('user', nom);
						window.location="../..";
						window.location="/carrito";
					}else{
						alert("Error al regitrar usuario, intenta más tarde");
					}
				}
			});
		}
	}else{
		alert("Campos vacíos, verifica y vuelve a intentar");
	}
}

function add(id){
	if(sessionStorage.getItem('user') != null){
		console.log(1);
	}else{
		console.log(2);
		if(confirm("No hay una sesión creada\n¿Deseas iniciar seión?")){
			window.location="../..";
			window.location="/carrito/log";
		}else{
			alert("Producto agregado");
		}
	}
}

function log() {
	var mail = document.getElementById('mail').value;
	var pass = document.getElementById('pass').value;
	var form = $("#logForm")[0];
	var token = form.csrfmiddlewaretoken.value;

	if(mail != "" && pass != ""){
		$.ajax({
			url: 'iniciar',
			type: 'POST',
			data:{csrfmiddlewaretoken:token, mail:mail, pass:pass},
			success:
			function(data){
				if(data!="2"){
					var nombre = data;
					alert("Bienvenido " + nombre);
					sessionStorage.setItem('user', nombre);
					window.location="../..";
					window.location="/carrito";
				}else{
					alert("Error al iniciar sesión, intenta más tarde");
				}
			}
		});
	}else{
		alert("Campos vacíos, verifica y vuelve a intentar");
	}
}

function redirect() {
	var div = document.querySelector('.menu-icon');
	var user = sessionStorage.getItem('user');
	if(user != null){
		div.innerHTML += "<i class='fa fa-user'> </i><p> "+user+"</p>";
	}else{
		div.innerHTML = "<button class='btn btn-link' id='redLink' onclick='fn();'><i class='fa fa-sign-in-alt'></i> Inicia sesión</button>";
	}
}

function fn(){
	window.location = "../..";
	window.location = "carrito/log";
}

function hide(id){
	var div = document.getElementById(id);
	if(id == 'log'){
		if(div.style.display="block"){
			div.style.display="none";
			document.getElementById('reg').style.display="block";
		}else{
			div.style.display="none";
			document.getElementById('reg').style.display="block";
		}
	}else{
		if(div.style.display=="none"){
			div.style.display="none";
			document.getElementById('log').style.display="block";
		}else{
			div.style.display="none";
			document.getElementById('log').style.display="block";
		}
	}
}