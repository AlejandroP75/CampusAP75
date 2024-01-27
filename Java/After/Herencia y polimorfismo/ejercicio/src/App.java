import java.util.ArrayList;
import java.util.Scanner;

public class App {
    private static Scanner leer = new Scanner(System.in);
    private static ArrayList<Libro> libros = new ArrayList<>();
    private static ArrayList<Disco> discos = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        while (true) {
            int op = menu();
            boolean sal = false;
            switch (op) {
                case 1:
                    crearlibro();
                    break;
                case 2:
                    System.out.print("CREAR DISCO");
                    break;
                case 3:
                    System.out.print("VER LIBROS");
                    break;
                case 4:
                    System.out.print("VER DISCOS");
                    break;
                case 5:
                    System.out.print("SALIDA");
                    sal = true;
                    break;
                default:
                    System.out.print("ERROR");
                    break;
            }
            if(sal){
                break;
            }
        }
        
    }
    
    public static int menu(){
        int opc;
        while (true) {
            System.out.print("MENU\n");
            System.out.print("\n1.Crear libro");
            System.out.print("\n2.Crear disco");
            System.out.print("\n3.Ver libros");
            System.out.print("\n4.Ver discos");
            System.out.print("\n5.Salir");
            System.out.print("\n\nSeleccion el numero de la opción deseada --> ");
            opc = leer.nextInt(); 
            if(opc < 1 || opc > 5){
                System.out.println("\nOpción no valida\n");
                continue;
            }
            break;
        }
        return opc;
    }
    
    public static void crearlibro(){
        System.out.print("CREAR LIBRO");
        
    }
}
