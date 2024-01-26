public class Gobernador {
    private String nombre;
    private int telefono;
    private String email;
    private String partidoPolitico;
    
    public Gobernador(String nombre, int telefono, String email, String partidoPolitico) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.email = email;
        this.partidoPolitico = partidoPolitico;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPartidoPolitico() {
        return partidoPolitico;
    }

    public void setPartidoPolitico(String partidoPolitico) {
        this.partidoPolitico = partidoPolitico;
    }

    
}
