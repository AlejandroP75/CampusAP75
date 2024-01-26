import java.util.Scanner;

public class HoraFutura {
    public static void main(String args[]) {
        int horaAcN;
        Scanner leer = new Scanner(System.in);
        System.out.println("Hora actual:");
        int horaAc = leer.nextInt();
        System.out.println("Cantidad de horas: ");
        int cantHo = leer.nextInt();
        horaAcN = horaAc + cantHo;
        if(horaAcN > 48){
            horaAcN = horaAcN - 48;
        }
        System.out.println("En " + cantHo + " horas, el reloj marcara las " + horaAcN);
        leer.close();
    }
}
