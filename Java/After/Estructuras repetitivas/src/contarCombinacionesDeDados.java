import java.util.Scanner;

public class contarCombinacionesDeDados {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese el puntaje: ");
        int punt = leer.nextInt();

        int var = 0;
        int cont = 0;

        if(punt < 2 || punt > 12){
            System.out.print("Hay 0 combinaciones para obtener " + punt);
        }else{
            for(int j = 1; j < 7; j++){
                for(int i = 1; i < 7; i++){
                    var = j + i;
                    if(var == punt){
                        cont++;
                    }
                }
            }
            System.out.print("Hay " + cont + " combinaciones para obtener " + punt);
        }

        leer.close();
    }
}
