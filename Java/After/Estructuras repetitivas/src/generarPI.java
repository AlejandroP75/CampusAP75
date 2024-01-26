import java.util.Scanner;

public class generarPI {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("n: ");
        int n = leer.nextInt();
        
        double sum = 0;
        float f = 2;

        for(int i = 0; i < (n*2); i = i + 2){
            double lol = (Math.pow(-1, f)* 1);
            int lel = (i+1);
            sum = sum + (lol/lel);
            f++;
        }

        System.out.print(sum * 4);

        leer.close();
    }
}
