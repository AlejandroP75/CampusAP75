import java.util.Scanner;

public class PalabraMasLarga {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);

        System.out.println("Palabra 1:");
        String pal1 = leer.nextLine();

        System.out.println("Palabra 2:");
        String pal2 = leer.nextLine();

        int tamp1 = pal1.length(), tamp2 = pal2.length();

        if(tamp1 > tamp2){
           System.out.println("La palabra " + pal1 + " tiene " + (tamp1 - tamp2) + " mas letras que " + pal2);
        }else if(tamp2 > tamp1){
            System.out.println("La palabra " + pal2 + " tiene " + (tamp2 - tamp1) + " mas letras que " + pal1);
        }else{
            System.out.println("Las dos palabras tienen el mismo largo");
        }
        leer.close();
    }
}
