import java.time.LocalDateTime;

public class AlquilerPelicula {
    private LocalDateTime fechaInicio;
    private LocalDateTime fechaEntrega;
    private int id;
    Pelicula pelicula;
    Cliente cliente;

    public AlquilerPelicula(LocalDateTime fechaInicio, LocalDateTime fechaEntrega, int id, Pelicula pelicula, Cliente cliente) {
        this.fechaInicio = fechaInicio;
        this.fechaEntrega = fechaEntrega;
        this.id = id;
        this.pelicula = pelicula;
        this.cliente = cliente;
    }

    public LocalDateTime getFechaInicio() {
        return fechaInicio;
    }

    public void setFechaInicio(LocalDateTime fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public LocalDateTime getFechaEntrega() {
        return fechaEntrega;
    }

    public void setFechaEntrega(LocalDateTime fechaEntrega) {
        this.fechaEntrega = fechaEntrega;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Pelicula getPelicula() {
        return pelicula;
    }

    public void setPelicula(Pelicula pelicula) {
        this.pelicula = pelicula;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    
    
}
