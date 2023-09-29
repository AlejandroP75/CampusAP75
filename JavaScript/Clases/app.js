//Obtener elementos HTML
const inputDescuento = document.getElementById('descuento');
const botonCalcular = document.getElementById('calcular');
const resultados = document.getElementById('resultados');

//Lista de precios
const precios = [20, 30, 40, 50];
//Función para calcular precios con descuento
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