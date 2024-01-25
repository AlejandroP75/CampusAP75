import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Eje10 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese su fecha de nacimiento (Formato: DD/MM/YYYY): ");
        String fechaNacimientoStr = leer.nextLine();

        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate fechaNacimiento = LocalDate.parse(fechaNacimientoStr, formato);

        LocalDate fechaActual = LocalDate.now();
        
        int años = fechaActual.getYear() - fechaNacimiento.getYear();
        int meses = fechaActual.getMonthValue() - fechaNacimiento.getMonthValue();
        int días = fechaActual.getDayOfMonth() - fechaNacimiento.getDayOfMonth();

        if (meses < 0 || (meses == 0 && días < 0)) {
            años--;
        }

        System.out.println("Usted tiene " + años + " años");

        leer.close();
    }

}
