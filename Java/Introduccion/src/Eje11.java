import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Eje11 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        ArrayList<Integer> num = new ArrayList<>();

        System.out.print("Ingrese el primer numero: ");
        int num1 = leer.nextInt();
        num.add(num1);

        System.out.print("Ingrese el segundo numero: ");
        int num2 = leer.nextInt();
        num.add(num2);

        System.out.print("Ingrese el tercer numero: ");
        int num3 = leer.nextInt();
        num.add(num3);

        System.out.print("Ingrese el cuarto numero: ");
        int num4 = leer.nextInt();
        num.add(num4);

        Collections.sort(num);

        for (Integer numero : num) {
            System.out.print(numero + " ");
        }

        leer.close();
    }
}
