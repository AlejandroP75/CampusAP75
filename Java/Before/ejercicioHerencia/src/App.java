public class App {
    public static void main(String[] args) {
        Publicacion prueba = new Publicacion("This is a test", 100);
        Publicacion prueba2 = new Libro(200, 2022, "La oscuridad", 20000);
        Publicacion prueba3 = new Disco("Josean Log", 15, 20);

        prueba.mostratInfo();
        prueba2.mostratInfo();
        prueba3.mostratInfo();
    }
}
