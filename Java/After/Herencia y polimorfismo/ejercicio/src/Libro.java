public class Libro extends Publicaciones{
    private int numeroPag;
    private int añoPubli;
    
    public Libro(String titulo, float precio, int numeroPag, int añoPubli) {
        super(titulo, precio);
        this.numeroPag = numeroPag;
        this.añoPubli = añoPubli;
    }

    public int getNumeroPag() {
        return numeroPag;
    }

    public void setNumeroPag(int numeroPag) {
        this.numeroPag = numeroPag;
    }

    public int getAñoPubli() {
        return añoPubli;
    }

    public void setAñoPubli(int añoPubli) {
        this.añoPubli = añoPubli;
    }

    @Override
    public void mostrar() {
        System.out.print("LIBRO");
        System.out.print("\n\nTitulo: " + super.getTitulo());
        System.out.print("\nPrecio: " + super.getPrecio());
        System.out.print("\nNumero de paginas: " + this.numeroPag);
        System.out.print("\nAño de publicación: " + this.añoPubli);
    }
}
