import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner leer = new Scanner(System.in);

        System.out.print("Juegos ganados por A: ");
        int a = leer.nextInt();

        System.out.print("Juegos ganados por B: ");
        int b = leer.nextInt();

        marcador marc = new marcador(a, b);

        System.out.println(marc.resultado());

        leer.close();
    }
}
