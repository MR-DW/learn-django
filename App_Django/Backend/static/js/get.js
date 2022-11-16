// Metodo GET

const pedir = document.getElementById("buttonLlamar");

pedir.addEventListener('click', () => {
    console.log('--funciona--');
    // callHeroes();
    llamarHeroes();
});

// const callHeroes = async () => {
	
//     const response = await fetch('http://127.0.0.1:8000/heroes-list/'); 

//     const data = await response.json();

//     console.log(data);

//     const div = document.getElementById('lista');

    
  
//     let info =  `<h3>${data[0].name}</h3>
//     <h3>${data[0].age}</h3>
//     <p>${data[0].universe}</p>`
   
//     div.innerHTML = info;

//     console.log(data[0].name);
// }
const div = document.getElementById('lista');

const url = 'http://127.0.0.1:8000/heroes-list/'

function llamarHeroes(){

    fetch(url)
	.then(res => res.json())
	.then(data => {
        data.forEach(heroe => {
            // console.log(heroe.name)
            // const p = document.getElementById('p');
            const p = document.createElement('p');
            let id = p.setAttribute('id', heroe.id)            
            p.innerHTML= heroe.name
            p.style.width = '50%'
            p.style.margin = '1% 0'
            div.appendChild(p)

            p.addEventListener('click', () => {
                // console.log('apretaste para ver la descripcion del heroe')
                descripcionHeroe();    
            })
            
            function descripcionHeroe(){
                let infoHeroe = document.getElementById('infoHeroe');
                // console.log('adentro de la funcion descripcion');
                
                    let datos = `<h3 id="name">${heroe.name}</h3>
                    <h3 id="name">${heroe.age}</h3>
                    <h3 id="name">${heroe.universe}</h3>`
                    
                    infoHeroe.innerHTML = datos;
                }
                
        })
        
    });

}




