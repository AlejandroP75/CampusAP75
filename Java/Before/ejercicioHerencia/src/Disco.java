public class Disco extends Publicacion{
    private float duracion;

    public Disco(String titulo, float precio, float duracion) {
        super(titulo, precio);
        this.duracion = duracion;
    }

    @Override
    public void mostratInfo() {
        System.out.println("-DISCO-");
        System.out.println("Titulo: " + super.getTitulo());
        System.out.println("Precio: " + super.getPrecio());
        System.out.println("Duración: " + duracion);
    }
    
}
