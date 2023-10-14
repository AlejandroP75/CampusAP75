let deTi = document.getElementById("deTi");
let aTi = document.getElementById("aTi");
let ingresoTi = document.getElementById("ingresoTi");
let resultadoTi = document.getElementById("resultadoTi");

export function tiempo(){
    let deTiv = deTi.value;
    let aTiv = aTi.value;

    if(ingresoTi.value == ""){
        alert("Ingrese un numero valido")
    }

    if(deTiv == "seg"){
        if(aTiv == "min"){
            let res = parseFloat(ingresoTi.value)/60;
            resultadoTi.textContent = res;
        }
        else if(aTiv == "hora"){
            let res1 = (parseFloat(ingresoTi.value))/3600;
            resultadoTi.textContent = res1;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deTiv == "min"){
        if(aTiv == "seg"){
            let res = parseFloat(ingresoTi.value)*60;
            resultadoTi.textContent = res;
        }
        else if(aTiv == "hora"){
            let res = (parseFloat(ingresoTi.value))/60;
            resultadoTi.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

    if(deTiv == "hora"){
        if(aTiv == "seg"){
            let res3 = (parseFloat(ingresoTi.value))*3600;
            resultadoTi.textContent = res3;
        }
        else if(aTiv == "min"){
            let res1 = parseFloat(ingresoTi.value)*60;
            resultadoTi.textContent = res1;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
} 