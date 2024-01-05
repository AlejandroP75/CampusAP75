import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {

        Random random = new Random();

        Carro car = new Carro("Azul", "UIO878", 890, "Suzuki", true, 0);
        Carro car1 = new Carro("Rojo", "UIO878", 890, "Suzuki", true, 0);
        Carro car2 = new Carro("Verde", "UIO878", 890, "Suzuki", true, 0);

        for (int i = 0; i < 5; i++) {
            car.acelerar(random.nextInt(50)+1);
            car2.acelerar(random.nextInt(50)+1);
            car1.acelerar(random.nextInt(50)+1);
        }

        System.out.println(car.velocidad);
        System.out.println(car1.velocidad);
        System.out.println(car2.velocidad);

        System.out.println(car);
    }
}
