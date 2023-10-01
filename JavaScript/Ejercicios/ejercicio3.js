let d = document;
const contenedor = d.querySelector(".contenedor");


function añadirTarea() {
    const tarea = d.querySelector("#tarea").value;
    if (tarea == "") {
        alert("No sea bobo perro hp no puede añadir una tarea vacia");
        return;
    }
    const nuevaTarea = d.createElement("checkbox");

    nuevaTarea.textContent = tarea;
    contenedor.appendChild(nuevaTarea);
}

const botonAñadirTarea = d.querySelector("#botAñadir");
botonAñadirTarea.addEventListener("click", añadirTarea);