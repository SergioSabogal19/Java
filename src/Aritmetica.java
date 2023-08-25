public class Aritmetica {

    // Atributos de la clase
    int a;
    int b;

    public Aritmetica() {
        System.out.println("Ejecutando constructor vacio");
    }

    public Aritmetica(int arg1, int arg2) {
        a = arg1;
        b = arg2;
        System.out.println("Ejecutando constructor con dos argumentos...");
    }


    public int sumar() {
        // int resultado = a+b;
        // return resultado;
        return a+b;
    }

    public int restar() {
        return a - b;

    }

    
}
