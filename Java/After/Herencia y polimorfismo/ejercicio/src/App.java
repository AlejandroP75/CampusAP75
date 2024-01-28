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
                    creardisco();
                    break;
                case 3:
                    verlibros();
                    break;
                case 4:
                    verdiscos();
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
            System.out.print("\nMENU\n");
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
        System.out.print("\nCREAR LIBRO");
        System.out.print("\n\nIngresa el titulo --> ");
        leer.nextLine();
        String titulo = leer.nextLine();
        System.out.print("Ingresa el precio --> $");
        float precio = leer.nextFloat();
        System.out.print("Ingresa el numero de paginas --> ");
        int paginas = leer.nextInt();
        System.out.print("Ingresa el año de publicación --> ");
        int año = leer.nextInt();

        Libro nuevoLibro = new Libro(titulo, precio, paginas, año);
        libros.add(nuevoLibro);

        System.out.print("\nLibro añadido con exito\n");
    }

    public static void creardisco(){
        System.out.print("\nCREAR DISCO");
        System.out.print("\n\nIngresa el titulo --> ");
        leer.nextLine();
        String titulo = leer.nextLine();
        System.out.print("Ingresa el precio --> $");
        float precio = leer.nextFloat();
        System.out.print("Ingresa la duración en minutos --> ");
        int duracion = leer.nextInt();

        Disco nuevoDisco = new Disco(titulo, precio, duracion);
        discos.add(nuevoDisco);

        System.out.print("\nDisco añadido con exito\n");
    }

    public static void verlibros(){
        System.out.print("\nVER LIBROS\n");
        int cont = 1;

        for (Libro libro : libros) {
            System.out.print("\nLibro #" + cont + "\n");
            System.out.print("--------------------------\n");
            System.out.print(libro.getTitulo() + "\n");
            System.out.print(libro.getPrecio() + "\n");
            System.out.print(libro.getNumeroPag() + "\n");
            System.out.print(libro.getAñoPubli() + "\n");
            cont++;
        }
        System.out.print("\nIngresa cualquier letra o numero para continuar al menu --> ");
        leer.next();
    }

    public static void verdiscos(){
        System.out.print("\nVER DISCOS\n");
        int cont = 1;

        for (Disco disco : discos) {
            System.out.print("\nDisco #" + cont + "\n");
            System.out.print("--------------------------\n");
            System.out.print(disco.getTitulo() + "\n");
            System.out.print(disco.getPrecio() + "\n");
            System.out.print(disco.getDuracionMinu() + "\n");
            cont++;
        }
        System.out.print("\nIngresa cualquier letra o numero para continuar al menu --> ");
        leer.next();
    }
}
