class Automovil {
    constructor(brand, model, price, color) {
        this.marca = brand;
        this.modelo = model;
        this.precio = price;
        this.color = color;
    }
    vender(){
        this.disponibilidad = false;
    }
}
miAuto = new Automovil("Chevrolet", "2022", 40000000, "Azul");
miAuto.vender();
console.log(miAuto.disponibilidad);