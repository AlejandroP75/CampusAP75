import java.util.Scanner;

public class Pitagoras {
    public static void main(String arg[]) {
        Scanner leer = new Scanner(System.in);
        double a, b, c;
        System.out.println("Ingrese el valor el cateto a: ");
        a = leer.nextDouble();
        System.out.println("Ingrese el valor el cateto b: ");
        b = leer.nextDouble();
        c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
        System.out.println("La hipotenusa es: " + c);
        leer.close();
    }
}
