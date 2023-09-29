let butt1 = document.querySelector(".generarAlea1");
let butt2 = document.querySelector(".generarAlea2");
let butt3 = document.querySelector(".add");
let num1 = document.querySelector(".num1");
let num2 = document.querySelector(".num2");
let fibbo = [1, 1, 2, 3, 5, 8, 13];
let n1 = 0;
let n2 = 0;

function generarNum1(){
    n1 = Math.floor(Math.random() * 11) + 1;
    num1.textContent = n1;
    if(n2 != 0){
        let n3 = n1 + n2;
        fibbo.forEach((element) => {
            if(element == n3){
                alert("The number is fibonacci");
            }
        })
    }
}

function addition(){
    n2 = Math.floor(Math.random() * 11) + 1;
    num2.textContent = n2;
    if(n1 != 0){
        let n3 = n1 + n2;
        fibbo.forEach((element) => {
            if(element == n3){
                alert("The number is fibonacci");
            }
        })
    }

}

butt1.addEventListener("click", generarNum1);
butt2.addEventListener("click", addition);
