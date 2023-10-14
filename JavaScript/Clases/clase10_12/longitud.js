let deL = document.getElementById("deL");
let aL = document.getElementById("aL");
let ingresoL = document.getElementById("ingresoL");
let resultadoL = document.getElementById("resultadoL");
let select1 = document.getElementById('deL');
let select2 = document.getElementById('aL');

let select = {
    de: '',
    a: ''
}
let selects = JSON.parse(localStorage.getItem('longi'));

if (selects) {
    select = selects;
    select1.value = select.de;
    select2.value = select.a;
}

export function longitud(){
    let deLv = deL.value;
    let aLv = aL.value;

    if(ingresoL.value == ""){
        alert("Ingrese un numero valido")
    }

    if(deLv == "m"){
        if(aLv == "km"){
            let res = parseFloat(ingresoL.value)/1000;
            resultadoL.textContent = res;
        }
        else if(aLv == "milla"){
            let res1 = parseFloat(ingresoL.value)/1609;
            resultadoL.textContent = res1;
        }
        else if(aLv == "yarda"){
            let res2 = parseFloat(ingresoL.value)*1094;
            resultadoL.textContent = res2;
        }
         else if(aLv == "codo"){
            let res3 = parseFloat(ingresoL.value)*2.25;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deLv == "km"){
        if(aLv == "m"){
            let res = parseFloat(ingresoL.value)*1000;
            resultadoL.textContent = res;
        }
        else if(aLv == "milla"){
            let res = parseFloat(ingresoL.value)/1609;
            resultadoL.textContent = res;
        }
        else if(aLv == "yarda"){
            let res2 = parseFloat(ingresoL.value)/1094;
            resultadoL.textContent = res2;
        }
         else if(aLv == "codo"){
            let res3 = parseFloat(ingresoL.value)/2.25;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

    if(deLv == "milla"){
        if(aLv == "km"){
            let res3 = parseFloat(ingresoL.value)*1.609;
            resultadoL.textContent = res3;
        }
        else if(aLv == "m"){
            let res1 = parseFloat(ingresoL.value)*1.609;
            resultadoL.textContent = res1;
        }
        else if(aLv == "yarda"){
            let res2 = parseFloat(ingresoL.value)*1760;
            resultadoL.textContent = res2;
        }
         else if(aLv == "codo"){
            let res3 = parseFloat(ingresoL.value)*3616.50;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deLv == "yarda"){
        if(aLv == "km"){
            let res = parseFloat(ingresoL.value)/1094;
            resultadoL.textContent = res;
        }
        else if(aLv == "milla"){
            let res1 = parseFloat(ingresoL.value)/1760;
            resultadoL.textContent = res1;
        }
        else if(aLv == "m"){
            let res2 = parseFloat(ingresoL.value)*1.094;
            resultadoL.textContent = res2;
        }
         else if(aLv == "codo"){
            let res3 = parseFloat(ingresoL.value)*2;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deLv == "codo"){
        if(aLv == "km"){
            let res = parseFloat(ingresoL.value)*0.0005;
            resultadoL.textContent = res;
        }
        else if(aLv == "milla"){
            let res1 = parseFloat(ingresoL.value)*0.0003;
            resultadoL.textContent = res1;
        }
        else if(aLv == "m"){
            let res2 = parseFloat(ingresoL.value)*0.4572;
            resultadoL.textContent = res2;
        }
         else if(aLv == "yarda"){
            let res3 = parseFloat(ingresoL.value)*0.5;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    select.de = select1.value;
    select.a = select2.value;

    localStorage.setItem('longi', JSON.stringify(select));

}