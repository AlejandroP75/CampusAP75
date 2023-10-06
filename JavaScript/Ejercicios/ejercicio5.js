let portLib = document.getElementById("linkLib");
let titLib = document.getElementById("titLib");
let autLib = document.getElementById("autLib");
let anioLib = document.getElementById("anioLib");
let disLib = document.getElementById("disLib");
let presLib = document.getElementById("presLib");
let botAniadir = document.getElementById("aniaLib");
let form = document.getElementById("form");

function añadirLibro(){
    let portada = portLib.value;
    let titulo = titLib.value;
    let autor = autLib.value;
    let anio = anioLib.value;
    let disponible = disLib.value;
    let prestado = presLib.value;

    let br = document.createElement("br");
    let portadaE = document.createElement("img");
    portadaE.setAttribute("src", portada);
    portadaE.setAttribute("width", "200px");
    portadaE.setAttribute("height", "200px");
    let textE = document.createElement("p");
    textE.innerHTML = "<br>Titulo: " + titulo + "<br>Autor: " + autor + "<br>";
  
    form.appendChild(br);
    form.appendChild(portadaE);
    form.appendChild(textE);
}

botAniadir.addEventListener("click", añadirLibro);