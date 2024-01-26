import java.util.Scanner;

public class NumeroInvertido {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese un numero: ");
        String num = leer.next();
        String[] numeroSeparado = num.split("");

        for(int i = num.length(); i <= num.length(); i--){
            if(i == 0){
                break;
            }
            System.out.print(numeroSeparado[(i-1)]);
        }
        leer.close();
    }
}
