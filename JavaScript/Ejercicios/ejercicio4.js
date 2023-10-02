let nomProdu = document.querySelector("#nomProdu");
let preProdu = document.querySelector("#preProdu");
let porcentaje = document.querySelector("#porcentaje");
let listProdu = document.querySelector("#listProdu");
let listDescProdu = document.querySelector("#listDescProdu");
let botAnad = document.querySelector("#botAñad");
let botCalc = document.querySelector("#botCalc");
let nombresProductos = [];
let preciosProductos = [];
let cont = 0;

function añadirProducto(){
    let nProdu = nomProdu.value;
    let pProdu = preProdu.value;

    if (nProdu == ""){
        alert("No puede agregar un producto sin un nombre");
        return;
    }else if(pProdu == ""){
        alert("No puede agregar un producto sin un precio");
        return;
    }
    nombresProductos.push(nProdu);
    preciosProductos.push(pProdu);

    listProdu.innerHTML = '<h1>Prodcutos añdidos</h1>';

    for (let i = 0; i < nombresProductos.length; i++) {
        listProdu.innerHTML += `<p class = "productos">${nombresProductos[i]} $${preciosProductos[i]}</p>`;
    }

    nomProdu.value = "";
    preProdu.value = "";
}

function calcularDescuentos(){
    let porce = porcentaje.value;
     if (porce == ""){
        alert("No se puede calcular el descuento sin un porcentaje");
        return;
     } else if(nombresProductos == ""){
        alert("Debes añadir por lo menos un producto");
        return;
     } else if(porce < 1 || porce > 100){
        alert("El porcentaje de descuento debe estar entre 1 y 100");
        return;
     }else{
        for (let i = 0; i < nombresProductos.length; i++) {
            listProdu.innerHTML += `<p class = "descuento">${nombresProductos[i]} (precio con descuento del ${porce}%): $${preciosProductos[i]-((preciosProductos[i] * porce) / 100)}</p>`;
        }
     }
     porcentaje.value = "";
}

botAnad.addEventListener("click", añadirProducto);
botCalc.addEventListener("click", calcularDescuentos);