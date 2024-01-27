public class Publicaciones {
    private String titulo;
    private float precio;
    
    public Publicaciones(String titulo, float precio) {
        this.titulo = titulo;
        this.precio = precio;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public float getPrecio() {
        return precio;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }

    public void mostrar(){
        System.out.print("PUBLICACIÓN");
        System.out.print("\n\nTitulo: " + this.titulo);
        System.out.print("\nPrecio: " + this.precio);
    }
}
