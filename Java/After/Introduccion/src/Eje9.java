import java.util.Scanner;

public class Eje9 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Palabra 1: ");
        String p1 = leer.nextLine();

        System.out.print("Palabra 2: ");
        String p2 = leer.nextLine();

        int num1 = p1.length();
        int num2 = p2.length();

        if(num1 > num2){
            System.out.print("La palabra " + p1 + " tiene " + (num1 - num2) + " letras mas que " + p2);
        }else if(num2 > num1){
            System.out.print("La palabra " + p2 + " tiene " + (num2 - num1) + " letras mas que " + p1);
        }else{
            System.out.print("Las palabras tienen el mismo largo");
        }

        leer.close();
    }
}
