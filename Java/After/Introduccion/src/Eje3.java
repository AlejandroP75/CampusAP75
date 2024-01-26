import java.util.Scanner;

public class Eje3 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese la primera nota: ");
        float not1 = leer.nextFloat();

        System.out.print("Ingrese la segunda nota: ");
        float not2 = leer.nextFloat();

        System.out.print("Ingrese la tercera nota: ");
        float not3 = leer.nextFloat();

        System.out.print("Ingrese la cuarta nota: ");
        float not4 = leer.nextFloat();

        double promedio = (not1 + not2 + not3 + not4) / 4;

        System.out.print("El promedio es: " + promedio);

        leer.close();
    }
}
