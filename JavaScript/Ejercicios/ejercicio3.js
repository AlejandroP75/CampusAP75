let d = document;
let contenedor = d.querySelector(".contenedor");
let botonAñadirTarea = d.querySelector("#botAñadir");
let cajaTexto = d.querySelector("#tarea");

function añadirTarea() {
    let tarea = cajaTexto.value;
    if (tarea == "") {
        alert("No puedes agregar una tarea vacía");
        return;
    }
    let miniCaja = d.createElement("div");
    miniCaja.setAttribute("class", "tareitas");
    let miniminiCaja = d.createElement("div");
    miniminiCaja.setAttribute("class", "miniTareas");

    let check = d.createElement("input");
    check.setAttribute("type", "checkbox");
    check.addEventListener("change", function () {
        marcar(this);
    });
    let label = d.createElement("label");
    label.textContent = tarea;
    let br = d.createElement("br");
    let eliminar = d.createElement("button");
    eliminar.setAttribute("class", "botonEliminar");
    eliminar.textContent = "Eliminar";
    eliminar.addEventListener("click", function () {
        eliminarTarea(miniCaja);
    });

    contenedor.appendChild(miniCaja);
    miniCaja.appendChild(miniminiCaja);
    miniminiCaja.appendChild(check);
    miniminiCaja.appendChild(label);
    miniCaja.appendChild(br);
    miniCaja.appendChild(eliminar);

    cajaTexto.value = "";
}

function marcar(checkbox) {
    let labeld = checkbox.nextElementSibling;
    if (checkbox.checked) {
        labeld.style.textDecoration = "line-through";
        labeld.style.color = "#000706";
    } else {
        labeld.style.textDecoration = "none";
        labeld.style.color = "white";
    }
}

function eliminarTarea(taskContainer) {
    contenedor.removeChild(taskContainer);
}

botonAñadirTarea.addEventListener("click", añadirTarea);
