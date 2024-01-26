import java.util.Calendar;

public class App {
    public static void main(String[] args) throws Exception {
        Calendar fecha1 = Calendar.getInstance();
        System.out.println(fecha1.get(Calendar.DATE));
        System.out.println(fecha1.get(Calendar.MONTH + 1));
        System.out.println(fecha1.get(Calendar.YEAR));
    }
}
