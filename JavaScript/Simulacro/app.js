let documento = document.getElementById("docCli");
let nombre = document.getElementById("nomCli");
let telefono = document.getElementById("telCli");
let correo = document.getElementById("corCli");
let puntos = document.getElementById("punCli");
let botRegistrar = document.getElementById("botonRegistrar");
let contenedor = document.getElementById("contenedor");
let clientes = [];


class cliente{
    constructor(doc, nom, tel, cor, pun){
        this.documento = doc;
        this.nombre = nom;
        this.telefono = tel;
        this.correo = cor;
        this.puntos = pun;
    }
    modificarCli(doc, nom, tel, cor, pun){
        this.documento = doc;
        this.nombre = nom;
        this.telefono = tel;
        this.correo = cor;
        this.puntos = pun;
    }
}

function funcionRegistrar(){
    let nueCli = new cliente(documento.value, nombre.value, telefono.value, correo.value, puntos.value);
    clientes.push(nueCli);
    contenedor.innerHTML = "";

    for(let i = 0; i < clientes.length; i++){

        let element = document.createElement("p");
        element.innerHTML = "Documento: " + clientes[i].documento + " Nombre: " + clientes[i].nombre + " Telefono: " + clientes[i].telefono + " Correo: " + clientes[i].correo + " Puntos: " + clientes[i].puntos;

        contenedor.appendChild(element);
    }
}

botRegistrar.addEventListener("click", funcionRegistrar);