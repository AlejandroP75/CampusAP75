import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class calcularEdad {
    private String diaNacimiento;
    private String mesNacimiento;
    private String añoNacimiento;

    public calcularEdad(String diaNacimiento, String mesNacimiento, String añoNacimiento) {
        this.diaNacimiento = diaNacimiento;
        this.mesNacimiento = mesNacimiento;
        this.añoNacimiento = añoNacimiento;
    }


    public String getDiaNacimiento() {
        return diaNacimiento;
    }

    public void setDiaNacimiento(String diaNacimiento) {
        this.diaNacimiento = diaNacimiento;
    }

    public String getMesNacimiento() {
        return mesNacimiento;
    }

    public void setMesNacimiento(String mesNacimiento) {
        this.mesNacimiento = mesNacimiento;
    }

    public String getAñoNacimiento() {
        return añoNacimiento;
    }

    public void setAñoNacimiento(String añoNacimiento) {
        this.añoNacimiento = añoNacimiento;
    }

    public int calcularedad(){
        LocalDate fechaHoy = LocalDate.now();
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        int mesNum = Integer.parseInt(mesNacimiento);
        int diaNum = Integer.parseInt(diaNacimiento);

        if(mesNum < 10){
            mesNacimiento = "0" + mesNacimiento;
        }

        if(diaNum < 10){
            diaNacimiento = "0" + diaNacimiento;
        }

        String crear = diaNacimiento + "/" + mesNacimiento + "/" + añoNacimiento;
        LocalDate fechaNacimiento = LocalDate.parse(crear, formato);

        int años = fechaHoy.getYear() - fechaNacimiento.getYear();
        int meses = fechaHoy.getMonthValue() - fechaNacimiento.getMonthValue();
        int días = fechaHoy.getDayOfMonth() - fechaNacimiento.getDayOfMonth();

        if (meses < 0 || (meses == 0 && días < 0)) {
            años--;
        }

        return años;
    }
}

