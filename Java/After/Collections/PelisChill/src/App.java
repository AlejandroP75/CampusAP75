import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static Scanner leer = new Scanner(System.in);
    public static List<Cliente> clientes = new ArrayList<>();
    public static List<Pelicula> peliculas = new ArrayList<>();
    public static void main(String[] args) throws Exception {
            datosPrueba();

            int opc =menu();
            switch (opc) {
                case 1:
                    
                    break;
                case 2:
                    
                    break;
                case 3:
                    
                    break;
                case 4:
                    
                    break;
                case 5:
                    
                    break;
                case 6:
                    
                    break;
                case 7:
                    
                    break;
                case 8:
                    
                    break;
            
                default:
                    break;
            }

        }
        
    public static void datosPrueba(){
        Cliente c1 = new Cliente("María", "maria@gmail.com", 311334455);
        Cliente c2 = new Cliente("Carlos", "carlos@hotmail.com", 310112233);
        Cliente c3 = new Cliente("Laura", "laura@yahoo.com", 315556677);
        Cliente c4 = new Cliente("Ana", "ana@gmail.com", 318889900);
        Cliente c5 = new Cliente("Pedro", "pedro@gmail.com", 317778899);
        
        Pelicula p1 = new Pelicula(2, "El Renacido", "Leonardo DiCaprio", "Aventura", 15000, 25);
        Pelicula p2 = new Pelicula(3, "La La Land", "Emma Stone", "Musical", 10000, 15);
        Pelicula p3 = new Pelicula(4, "Inception", "Christopher Nolan", "Ciencia Ficción", 14000, 22);
        Pelicula p4 = new Pelicula(5, "El Gran Hotel Budapest", "Ralph Fiennes", "Comedia", 11000, 18);
        Pelicula p5 = new Pelicula(6, "Interestelar", "Matthew McConaughey", "Drama", 16000, 30);

        clientes.add(c1);
        clientes.add(c2);
        clientes.add(c3);
        clientes.add(c4);
        clientes.add(c5);

        peliculas.add(p1);
        peliculas.add(p2);
        peliculas.add(p3);
        peliculas.add(p4);
        peliculas.add(p5);
    }

    public static int menu(){
        int op;
        while (true) {
            System.out.print("\n---------------");
            System.out.print("\nMENU");
            System.out.print("\n---------------");
            System.out.print("\n1.Añadir cliente");
            System.out.print("\n2.Añadir pelicula");
            System.out.print("\n3.Mostrar Pelicula");
            System.out.print("\n4.Cambiar precio pelicula");
            System.out.print("\n5.Eliminar pelicula");
            System.out.print("\n6.Calcular precio pelicula");
            System.out.print("\n7.Alquilar pelicula");
            System.out.print("\n8.Salir");
            System.out.print("\nIngrese el numero de la opción deseada --> ");
            op = leer.nextInt();
            if (op < 1 || op > 8) {
                System.out.print("\nOpcion no disponible, vuelva a intentarlo");
                continue;
            }
            break;
        }
        return op;
    }
}
