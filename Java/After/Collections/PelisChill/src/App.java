import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;


public class App {
    public static Scanner leer = new Scanner(System.in);
    public static List<Cliente> clientes = new ArrayList<>();
    public static List<Pelicula> peliculas = new ArrayList<>();
    public static void main(String[] args) throws Exception {
            datosPrueba();

            boolean sal = false;
            while (true) {
                int opc =menu();
                switch (opc) {
                    case 1:
                        añadirCliente();
                        break;
                    case 2:
                        añadirPelicula();
                        break;
                    case 3:
                        mostrarPelicula();
                        break;
                    case 4:
                        cambiarPrecio();
                        break;
                    case 5:
                        eliminarPelicula();
                        break;
                    case 6:
                        calcularPrecio();
                        break;
                    case 7:
                        
                        break;
                    case 8:
                        System.out.print("\nSALIDA");
                        sal = true;
                        break;
                    default:
                        break;
                }
                if (sal) {
                    break;
                }
            }

        }
        
    public static void datosPrueba(){
        Cliente c1 = new Cliente("María", "maria@gmail.com", 311334455);
        Cliente c2 = new Cliente("Carlos", "carlos@hotmail.com", 310112233);
        Cliente c3 = new Cliente("Laura", "laura@yahoo.com", 315556677);
        Cliente c4 = new Cliente("Ana", "ana@gmail.com", 318889900);
        Cliente c5 = new Cliente("Pedro", "pedro@gmail.com", 317778899);
        
        Pelicula p1 = new Pelicula(1, "El Renacido", "Leonardo DiCaprio", "Aventura", 15000, 25);
        Pelicula p2 = new Pelicula(2, "La La Land", "Emma Stone", "Musical", 10000, 15);
        Pelicula p3 = new Pelicula(3, "Inception", "Christopher Nolan", "Ciencia Ficción", 14000, 22);
        Pelicula p4 = new Pelicula(4, "El Gran Hotel Budapest", "Ralph Fiennes", "Comedia", 11000, 18);
        Pelicula p5 = new Pelicula(5, "Interestelar", "Matthew McConaughey", "Drama", 16000, 30);

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
            System.out.print("\n\n---------------");
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
            System.out.print("\n\nIngrese el numero de la opción deseada --> ");
            op = leer.nextInt();
            if (op < 1 || op > 8) {
                System.out.print("\nOpcion no disponible, vuelva a intentarlo");
                continue;
            }
            break;
        }
        return op;
    }

    public static void añadirCliente(){
        System.out.print("\nAÑADIR CLIENTE\n");
        System.out.print("\nIngrese el nombre --> ");
        leer.nextLine();
        String nom = leer.nextLine();
        System.out.print("Ingrese el correo electronico --> ");
        String cor = leer.next();
        System.out.print("Ingrese el numero de telefono --> ");
        int tel = leer.nextInt();

        Cliente nueCliente = new Cliente(nom, cor, tel);
        clientes.add(nueCliente);

        System.out.print("\n--- CLIENTE AÑADIDO CON EXITO ---");

        System.out.print("\n\nPresione enter para continuar --> ");
        leer.nextLine();
        leer.nextLine();
    }

    public static void añadirPelicula(){
        System.out.print("\nAÑADIR PELICULA\n");
        int id;
        while (true) {
            boolean esta = false;
            System.out.print("\nIngrese el id --> ");
            id = leer.nextInt();
            for (Pelicula i : peliculas) {
                if (id == i.getId()) {
                    esta = true;
                }
            }
            if (esta == true) {
                System.out.print("Id ya registrado, vuelva a intentarlo");
                continue;
            }
            break;
        }

        System.out.print("Ingrese el titulo --> ");
        leer.nextLine();
        String nom = leer.nextLine();
        System.out.print("Ingrese el director --> ");
        String dir = leer.nextLine();
        System.out.print("Ingrese el genero --> ");
        String gen = leer.nextLine();
        System.out.print("Ingrese el precio --> ");
        float pre = leer.nextFloat();
        System.out.print("Ingrese el porcentaje de descuento --> ");
        int des = leer.nextInt();

        Pelicula nuePelicula = new Pelicula(id, nom, dir, gen, pre, des);
        peliculas.add(nuePelicula);

        System.out.print("\n--- PELICULA AÑADIDA CON EXITO ---");

        System.out.print("\nPresione enter para continuar --> ");
        leer.nextLine();
        leer.nextLine();
    }

    public static void mostrarPelicula(){
        System.out.print("\nMOSTRAR PELICULAS\n");
        int opc, nueid;
        while (true) {
            System.out.print("\n1.Buscar por id");
            System.out.print("\n2.Mostrar todas las peliculas");
            System.out.print("\n\nIngrese el numero de la opción que desea --> ");
            opc = leer.nextInt();
            if (opc < 1 || opc > 2) {
                System.out.print("Opción invalida, vuelva a intentarlo");
                continue;
            }
            break;
        }
        if (opc == 1) {
            System.out.print("\nIngrese el id de la pelicula --> ");
            nueid = leer.nextInt();
            for (Pelicula i : peliculas) {
                if (nueid == i.getId()) {
                    System.out.print("\nId: " + i.getId());
                    System.out.print("\nTitulo: " + i.getTitulo());
                    System.out.print("\nDirector: " + i.getDirector());
                    System.out.print("\nGenero: " + i.getGenero());
                    System.out.printf("\nPrecio: %.0f", i.getPrecio());
                    System.out.print("\nDescuento: " + i.getDescuento() + "%");
                    System.out.print("\n\nPresione enter para continuar --> ");
                    leer.nextLine();
                    leer.nextLine();
                }
            }
        }else{
            int cont = 1;
            for (Pelicula i : peliculas) {
                    System.out.print("\n\nPelicula #" + cont);
                    System.out.print("\nId: " + i.getId());
                    System.out.print("\nTitulo: " + i.getTitulo());
                    System.out.print("\nDirector: " + i.getDirector());
                    System.out.print("\nGenero: " + i.getGenero());
                    System.out.printf("\nPrecio: %.0f", i.getPrecio());
                    System.out.print("\nDescuento: " + i.getDescuento() + "%");
                    cont++;
            }
            System.out.print("\n\nPresione enter para continuar --> ");
            leer.nextLine();
            leer.nextLine();
        }

    }

    public static void cambiarPrecio(){
        int id;
        System.out.print("\nCAMBIAR PRECIO PELICULA\n");
        System.out.print("\nIngrese el id de la pelicula --> ");
        id = leer.nextInt();
        for (Pelicula i : peliculas) {
            if (id == i.getId()) {
                System.out.printf("\nEl precio actual de la pelicula es: %.0f", i.getPrecio());
                System.out.print("\nIngrese el nuevo precio de la pelicula --> ");
                float nuePrecio = leer.nextFloat();

                i.setPrecio(nuePrecio);
                break;
            }
        }
        System.out.print("\nPRECIO CAMBIADO CON EXITO");

        System.out.print("\n\nPresione enter para continuar --> ");
        leer.nextLine();
        leer.nextLine();
    }

    public static void eliminarPelicula(){
        int id;
        System.out.print("\nELIMINAR PELICULA\n");
        System.out.print("\nIngrese el id de la pelicula --> ");
        id = leer.nextInt();

        Iterator<Pelicula> iterator = peliculas.iterator();

        while (iterator.hasNext()) {
            Pelicula pelicula = iterator.next();
    
            if (id == pelicula.getId()) {
                iterator.remove();
                break;
            }
        }
        System.out.print("\nPELICULA ELIMINADA CON EXITO");

        System.out.print("\n\nPresione enter para continuar --> ");
        leer.nextLine();
        leer.nextLine();
    }
    public static void calcularPrecio(){
        
    }
}
