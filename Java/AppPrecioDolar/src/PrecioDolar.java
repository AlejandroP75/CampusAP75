import java.time.LocalDate;

public class PrecioDolar {
    
    private double precio;
    private LocalDate fecha;

    public PrecioDolar(double precio, LocalDate fecha) {
        this.precio = precio;
        this.fecha = fecha;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public void setFecha(LocalDate fecha) {
        this.fecha = fecha;
    }

    
}
