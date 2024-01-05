import java.util.Scanner;

public class Humano {

    public String nombre;
    public String apellido;
    public String sexo;
    public int edad;
    public long id;

    public Humano(){

    }
    
    public Humano(String nombre, String apellido,String sexo, int edad, long id){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.id = id;
        this.sexo = sexo;
    }

    public void saludar(){
        Scanner leer = new Scanner(System.in);
        System.out.println("Hola gay " + this.nombre);
        System.out.println("¿Quieres ver tus atributos?");
        String r = leer.next();
        if (r.equals("si")) {
            this.mostrar();
        }else{
            System.out.println("Chao mmpinga");
        }
        leer.close();
    }
    
    public void mostrar(){
        System.out.println("Nombre: ");
        System.out.println("Apellido: ");
        System.out.println("Sexo: ");
        System.out.println("Edad: ");
        System.out.println("ID: ");
    }
}
