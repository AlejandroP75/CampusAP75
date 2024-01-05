import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {

        Random random = new Random();

        Carro car1 = new Carro("Azul", "UIO878", 890, "Suzuki", true, 0);
        Carro car2 = new Carro("Rojo", "UIO878", 890, "Suzuki", true, 0);
        Carro car3 = new Carro("Verde", "UIO878", 890, "Suzuki", true, 0);

        for (int i = 0; i < 5; i++) {
            car1.acelerar(random.nextInt(50)+1);
            car2.acelerar(random.nextInt(50)+1);
            car3.acelerar(random.nextInt(50)+1);
        }
        car1.setVelocidad(-9);
        System.out.println(car1.getVelocidad());
        System.out.println(car2.getVelocidad());
        System.out.println(car3.getVelocidad());

        System.out.println(car1);
    }
}
