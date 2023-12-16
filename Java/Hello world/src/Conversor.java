import java.util.Scanner;

public class Conversor {
    public static void main(String arg[]) {
        Scanner leer = new Scanner(System.in);
        double longitud, pulgadas;
        System.out.println("Ingrese la longitud en centumetros: ");
        longitud = leer.nextDouble();
        pulgadas = longitud / 2.54;
        System.out.println(longitud + "cm = " + pulgadas + " in");
        leer.close();
    }
}
