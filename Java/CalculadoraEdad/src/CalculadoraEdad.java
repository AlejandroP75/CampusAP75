import java.util.Calendar;

public class CalculadoraEdad {
    private int diaNacimiento;
    private int mesNacimiento;
    private int annoNacimiento;
    
    public CalculadoraEdad(int diaNacimiento, int mesNacimiento, int annoNacimiento) {
        this.diaNacimiento = diaNacimiento;
        this.mesNacimiento = mesNacimiento;
        this.annoNacimiento = annoNacimiento;
    }

    public int getDiaNacimiento() {
        return diaNacimiento;
    }

    public void setDiaNacimiento(int diaNacimiento) {
        this.diaNacimiento = diaNacimiento;
    }

    public int getMesNacimiento() {
        return mesNacimiento;
    }

    public void setMesNacimiento(int mesNacimiento) {
        this.mesNacimiento = mesNacimiento;
    }

    public int getAnnoNacimiento() {
        return annoNacimiento;
    }

    public void setAnnoNacimiento(int annoNacimiento) {
        this.annoNacimiento = annoNacimiento;
    }

    public int calcularEdad(){
        Calendar fecha1 = Calendar.getInstance();
        int diaActual = fecha1.get(Calendar.DATE);
        int mesActual = fecha1.get(Calendar.MONTH) + 1;
        int annioActual = fecha1.get(Calendar.YEAR);
        
        return 0;
    }
}
