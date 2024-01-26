import java.util.Scanner;

public class Ej4ReglamentoEvaluaciones {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);

        double c1, c2, c3, examen, promedio;

        while(true){
            System.out.print("C1: ");
            c1 = leer.nextDouble();

            System.out.print("C2: ");
            c2 = leer.nextDouble();

            if(c1 < 2.0 && c2 < 2.0){
                System.out.println("Reprobado");
                break;
            }else if(c1 > 9.0 && c2 > 9.0){
                System.out.println("Aprobado");
                break;
            }
            System.out.print("C3: ");
            c3 = leer.nextDouble();

            promedio = (c1 + c2 + c3) / 3;

            if(promedio < 3.0){
                System.out.println("Reprobado");
                break;
            }else if(promedio >= 7){
                System.out.println("Aprobado");
                break;
            }

            System.out.print("Examen: ");
            examen = leer.nextDouble();

            if(examen >= 5.0){
                System.out.println("Aprobado");
                break;
            }else{
                System.out.println("Reprobado");
                break;
            }
        }
        leer.close();
    }
}
