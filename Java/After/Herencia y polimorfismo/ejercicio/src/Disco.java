public class Disco extends Publicaciones{
    private int duracionMinu;

    public Disco(String titulo, float precio, int duracionMinu) {
        super(titulo, precio);
        this.duracionMinu = duracionMinu;
    }

    public int getDuracionMinu() {
        return duracionMinu;
    }

    public void setDuracionMinu(int duracionMinu) {
        this.duracionMinu = duracionMinu;
    }

    @Override
    public void mostrar() {
        System.out.print("Disco");
        System.out.print("\n\nTitulo: " + super.getTitulo());
        System.out.print("\nPrecio: " + super.getPrecio());
        System.out.print("\nDuración en minutos: " + this.duracionMinu);
    }
}
