// Metodo POST

const enviar = document.getElementById('buttonEnviar')
enviar.addEventListener('click', () => {
	callApi();
});


function callApi() {
	let url = 'http://127.0.0.1:8000/create-heroe/';
	let request = new XMLHttpRequest();
	let formData = new FormData(document.forms.altaDeHeroes);

	request.open('POST', url);
	request.send(formData);

	// function confirmacion() {
	// 	let name = document.getElementById('exampleFormControlInput1');
	// 	let ok = document.getElementById('ok');
	// 	let yaExiste = document.getElementById('yaExiste');

	// 	if (name != heroe.name) {
	// 		ok.innerText(' Tu heroes fue creado correctamente.')
	// 	} else {
	// 		yaExiste.innerText('Tu heroes ya fue creado anteriormente.')
	// 	}
	// }

	// confirmacion();

	request.onload = async function () {
		console.log('------se envio------');
	}

}

