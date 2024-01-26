public class Carro {
    private String color;
    private String placa;
    private int modelo;
    private String marca;
    private boolean motorEstado;
    private int velocidad;

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

    private void validarAceleracion(int dato){
        if(dato < 0){
            dato = 0;
        }
    }

    public void acelerar(int valor){
        validarAceleracion(valor);
        if(this.motorEstado != false){
            this.velocidad += valor;
        }
    }

    public void frenar(int valor){
        this.velocidad-=valor;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public int getModelo() {
        return modelo;
    }

    public void setModelo(int modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public boolean isMotorEstado() {
        return motorEstado;
    }

    public void setMotorEstado(boolean motorEstado) {
        this.motorEstado = motorEstado;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public void setVelocidad(int velocidad) {
        if(velocidad < 0){
            this.velocidad = 0;
        }else{
            this.velocidad = velocidad;
        }  
    }
    
}