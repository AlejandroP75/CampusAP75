import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class App {
    private static Scanner leer = new Scanner(System.in);
    private static List<Departamento> departamentos = new ArrayList<>();
    private static List<Municipio> municipios = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        int opc;

        opc = menu();

        switch (opc) {
            case 1:
                System.out.println("AGREGAR DEPARTAMENTO");
                departamentos.add(agregarDepartmento());
                break;
            case 2:
            System.out.println("AGREGAR MUNICIPIO");
                break;
            case 3:
            System.out.println("INFORME DE TODOS LOS MUNICIPIOS");
                break;
            case 4:
            System.out.println("BUSCAR MUNICIPIO");
                break;
            case 5:
            System.out.println("ELIMINAR UN MUNICIPIO");
                break;
            case 6:
            System.out.println("CALCULAR CENSO DE UN DEPARTAMENTO");
                break;
            case 7:
            System.out.println("CALCULAR EL AREA TOTAL DE UN DEPARTAMENTO");
                break;
            default:
                break;
        }



        leer.close();
    }
    
    private static int menu(){
        int op;
        while (true) {
            
            System.out.println("--- MENU ---");
            System.out.println("\n1.Agregar departamento");
            System.out.println("2.Agregar municipio");
            System.out.println("3.Informe de todos los municipios");
            System.out.println("4.Buscar municipio");
            System.out.println("5.Eliminar un municipio");
            System.out.println("6.Calcular censo de un departamento");
            System.out.println("7.Calcular el area total de un departamento");
            System.out.print("\nSeleccione una opcion del menu --> ");
            op = leer.nextInt();
            if (op < 1 || op > 7){
                System.out.println("Error, opción invalida");
                continue;
            }
            break;
        }
        return op;
    }

    private static Departamento agregarDepartmento(){
        String nombre;
        Municipio[] municipios;
        Gobernador gobernador;
        
        System.out.println("Ingrese el nombre del departamento --> ");
        nombre = leer.nextLine();
        while (true){
            municipios.add(agregarMunicipio());
            break;
        }

        return new Departamento(nombre, null, null);
    }

    private static Municipio agregarMunicipio(){
        String nombre;
        int poblacion;
        float area;

        System.out.println("Ingrese el nombre del municipio --> ");
        nombre = leer.nextLine();
        System.out.println("Ingrese el numero de la población del municipio --> ");
        poblacion = leer.nextInt();
        System.out.println("Ingrese el area del municipio");
        area = leer.nextFloat();

        return new Municipio(nombre, poblacion, area);
    }
}
