import java.util.Scanner;

public class PruebaAritmetica {

    public static void main(String[] args){
        
        int numeroA, numeroB;

        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese dos valores: ...");
        numeroA = entrada.nextInt();
        numeroB = entrada.nextInt();

        Aritmetica objeto1 = new Aritmetica(numeroA, numeroB);
        
        System.out.println(numeroA+"\n"+numeroB);

        
        System.out.println("El resultado de la suma es: \n" + objeto1.sumar());
        System.out.println("El resultado de la resta es : \n" + objeto1.restar());

    }
    
}
