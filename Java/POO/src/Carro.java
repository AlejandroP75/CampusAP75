public class Carro {
    public String color;
    public String placa;
    public int modelo;
    public String marca;
    public boolean motorEstado;
    public int velocidad;

    //metodo constructor

    public Carro(){

    }
    public Carro(String color,String placa, int modelo,String marca,boolean motorEstado, int velocidad){
        this.color = color;
        this.marca = marca;
        this.placa = placa;
        this.modelo = modelo;
        this.motorEstado = motorEstado;
        this.velocidad = 0;
    }
    @Override
    public String toString() {
        return "Carro [color=" + color + ", placa=" + placa + ", modelo=" + modelo + ", marca=" + marca
                + ", motorEstado=" + motorEstado + ", velocidad=" + velocidad + "]";
    }
    public void mostrar(){
        System.out.println("Estado del motor: " + this.motorEstado);
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Color: " + this.color);
        System.out.println("Placa: " + this.placa);
        System.out.println("Marca: " + this.marca);
    }
    public void acelerar(int valor){
        this.velocidad+=valor;
    }
    public void frenar(int valor){
        this.velocidad-=valor;
    }
}
