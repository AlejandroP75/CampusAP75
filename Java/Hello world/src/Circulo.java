public class Circulo {
    public static void main(String arg[]){
        int radio = Integer.parseInt(arg[0]);
        double perimetro = 2 * Math.PI * radio;
        double area = Math.PI * Math.pow(radio, 2) ;
        System.out.println("El perimetro es: " + perimetro + " El area es: " + area);
    }
}
