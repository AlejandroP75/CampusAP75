public class Municipio {
    private String nombre;
    private int poblacion;
    private float area;
    
    public Municipio(String nombre, int poblacion, float area) {
        this.nombre = nombre;
        this.poblacion = poblacion;
        this.area = area;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getPoblacion() {
        return poblacion;
    }

    public void setPoblacion(int poblacion) {
        this.poblacion = poblacion;
    }

    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }

    
}
