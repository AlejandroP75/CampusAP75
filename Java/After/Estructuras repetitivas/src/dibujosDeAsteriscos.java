import java.util.Scanner;

public class dibujosDeAsteriscos {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Altura: ");
        int altura = leer.nextInt();

        System.out.print("Ancho: ");
        int ancho = leer.nextInt();

        for(int i = 0; i < altura; i++){
            System.out.print("\n");
            for(int j = 0; j < ancho; j++){
                System.out.print("*");
            }
        }

        System.out.print("\n\nAltura: ");
        int altura2 = leer.nextInt();

        for(int i = 0; i < altura2 + 1; i++){
            System.out.print("\n");
            for(int j = 0; j < i; j++){
                System.out.print("*");
            }
        }

        System.out.print("\n\nLado: ");
        int lado = leer.nextInt();

        System.out.print("\n   ");
        for(int i = 0; i < lado; i++){
            System.out.print("*");
        }
        System.out.print("   ");
        System.out.print("\n");
        System.out.print("  ");
        for(int i = 0; i < lado + 2; i++){
            System.out.print("*");
        }
        System.out.print("  ");
        System.out.print("\n");
        System.out.print(" ");
        for(int i = 0; i < lado + 4; i++){
            System.out.print("*");
        }
        System.out.print(" ");
        System.out.print("\n");
        for(int i = 0; i < lado + 6; i++){
            System.out.print("*");
        }
        System.out.print("\n");
        System.out.print(" ");
        for(int i = 0; i < lado + 4; i++){
            System.out.print("*");
        }
        System.out.print(" ");
        System.out.print("\n");
        System.out.print("  ");
        for(int i = 0; i < lado + 2; i++){
            System.out.print("*");
        }
        System.out.print("  ");
        System.out.print("\n");
        System.out.print("   ");
        for(int i = 0; i < lado; i++){
            System.out.print("*");
        }
        System.out.print("   ");

        leer.close();
    }
}
