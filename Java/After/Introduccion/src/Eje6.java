import java.util.Scanner;

public class Eje6 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Hora actual: ");
        int hora = leer.nextInt();

        System.out.print("Cantidad de horas: ");
        int canHora = leer.nextInt();

        int sum = hora + canHora;

        while (sum > 23) {
            sum = sum - 24;
        }

        System.out.printf("En %d horas, el reloj marcara las %d", canHora, sum);

        leer.close();
    }
}
