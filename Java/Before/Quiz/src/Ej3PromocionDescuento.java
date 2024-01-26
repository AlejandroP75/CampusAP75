import java.text.DecimalFormat;
import java.util.Scanner;

public class Ej3PromocionDescuento {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#");
        int n, cantProd, total = 0;

        System.out.print("n: ");
        n = leer.nextInt();
        System.out.print("Cantidad productos: ");
        cantProd = leer.nextInt();
        int[] productos = new int[cantProd];

        for(int i = 0; i < cantProd; i++){
            System.out.print("Precio producto " + (i + 1) + ": ");
            productos[i] = leer.nextInt();
            total = total + productos[i];
        }

        System.out.println("Total: " + total);

        double des1 = 0, des2 = 0, des3 = 0;

        for(int i = 0; i < n; i++){
            if(i >= cantProd){
                break;
            }
            des1 = des1 + (productos[i] * 0.2);
        }
        for(int i = (0 + n); i < (n*2); i++){
            if(i >= cantProd){
                break;
            }
            des2 = des2 + (productos[i] * 0.1);
        }
        for(int i = (0 + (2*n)); i < (n*3); i++){
            if(i >= cantProd){
                break;
            }
            des3 = des3 + (productos[i] * 0.05);
        }

        double descuento = des1 + des2 + des3;
        System.out.println("Descuento: " + df.format(descuento));
        System.out.println("Por pagar: " + (df.format((total - descuento))));

        leer.close();
    }
}
