function enviar() {
	//formdata = new FormData("#prueba")[0];
	var user = $("#Usuario").val();
	var pass = $("#Pass").val();
	var form = $("#prueba")[0];
	var token = form.csrfmiddlewaretoken.value;
	console.log(user);
	$.ajax({
		url: 'lol/registro',
		type: 'POST',
		data:{csrfmiddlewaretoken:token, user:user, pass:pass},
		success:
		function(data){
			alert(data);
		}
	});
}

function dale() {
	formdata = new FormData($("#registro")[0]);
	console.log(formdata);
	$.ajax({
		url: 'data',
		type: 'POST',
		processData: false,  // tell jQuery not to process the data
  		contentType: false, 
  		data:formdata,  // tell jQuery not to set contentType
		success:
		function(data){
			alert(data)
		}
	});
}

function show(){
	formdata = new FormData($("#registro")[0]);
	$.ajax({
		url: 'image',
		type: 'POST',
		processData: false,  
  		contentType: false,  
  		data: formdata,
		success:
		function(data){
			
			alert(data)
		}
	});
}