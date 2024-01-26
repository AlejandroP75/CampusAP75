import java.util.Scanner;

public class Edad {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);

        System.out.println("Ingrese su fecha de nacimiento.");

        System.out.println("Día:");
        int dia = leer.nextInt();

        System.out.println("Mes:");
        int mes = leer.nextInt();

        System.out.println("Año:");
        int año = leer.nextInt();

        leer.close();

        System.out.println(dia + mes + año);
    }
}
