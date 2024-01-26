import java.util.Scanner;

public class Eje4 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese la longitud a convertir: ");
        int centimetros = leer.nextInt();

        double pulgadas = centimetros / 2.54;

        System.out.printf("%d cm = %.4f in", centimetros, pulgadas);

        leer.close();
    }

}
