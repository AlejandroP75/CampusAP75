let d = document;
const contenedor = d.querySelector(".contenedor");
const botonAñadirTarea = d.querySelector("#botAñadir");
let cajaTexto = d.querySelector("#tarea");
let checko = 0;

function añadirTarea() {
    let tarea = cajaTexto.value;
    if (tarea == "") {
        alert("No puedes agregar una tarea vacia");
        return;
    }
    let miniCaja = d.createElement("div");
    miniCaja.setAttribute("style", "display: flex;");


    let check = d.createElement("input");
    check.setAttribute("type" ,"checkbox");
    checko = check;
    let label = d.createElement("label");
    label.textContent = tarea
    const br = d.createElement("br");
    let eliminar = d.createElement("button");
    eliminar.textContent = "Eliminar";

    contenedor.appendChild(miniCaja);
    miniCaja.appendChild(check);
    miniCaja.appendChild(label);
    miniCaja.appendChild(br);
    miniCaja.appendChild(eliminar);
}

function marcar() {
    console.log("This is a test");
}

botonAñadirTarea.addEventListener("click", añadirTarea);