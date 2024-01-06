public class Libro extends Publicacion {
    
    private int num_pag;
    private int annio_pub;

    public Libro(int num_pag, int annio_pub, String titulo, float precio){
        super(titulo, precio);
        this.annio_pub = annio_pub;
        this.num_pag = num_pag;
    }

    @Override
    public void mostratInfo() {
        System.out.println("-LIBRO-");
        System.out.println("Titulo: " + super.getTitulo());
        System.out.println("Precio: " + super.getPrecio());
        System.out.println("Año publicación: " + annio_pub);
        System.out.println("Numero de paginas: " + num_pag);
    }
}
