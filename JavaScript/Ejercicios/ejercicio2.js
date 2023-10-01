let cont = 1;
const formulario = document.getElementById('miFormulario');
const botonAgregarCampo = document.querySelector('.agregarCampo');
const botonCambiarFondo = document.querySelector('.cambiarFondo');
let botonEliminar = document.querySelector('.eliminarEtiqueta');
let arrai = [];
let arrayBr = [];
let arrayLabel = [];


// Función para agregar un nuevo campo (etiqueta y caja de texto) al formulario
function agregarCampo() {
  const br = document.createElement('br');
  arrayBr[cont-1] = br;
  formulario.style.display = "flex";
  formulario.style.flexDirection = "column";
  formulario.style.textAlign = "center";
  formulario.style.justifyContent = "center";
  formulario.style.alignItems = "center";
  // Crear una nueva etiqueta <label>
  const label = document.createElement('label');
  arrayLabel[cont-1] = label;
  label.style.color = "white";
  label.style.fontWeight = "blond";
  label.style.fontSize = "30px";
  label.textContent = 'Etiqueta ' + (cont);
  // Crear una nueva caja de texto <input>
  let input = document.createElement('textArea');
  arrai[cont-1] = input;
  input.style.borderRadius = "5px";
  input.style.color = "white";
  input.style.backgroundColor = "black";
  input.style.height = "50px";
  input.style.width = "600px";
  input.style.fontWeight = "100px";
  input.style.fontSize = "20px";
  input.style.border = "3px white solid"
  input.name = 'campo' + (cont);
  // Agregar la etiqueta y la caja de texto al formulario

  formulario.appendChild(br);
  formulario.appendChild(label);
  formulario.appendChild(input);
  formulario.appendChild(br);

  cont++
}

function cambiarFondo(){
  arrai.forEach(element => {
    element.style.backgroundColor = "crimson";
  });
}

function eliminarEtiqueta(){
  console.log(arrai[arrai.length - 1]);
  arrai[arrai.length - 1].style.display = "none";
  arrai.pop();
  arrayBr[arrayBr.length - 1].style.display = "none";
  arrayBr.pop();
  arrayLabel[arrayLabel.length - 1].style.display = "none";
  arrayLabel.pop();
  cont = arrai.length + 1;
}

// Obtener el botón de "Agregar Campo" y agregar un manejador de eventos

botonAgregarCampo.addEventListener('click', agregarCampo);
botonCambiarFondo.addEventListener('click', cambiarFondo);
botonEliminar.addEventListener('click', eliminarEtiqueta);
