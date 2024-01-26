import java.util.Arrays;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        Integer [] datosNumericos = {5,7,9,1,2,0,12,45};

        Arrays.sort(datosNumericos, Collections.reverseOrder());
        System.out.println(Arrays.toString(datosNumericos));
        for(int i = 0; i < datosNumericos.length; i++){
            System.out.println(datosNumericos[i]);
        }
    }
}
