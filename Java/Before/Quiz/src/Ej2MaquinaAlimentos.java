import java.util.Scanner;

public class Ej2MaquinaAlimentos {
    public static void main(String args[]) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Elija producto: ");
        String producto = leer.nextLine();

        switch (producto.toUpperCase()) {
            case "A":
                System.out.println("Ingrese monedas:");
                int moneda = 0, mon10 = 0, mon50 = 0, mon100 = 0, total = 0;
                while(true){
                    moneda = leer.nextInt();
                    if(moneda == 10){
                        mon10++;
                    }else if(moneda == 50){
                        mon50++;
                    }else if(moneda == 100){
                        mon100++;
                    }else{
                        System.out.println("Valor de la moneda invalido");
                    }
                    total = total + moneda;
                    if (total >= 270){
                        break;
                    }
                }
                mon10 = 0;
                mon50 = 0;
                mon100 = 0;
                int vueltas = total - 270;
                while (true) {
                    if(vueltas >= 100){
                        mon100++;
                        vueltas = vueltas - 100;
                    }else{
                        break;
                    }
                }
                while (true) {
                    if(vueltas >= 50){
                        mon50++;
                        vueltas = vueltas - 50;
                    }else{
                        break;
                    }
                }
                while (true) {
                    if(vueltas >= 10){
                        mon10++;
                        vueltas = vueltas - 10;
                    }else{
                        break;
                    }
                }
                System.out.println("Su vuelto:");
                if(mon100 != 0){
                    while(true){
                        System.out.println("100");
                        mon100--;
                        if(mon100 == 0){
                            break;
                        }
                    }
                }
                if(mon50 != 0){
                    while(true){
                        System.out.println("50");
                        mon50--;
                        if(mon50 == 0){
                            break;
                        }
                    }
                }
                if(mon10 != 0){
                    while(true){
                        System.out.println("10");
                        mon10--;
                        if(mon10 == 0){
                            break;
                        }
                    }
                }
                break;
            case "B":
                System.out.println("Ingrese monedas:");
                int monedab = 0, mon10b = 0, mon50b = 0, mon100b = 0, totalb = 0;
                while(true){
                    monedab = leer.nextInt();
                    if(monedab == 10){
                        mon10b++;
                    }else if(monedab == 50){
                        mon50b++;
                    }else if(monedab == 100){
                        mon100b++;
                    }else{
                        System.out.println("Valor de la moneda invalido");
                    }
                    totalb = totalb + monedab;
                    if (totalb >= 340){
                        break;
                    }
                }
                mon10b = 0;
                mon50b = 0;
                mon100b = 0;
                int vueltasb = totalb - 340;
                while (true) {
                    if(vueltasb >= 100){
                        mon100b++;
                        vueltasb = vueltasb - 100;
                    }else{
                        break;
                    }
                }
                while (true) {
                    if(vueltasb >= 50){
                        mon50b++;
                        vueltasb = vueltasb - 50;
                    }else{
                        break;
                    }
                }
                while (true) {
                    if(vueltasb >= 10){
                        mon10b++;
                        vueltasb = vueltasb - 10;
                    }else{
                        break;
                    }
                }
                System.out.println("Su vuelto:");
                if(mon100b != 0){
                    while(true){
                        System.out.println("100");
                        mon100b--;
                        if(mon100b == 0){
                            break;
                        }
                    }
                }
                if(mon50b != 0){
                    while(true){
                        System.out.println("50");
                        mon50b--;
                        if(mon50b == 0){
                            break;
                        }
                    }
                }
                if(mon10b != 0){
                    while(true){
                        System.out.println("10");
                        mon10b--;
                        if(mon10b == 0){
                            break;
                        }
                    }
                }
                break;
            case "C":
                System.out.println("Ingrese monedas:");
                int monedac = 0, mon10c = 0, mon50c = 0, mon100c = 0, totalc = 0;
                while(true){
                    monedac = leer.nextInt();
                    if(monedac == 10){
                        mon10c++;
                    }else if(monedac == 50){
                        mon50c++;
                    }else if(monedac == 100){
                        mon100c++;
                    }else{
                        System.out.println("Valor de la moneda invalido");
                    }
                    totalc = totalc + monedac;
                    if (totalc >= 390){
                        break;
                    }
                }
                mon10c = 0;
                mon50c = 0;
                mon100c = 0;
                int vueltasc = totalc - 390;
                while (true) {
                    if(vueltasc >= 100){
                        mon100c++;
                        vueltasc = vueltasc - 100;
                    }else{
                        break;
                    }
                }
                while (true) {
                    if(vueltasc >= 50){
                        mon50c++;
                        vueltasc = vueltasc - 50;
                    }else{
                        break;
                    }
                }
                while (true) {
                    if(vueltasc >= 10){
                        mon10c++;
                        vueltasc = vueltasc - 10;
                    }else{
                        break;
                    }
                }
                System.out.println("Su vuelto:");
                if(mon100c != 0){
                    while(true){
                        System.out.println("100");
                        mon100c--;
                        if(mon100c == 0){
                            break;
                        }
                    }
                }
                if(mon50c != 0){
                    while(true){
                        System.out.println("50");
                        mon50c--;
                        if(mon50c == 0){
                            break;
                        }
                    }
                }
                if(mon10c != 0){
                    while(true){
                        System.out.println("10");
                        mon10c--;
                        if(mon10c == 0){
                            break;
                        }
                    }
                }
                break;
            default:
                System.out.println("El prodcuto no existe");
                break;
        }
        System.out.println("Gracias por comprar");
        leer.close();
    }
}
