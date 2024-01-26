import java.util.Scanner;

public class QueNotaNecesito {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese nota certamen 1:");
        int cert1 = leer.nextInt();
        System.out.println("Ingrese nota certamen 2:");
        int cert2 = leer.nextInt();
        System.out.println("Ingrese nota laboratorio:");
        int lab = leer.nextInt();

        double nc = (59.63333333333333 - (lab * 0.3)) / 0.7;
        double cert3 = (3 * nc) - cert1 - cert2;
        System.out.println("Necesita nota " + cert3 + " en el certamen 3");
        leer.close();
    }
}
