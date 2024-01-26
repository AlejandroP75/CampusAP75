import java.util.Scanner;

public class Eje1 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese su nombre: ");
        String nombre = leer.nextLine();
        System.out.print("Hola, " + nombre);

        leer.close();
    }
}
