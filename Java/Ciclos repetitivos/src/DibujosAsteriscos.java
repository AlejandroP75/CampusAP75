import java.util.Scanner;

public class DibujosAsteriscos {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Altura: ");
        int altura = leer.nextInt();
        System.out.print("Ancho: ");
        int ancho = leer.nextInt();

        for (int i = 0; i < altura; i++){
            System.out.println(" ");
            for (int j = 0; j < ancho; j++){
                System.out.print("*");
            }
        }
        System.out.println(" ");

        System.out.print("Altura: ");
        altura = leer.nextInt();

        for (int i = 0; i < altura; i++){
            
        }
        leer.close();
    }
}
