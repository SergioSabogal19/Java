import java.util.Scanner;

public class caja {
    public static void main(String[] args){


        Scanner entrada = new Scanner(System.in);

        int base, altura, profundidad;

        System.out.println(" ************BIENVENIDO*********** ");
        System.out.println("Ingresa la altura: ");
        altura = entrada.nextInt();
        System.out.println("Ingresa la profundidad: ");
        profundidad = entrada.nextInt();
        System.out.println("Ingresa la base: ");
        base = entrada.nextInt();


        Volumen objeto1 = new Volumen(altura, profundidad, base);
        System.out.println("El volumen calculado para  tus valores es:  " + objeto1.calcularVolumen());




    }
    
}
                         