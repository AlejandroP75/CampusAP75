import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese su fecha de nacimiento: ");
        System.out.print("\nDía: ");
        String dia = leer.next();
        System.out.print("Mes: ");
        String mes = leer.next();
        System.out.print("Año: ");
        String año = leer.next();

        calcularEdad usuario = new calcularEdad(dia, mes, año);

        System.out.print("\nUsted tiene " + usuario.calcularedad() + " años.");

        leer.close();
    }
}
