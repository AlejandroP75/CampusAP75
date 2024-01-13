public class Departamento {
    private String nombre;
    private Municipio[] municipios;
    private Gobernador gobernador;
    
    public Departamento(String nombre, Municipio[] municipios, Gobernador gobernador) {
        this.nombre = nombre;
        this.municipios = municipios;
        this.gobernador = gobernador;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Municipio[] getMunicipios() {
        return municipios;
    }

    public void setMunicipios(Municipio[] municipios) {
        this.municipios = municipios;
    }

    public Gobernador getGobernador() {
        return gobernador;
    }

    public void setGobernador(Gobernador gobernador) {
        this.gobernador = gobernador;
    }

}
