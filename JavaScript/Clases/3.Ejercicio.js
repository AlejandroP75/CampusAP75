let cont = 1;

// Función para agregar un nuevo campo (etiqueta y caja de texto) al formulario
function agregarCampo() {
  const formulario = document.getElementById('miFormulario');
  const br = document.createElement('br');
  formulario.style.display = "flex";
  formulario.style.flexDirection = "column";
  formulario.style.textAlign = "center";
  formulario.style.justifyContent = "center";
  formulario.style.alignItems = "center";
  // Crear una nueva etiqueta <label>
  const label = document.createElement('label');
  label.style.color = "white";
  label.style.fontWeight = "blond";
  label.style.fontSize = "40px";
  label.textContent = 'Etiqueta ' + (cont);
  // Crear una nueva caja de texto <input>

  const input = document.createElement('textArea');
  input.style.borderRadius = "5px";
  input.style.color = "white";
  input.style.backgroundColor = "black";
  input.style.height = "100px";
  input.style.width = "600px";
  input.style.fontWeight = "100px";
  input.style.fontSize = "35px";
  input.style.border = "3px white solid"
  input.name = 'campo' + (cont);
  // Agregar la etiqueta y la caja de texto al formulario

  formulario.appendChild(br);
  formulario.appendChild(label);
  formulario.appendChild(input);
  formulario.appendChild(br);

  cont++
}

// Obtener el botón de "Agregar Campo" y agregar un manejador de eventos
const botonAgregarCampo = document.getElementById('agregarCampo');
botonAgregarCampo.addEventListener('click', agregarCampo);
