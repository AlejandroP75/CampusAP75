import java.util.Scanner;

public class sumaDeFracciones {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        double fraccion = 0;
        int cont = 1;
        double sum = 0.5;

        System.out.print("Potencia \tFracción \tSuma");

        while (fraccion > 0.000001) {
            System.out.print(cont + "\t" + (1 / Math.pow(0, cont)) + "\t" + sum);
            cont++;
        }

        leer.close();
    }
}
