let deP = document.getElementById("deP");
let aP = document.getElementById("aP");
let ingresoP = document.getElementById("ingresoP");
let resultadoP = document.getElementById("resultadoP");
let convertirP = document.getElementById("convertirP");
let deL = document.getElementById("deL");
let aL = document.getElementById("aL");
let ingresoL = document.getElementById("ingresoL");
let resultadoL = document.getElementById("resultadoL");
let convertirL = document.getElementById("convertirL");
let deT = document.getElementById("deT");
let aT = document.getElementById("aT");
let ingresoT = document.getElementById("ingresoT");
let resultadoT = document.getElementById("resultadoT");
let convertirT = document.getElementById("convertirT");
let deTi = document.getElementById("deTi");
let aTi = document.getElementById("aTi");
let ingresoTi = document.getElementById("ingresoTi");
let resultadoTi = document.getElementById("resultadoTi");
let convertirTi = document.getElementById("convertirTi");


function peso(){
    let dePv = deP.value;
    let aPv = aP.value;

    if(dePv == "kg"){
        if(aPv == "lb"){
            let res = parseFloat(ingresoP.value)*2.205;
            resultadoP.textContent = res;
        }
        else if(aPv == "arroba"){
            let res1 = parseFloat(ingresoP.value)*0.088;
            resultadoP.textContent = res1;
        }
        else if(aPv == "gramos"){
            let res2 = parseFloat(ingresoP.value)*1000;
            resultadoP.textContent = res2;
        }
         else if(aPv == "onzas"){
            let res3 = parseFloat(ingresoP.value)*35.;
            resultadoP.textContent = res3;
        }
        else{
            alert("COMO HPTAS ")
        }
    }
    if(dePv == "lb"){
        if(aPv == "kg"){
            console.log("This is a test");
        }
         else if(aPv == "arroba"){
            console.log("This is a test");
        }
         else if(aPv == "gramos"){
            console.log("This is a test");
        }
         else if(aPv == "onzas"){
            console.log("This is a test");
        }
    }
        if(dePv == "lb"){
        if(aPv == "kg"){
            console.log("This is a test");
        }
        else if(aPv == "arroba"){
            console.log("This is a test");
        }
        else if(aPv == "gramos"){
            console.log("This is a test");
        }
        else if(aPv == "onzas"){
            console.log("This is a test");
        }
    }
    if(dePv == "arroba"){
        if(aPv == "kg"){
            console.log("This is a test");
        }
        else if(aPv == "lb"){
            console.log("This is a test");
        }
        else if(aPv == "gramos"){
            console.log("This is a test");
        }
        else if(aPv == "onzas"){
            console.log("This is a test");
        }
    }
    if(dePv == "gramos"){
        if(aPv == "kg"){
            console.log("This is a test");
        }
        else if(aPv == "lb"){
            console.log("This is a test");
        }
        else if(aPv == "arroba"){
            console.log("This is a test");
        }
        else {
            console.log("This is a test");
        }
    }
    if(dePv == "onzas"){
        if(aPv == "kg"){
            console.log("This is a test");
        }
        else if(aPv == "lb"){
            console.log("This is a test");
        }
        else if(aPv == "arroba"){
            console.log("This is a test");
        }
        else if(aPv == "gramos"){
            console.log("This is a test");
        }
    }
}






convertirP.addEventListener("click",peso);
