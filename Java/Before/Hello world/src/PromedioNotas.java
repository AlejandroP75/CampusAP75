import java.util.Scanner;

public class PromedioNotas {
    public static void main(String arg[]) {
        Scanner leer = new Scanner(System.in);
        int nota1, nota2, nota3, nota4 ;
        System.out.println("Ingrese nota1: ");
        nota1 = leer.nextInt();
        System.out.println("Ingrese nota2: ");
        nota2 = leer.nextInt();
        System.out.println("Ingrese nota3: ");
        nota3 = leer.nextInt();
        System.out.println("Ingrese nota4: ");
        nota4 = leer.nextInt();
        double promedio = (nota1 + nota2 + nota3 + nota4) / 4;
        System.out.println("El promedio de las notas es: " + promedio);
        leer.close();
    }
}
