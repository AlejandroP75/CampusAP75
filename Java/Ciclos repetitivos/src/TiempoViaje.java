import java.util.Scanner;

public class TiempoViaje {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);
        int suma = 0;;

        while (true) {
            System.out.println("Duracion tramo: ");
            int num = leer.nextInt();
            if(num == 0){
                break;
            }
            suma = suma + num;
        }

        int horas = 0, minutos = suma;
        
        while (minutos >= 60) {
            horas = horas + 1;
            minutos = minutos - 60;
        }
        System.out.println("Tiempo total de viaje: " + horas + ":" + minutos + " horas");
        leer.close();
    }
}
