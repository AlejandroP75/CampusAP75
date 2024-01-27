public class marcador {
    private int juegosA;
    private int juegosB;
    
    public marcador(int juegosA, int juegosB) {
        this.juegosA = juegosA;
        this.juegosB = juegosB;
    }

    public int getJuegosA() {
        return juegosA;
    }

    public void setJuegosA(int juegosA) {
        this.juegosA = juegosA;
    }

    public int getJuegosB() {
        return juegosB;
    }

    public void setJuegosB(int juegosB) {
        this.juegosB = juegosB;
    }

    public String resultado(){
        String respuesta = "";
        if(((juegosA >= 7) && (juegosB >= 7)) || ((juegosA == 7) && (juegosB < 5)) || ((juegosB == 7) && (juegosA < 5)) || (juegosA < 0) || (juegosB < 0)){
            respuesta = "El partido es invalido";
        }else{
            if((juegosA >= 5) && (juegosB >= 5)){
                if(juegosA == 7){
                    respuesta = "Gano A";
                }else if(juegosB == 7){
                    respuesta = "Gano B";
                }else{
                    respuesta = "El partido continua";
                }
            }else{
                if((juegosA == 6) && (juegosB >= 4)){
                    respuesta = "Gano A";
                }else if((juegosB == 6) && (juegosA >= 4)){
                    respuesta = "Gano B";
                }else{
                    respuesta = "El partido continua";
                }
            }
        }
        return respuesta;
    }
}
