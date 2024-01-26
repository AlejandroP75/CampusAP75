import java.util.Scanner;

public class Eje13 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Juegos ganados por A: ");
        int a = leer.nextInt();

        System.out.print("Juegos ganados por B: ");
        int b = leer.nextInt();

        if(((a >= 7) && (b >= 7)) || ((a == 7) && (b < 5)) || ((b == 7) && (a < 5)) || (a < 0) || (b < 0)){
            System.out.print("El partido es invalido");
        }else{
            if((a >= 5) && (b >= 5)){
                if(a == 7){
                    System.out.print("Gano A");
                }else if(b == 7){
                    System.out.print("Gano B");
                }else{
                    System.out.print("El partido continua");
                }
            }else{
                if((a == 6) && (b >= 4)){
                    System.out.print("Gano A");
                }else if((b == 6) && (a >= 4)){
                    System.out.print("Gano B");
                }else{
                    System.out.print("El partido continua");
                }
            }
        }

        leer.close();
    }
}
