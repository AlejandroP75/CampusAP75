public class Pelicula {
    private int id;
    private String titulo;
    private String director;
    private String genero;
    private float precio;
    private int descuento;
    
    public Pelicula(int id, String titulo, String director, String genero, float precio, int descuento) {
        this.id = id;
        this.titulo = titulo;
        this.director = director;
        this.genero = genero;
        this.precio = precio;
        this.descuento = descuento;
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

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public float getPrecio() {
        return precio;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }

    public int getDescuento() {
        return descuento;
    }

    public void setDescuento(int descuento) {
        this.descuento = descuento;
    }

    public void mostrarPelicula(){
        System.out.print("\nId: " + this.id);
        System.out.print("\nTitulo: " + this.titulo);
        System.out.print("\nDirector: " + this.director);
        System.out.print("\nGenero: " + this.genero);
        System.out.print("\nPrecio: " + this.precio);
        System.out.print("\nDescuento: " + this.descuento);
    }
}
