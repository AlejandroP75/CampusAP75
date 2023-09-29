//Obtener elementos HTML
const inputDescuento = document.getElementById('descuento');
const botonCalcular = document.getElementById('calcular');
const resultados = document.getElementById('resultados');
const botonIngresar = document.querySelector('#ingresar');
const div = document.querySelector('#dive');
const d=document;


//Lista de precios
const precios = [20, 30, 40, 50];
//Función para calcular precios con descuento
function ingresaProductos() {
    let numPro = document.querySelector("#productos").value;
    let i = 0;
    while(i < numPro) {
        let etiquetas=`
        <div style="display: flex;">
            <p>Nombre</p>
            <input id="name" type="text" placeholder="Nombre del producto"></input>
        </div><br>
        <div style="display: flex;">
            <p>Precio</p>
            <input id="price" type="number" placeholder="Precio del producto"></input>
        </div><br>
        <button id = "añadir">Añadir</button>
        `;
        div.insertAdjacentHTML('beforeend',etiquetas);
        i++;
    }




        /*let nuePa = document.createElement("label");
        nuePa.textContent = `  Ingrese el nombre del producto  `;
        let nueNom = document.createElement("input");

        let nuePo = document.createElement("label");
        nuePo.textContent = "  Ingrese el valor del prodcucto  ";
        let nuePro = document.createElement("input");

        let salto = document.createElement("br");

        div.appendChild(nuePa);
        div.appendChild(nueNom);
        div.appendChild(nuePo);
        div.appendChild(nuePro);
        div.appendChild(salto);
        i++;*/
}



function calcularDescuento(){
    const descuento = parseFloat(inputDescuento.value);
    const preciosConDescuento = precios.map(function(precio) {
        const preciosConDescuento = precio - (precio * (descuento / 100));
        return preciosConDescuento.toFixed(2); //Redonder a 2 decimales
    });
    resultados.innerHTML = '<h2>Precios con Descuento:</h2>';
    preciosConDescuento.forEach((precio, index) => {
        resultados.innerHTML += `<p>Producto ${index + 1}: $${precio}</p>`;
    });
}
//Agregar evento al botón "Calcular"
botonCalcular.addEventListener('click', calcularDescuento);
botonIngresar.addEventListener('click', ingresaProductos);
