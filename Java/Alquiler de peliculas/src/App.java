import java.util.ArrayList;
import java.util.Scanner;

public class App {

    public static void main(String[] args) throws Exception {
        Scanner leer = new Scanner(System.in);
        ArrayList<Pelicula> Catalogo = new ArrayList<Pelicula>();
        System.out.println("Bienvenido\n");
        int opc, opc2;
        while (true){
            while (true) {
                System.out.println("MENU PELISCHILL\n");
                System.out.println("1.Peliculas");
                System.out.println("2.Clientes");
                System.out.println("3.Alquilar pelicula\n");
                System.out.print("Digite el numero de la opción deseada --> ");
                opc = leer.nextInt();
                if (opc < 1 || opc > 3){
                    System.out.println("Opción invalida");
                    continue;
                }
                break;
            }
            switch (opc) {
                case 1:
                    while (true) {
                        System.out.println("\nMENU PELICULAS\n");
                        System.out.println("1.Registrar pelicula");
                        System.out.println("2.Modificar pelicula");
                        System.out.println("3.Eliminar pelicula");
                        System.out.print("Digite el numero de la opción deseada --> ");
                        opc2 = leer.nextInt();
                        if (opc2 < 1 || opc2 > 3){
                            System.out.println("Opción invalida");
                            continue;
                        }
                        break;
                    }
                    switch (opc2) {
                        case 1:
                            System.out.println("\nREGISTRAR PELICULA\n");
                            System.out.println("Ingrese el titulo de la pelicula --> ");
                            leer.nextLine();
                            String titulo = leer.nextLine();
                            System.out.println("Ingrese el genero de la pelicula --> ");
                            String genero = leer.nextLine();
                            System.out.println("Ingrese el precio de alquiler --> ");
                            double precio_alquiler = leer.nextDouble();
                            System.out.println("Ingrese el nombre del director --> ");
                            leer.nextLine();
                            String director = leer.nextLine();
                            System.out.println("Ingrese el % de descuento --> ");
                            double descuento = leer.nextDouble();
                            Pelicula peliprueba = new Pelicula(1, titulo, genero, precio_alquiler, director, descuento);
                            Catalogo.add(peliprueba);
                            System.out.println(Catalogo);
                            break;
                        case 2:
                            System.out.println("\nMODIFICAR PELICULA\n");
                            while (true) {
                                System.out.println("\n¿Que desea modificar?\n");
                                System.out.println("1.Titulo");
                                System.out.println("2.Genero");
                                System.out.println("3.Precio Alquiler");
                                System.out.println("4.Director");
                                System.out.println("5.Descuento");
                                System.out.print("Digite el numero de la opción deseada --> ");
                                opc2 = leer.nextInt();
                                if (opc2 < 1 || opc2 > 5){
                                    System.out.println("Opción invalida");
                                    continue;
                                }
                                break;
                                
                            }
                            break;
                        case 3:
                            System.out.println("\nELIMINAR PELICULA\n");
                            break;
                        default:
                            System.out.println("ERROR");
                            break;
                    }
                    break;
                case 2:
                    System.out.println("\nMENU CLIENTES\n");
                    break;
                case 3:
                    System.out.println("\nMenu alquiler de peliculas");
                    break;
                default:
                    System.out.println("ERROR");
                    break;
            }
        leer.close();}
    }
}
