import java.util.ArrayList;
import java.util.Scanner;

public class masCortaYMasLarga {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        String mayor = ""; 
        String menor = "jajajajajajajajajajajajajaja";

        ArrayList<String> palabras = new ArrayList<>();

        System.out.print("Cantidad de palabras: ");
        int n = leer.nextInt();

        for(int i = 0; i < n; i++){
            System.out.print("Palabra " + (i + 1) + " : ");

            String palabra = leer.next();
            palabras.add(palabra);
        }

        for (String string : palabras) {
            if(string.length() < menor.length()){
                menor = string;
            }
            if(string.length() > mayor.length()){
                mayor = string;
            }
        }

        System.out.print("La palabra mas larga es " + mayor);
        System.out.print("\nLa palabra mas corta es " + menor);


        leer.close();
    }
}
