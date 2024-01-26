import java.util.Scanner;

public class Eje12 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese su estatura (metros): ");
        float estatura = leer.nextFloat();

        System.out.print("Ingrese su peso (kilos): ");
        float peso = leer.nextFloat();

        System.out.print("Ingrese su edad (años): ");
        int edad = leer.nextInt();

        double imc = peso / Math.pow(estatura, 2);

        if(imc < 22){
            if(edad < 45){
                System.out.print("Su condición de riesgo es baja");
            }
            else{
                System.out.print("Su condición de riesgo es media");
            }
        }else{
            if(edad < 45){
                System.out.print("Su condición de riesgo es media");
            }
            else{
                System.out.print("Su condición de riesgo es alta");
            }
        }

        leer.close();
    }
}
