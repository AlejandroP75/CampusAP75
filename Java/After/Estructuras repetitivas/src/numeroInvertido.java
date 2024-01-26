import java.util.Scanner;

public class numeroInvertido {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese numero: ");
        String num = leer.nextLine();

        String[] split = num.split("");

        for(int i = split.length-1; i >= 0; i--){
            System.out.print(split[i]);
        }

        leer.close();
    }
}
