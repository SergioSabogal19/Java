public class Volumen {

    int base;
    int altura;
    int profundidad;

    public Volumen(){
        System.out.println("Constructor vacio");
    }

    public Volumen(int base, int altura, int profundidad) {

        this.base = base;
        this.altura = altura;
        this.profundidad = profundidad;
        System.out.println("Ejecutando constructor lleno....");
    }

    public int calcularVolumen() {
        return base * altura * profundidad;
    }
    
}
