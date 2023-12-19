import java.util.Scanner;

public class ParteDecimal {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        float num = leer.nextFloat();
        float num2 = num - (int) num;
        if(num2 < 0){
            num2 = num2 * -1;
        }
        System.out.println(Math.round(num2*100.0)/100.0);
        leer.close();
    }
}
