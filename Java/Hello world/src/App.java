import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese el valor a: ");
        int a = leer.nextInt();
        System.out.println("Ingrese el valor b: ");
        int b = leer.nextInt();
        int rta = a + b;
        System.out.println("La suma de los lados es: " + rta);
        leer.close();
    }
}
