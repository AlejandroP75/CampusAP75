let deT = document.getElementById("deT");
let aT = document.getElementById("aT");
let ingresoT = document.getElementById("ingresoT");
let resultadoT = document.getElementById("resultadoT");
let select1 = document.getElementById('deT');
let select2 = document.getElementById('aT');

let select = {
    de: '',
    a: ''
}
let selects = JSON.parse(localStorage.getItem('tempe'));

if (selects) {
    select = selects;
    select1.value = select.de;
    select2.value = select.a;
}

export function temperatura(){
    let deTv = deT.value;
    let aTv = aT.value;

    if(ingresoT.value == ""){
        alert("Ingrese un numero valido")
    }

    if(deTv == "k"){
        if(aTv == "c"){
            let res = parseFloat(ingresoT.value)-273.15;
            resultadoT.textContent = res;
        }
        else if(aTv == "f"){
            let res1 = (parseFloat(ingresoT.value)-273)*9/5+32;
            resultadoT.textContent = res1;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deTv == "c"){
        if(aTv == "k"){
            let res = parseFloat(ingresoT.value)+273.15;
            resultadoT.textContent = res;
        }
        else if(aTv == "f"){
            let res = (parseFloat(ingresoT.value)*9/5)+32;
            resultadoT.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

    if(deTv == "f"){
        if(aTv == "k"){
            let res3 = (parseFloat(ingresoT.value)-32)*5/9+273.15;
            resultadoT.textContent = res3;
        }
        else if(aTv == "c"){
            let res1 = (parseFloat(ingresoT.value)-32)*5/9;
            resultadoT.textContent = res1;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    select.de = select1.value;
    select.a = select2.value;

    localStorage.setItem('tempe', JSON.stringify(select));
}