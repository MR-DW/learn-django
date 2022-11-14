let enviar = document.getElementById("button");
enviar.addEventListener('click', () => {
	return callApi();
})


function callApi(){
	let url = 'http://127.0.0.1:8000/create-heroe/';
	let request = new XMLHttpRequest();
	let formData = new FormData(document.forms.altaDeHeroes);
	
	request.open('POST',url);
	request.send(formData);
	
	
	request.onload = async function () {
		console.log ('------se envio------');
	}
	
}