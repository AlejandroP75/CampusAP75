import java.util.Scanner;

public class Eje7 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese un numero: ");
        float num = Math.abs(leer.nextFloat());

        float part = num % 1;

        String numText = Float.toString(num);
        int decimales = 0;

        if (numText.contains(".")) {
            decimales = numText.length() - numText.indexOf('.') - 1;

        }
        System.out.printf("%." + decimales + "f", part);

        leer.close();
    }
}