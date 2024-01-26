import java.util.Scanner;

public class tiempoDeViaje {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        int tramos = 0;

        while (true) {
            System.out.print("Duracion tramo: ");
            int tramo = leer.nextInt();
            if(tramo == 0){
                break;
            }
            tramos = tramos + tramo;
        }

        int horas = 0;

        while (tramos > 60) {
            tramos = tramos - 60;
            horas++;
        }

        System.out.printf("Timepo total de viaje: %d:%02d horas", horas, tramos);

        leer.close();
    }
}
