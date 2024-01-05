import java.util.Calendar;

public class App {
    public static void main(String[] args) throws Exception {
        Calendar fechaActual = Calendar.getInstance();
        String cadenaFecha = String.format("%04d-%02d-%02d-%02d",
          fechaActual.get(Calendar.YEAR),
          fechaActual.get(Calendar.MONTH)+1,
          fechaActual.get(Calendar.DAY_OF_MONTH));
        System.out.println(cadenaFecha);
    }
}
