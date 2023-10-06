let portLib = document.getElementById("linkLib");
let titLib = document.getElementById("titLib");
let autLib = document.getElementById("autLib");
let anioLib = document.getElementById("anioLib");
let disLib = document.getElementById("disLib");
let presLib = document.getElementById("presLib");
let botAniadir = document.getElementById("aniaLib");
let form = document.getElementById("nuevosLibros");

function añadirLibro(){
    console.log("This is a test");
    let portada = portLib.value;
    let titulo = titLib.value;
    let autor = autLib.value;
    let anio = anioLib.value;
    let disponible = disLib.value;
    let prestado = presLib.value;

    let contenedor = document.createElement("div");
    let portadaE = document.createElement("img");
    portadaE.setAttribute("src", portada);
    portadaE.setAttribute("width", "200px");
    portadaE.setAttribute("height", "200px");
    let textE = document.createElement("p");
    textE.innerHTML = "<br>Titulo: " + titulo + "<br>Autor: " + autor + "<br>Año: " + anio +"<br>Disponible: " + disponible +"<br>Prestado: " + prestado;
  
    form.appendChild(contenedor);
    contenedor.appendChild(portadaE);
    contenedor.appendChild(textE);    
}

botAniadir.addEventListener("click", añadirLibro);