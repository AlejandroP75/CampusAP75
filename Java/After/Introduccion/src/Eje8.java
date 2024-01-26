import java.util.Scanner;

public class Eje8 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese nota certamen 1: ");
        float notc1 = leer.nextFloat();
        System.out.print("Ingrese nota certamen 2: ");
        float notc2 = leer.nextFloat();
        System.out.print("Ingrese nota laboratorio: ");
        float notlab = leer.nextFloat();

        double nc = (59.63333333333333 - (notlab * 0.3)) / 0.7;
        double notc3 = (3 * nc) - notc1 - notc2;

        System.out.printf("Necesita nota %.0f en el certamen 3", notc3);

        leer.close();
    }
}

