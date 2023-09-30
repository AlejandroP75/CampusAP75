let butt1 = document.querySelector(".generarAlea1");
let butt2 = document.querySelector(".generarAlea2");
let butt3 = document.querySelector(".add");
let num1 = document.querySelector(".num1");
let num2 = document.querySelector(".num2");
let div = document.querySelector(".imagenes");
let fibbo = [1, 1, 2, 3, 5, 8, 13];
let n1 = 0;
let n2 = 0;
let c1 = document.querySelector("#c1");
let c2 = document.querySelector("#c2");
let c3 = document.querySelector("#c3");

function cartas(num, car){
    switch (num){
        case 1:
            car.src = "1.webp";
            break;
        case 2:
            car.src = "2.png";
            break;
        case 3:
            car.src = "3.png";
            break;
        case 4:
            car.src = "4.png";
            break;
        case 5:
            car.src = "5.png";
            break;
        case 6:
            car.src = "6.png";
            break;
        case 7:
            car.src = "7.png";
            break;
        case 8:
            car.src = "8.png";
            break;
        case 9:
            car.src = "9.png";
            break;
        case 10:
            car.src = "10.png";
            break;
        case 11:
            car.src = "11.webp";
            break;
    }
}


function generarNum1(){
    c2.src = "carta_trasera.webp";
    n1 = Math.floor(Math.random() * 11) + 1;
    num1.textContent = n1;
    cartas(n1, c1);
    if(n2 != 0){
        let n3 = n1 + n2;
        fibbo.forEach((element) => {
            if(element == n3){
                c2.src = "fibo.avif";
            }
        })
    }
}

function generarNum2(){
    c2.src = "carta_trasera.webp";
    n2 = Math.floor(Math.random() * 11) + 1;
    num2.textContent = n2;
    cartas(n2, c3);
    if(n1 != 0){
        let n3 = n1 + n2;
        fibbo.forEach((element) => {
            if(element == n3){
                c2.src = "fibo.avif";
            }
        })
    }

}

butt1.addEventListener("click", generarNum1);
butt2.addEventListener("click", generarNum2);
