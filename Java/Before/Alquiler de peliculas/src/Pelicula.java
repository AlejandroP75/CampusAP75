public class Pelicula {
    private int id;
    private String titulo;
    private String genero;
    private double precio_alquiler;
    private String director;
    private double descuento;

    public Pelicula(int id, String titulo, String genero, double precio_alquiler, String director, double descuento) {
        this.id = id;
        this.titulo = titulo;
        this.genero = genero;
        this.precio_alquiler = precio_alquiler;
        this.director = director;
        this.descuento = descuento;
    }

    double calcularPrecioConDescuento(){
        double new_prec = this.precio_alquiler - (this.precio_alquiler * (descuento / 100));
        return new_prec;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public double getPrecio_alquiler() {
        return precio_alquiler;
    }

    public void setPrecio_alquiler(double precio_alquiler) {
        this.precio_alquiler = precio_alquiler;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public double getDescuento() {
        return descuento;
    }

    public void setDescuento(double descuento) {
        this.descuento = descuento;
    }

}
