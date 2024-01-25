import java.util.Scanner;

public class Eje5 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese el cateto a: ");
        float a = leer.nextFloat();

        System.out.print("Ingrese el cateto b: ");
        float b = leer.nextFloat();

        double c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));

        System.out.printf("La hipotenusa es %.4f", c);

        leer.close();
    }
}
