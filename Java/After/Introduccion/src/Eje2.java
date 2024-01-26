import java.util.Scanner;

public class Eje2 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese el radio del circulo: ");
        int radio = leer.nextInt();

        System.out.print("Perimetro: " + (3.14 * 2 * radio));
        System.out.print("\nArea: " + 3.14 * (radio * radio));

        leer.close();
    }       
}
