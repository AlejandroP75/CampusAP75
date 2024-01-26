import java.util.Scanner;

public class historigrama {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        int contPos = 0;
        int contNeg = 0;

        System.out.println("Ingrese varios valores, termine con cero: ");
        while (true) {
            int num = leer.nextInt();
            if(num < 0){
                contNeg++;
            }else if (num > 0){
                contPos++;
            }else{
                break;
            }
        }

        System.out.print("Positivos: ");
        for(int i = 0; i < contPos; i++){
            System.out.print("*");
        }

        System.out.print("\nNegativos: ");
        for(int i = 0; i < contNeg; i++){
            System.out.print("*");
        }

        leer.close();
    }
}
