import java.text.DecimalFormat;
import java.util.Scanner;

public class Ej1AlzasDolar {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.00");

        System.out.print("Ingrese el numero de días: ");
        int dias = leer.nextInt();
        double[] dolarDias = new double[dias], alzas = new double[dias];

        for(int i = 0; i < dias; i++){
            System.out.print("Ingrese el valor del día " + (i+1) + ": ");
            dolarDias[i] = leer.nextDouble();
        }
        for(int i = 0; i < dias - 1; i++){
            alzas[i] = (dolarDias[i] - dolarDias[i + 1]) * -1;
        }

        double mayor = 0;

        for(int i = 0; i < dias; i++){
            if(mayor < alzas[i]){
                mayor = alzas[i];
            }
        }
        if(mayor != 0){
            System.out.println("El mayor alza fue de " + df.format(mayor) + " pesos");
        }else{
            System.out.println("No hubo alzas");
        }

        leer.close();
    }
}