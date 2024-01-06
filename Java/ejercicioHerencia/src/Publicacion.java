public class Publicacion {
    private String titulo;
    private float precio;
    
    public Publicacion(String titulo, float precio) {
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

    public void mostratInfo(){
        System.out.println("-PUBLICACIÓN-");
        System.out.println("Titulo: " + titulo);
        System.out.println("Precio: " + precio);
    }
}
