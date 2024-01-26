import java.util.Scanner;

public class sumaDeFracciones {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        int i = 1;
        double fraccion = 0;
        double sum = 0;

        System.out.printf("%-10s%-20s%-10s\n", "Potencia", "Fraccion", "Suma");
        while (true) {

            fraccion = (1 / Math.pow(2, i));

            sum = sum + fraccion;

            System.out.printf("%-10d%-20.10f%-10.10f\n", i, fraccion, sum);

            if(fraccion <= 0.000001){
                break;
            }
            i++;
        }

        leer.close();
    }
}
