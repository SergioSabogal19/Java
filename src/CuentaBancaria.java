import java.util.Scanner;

public class CuentaBancaria {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        String nombreTitular = "Sergio Sabogal";
        Transaccion transaccion = new Transaccion();
        transaccion.nuevoSaldo(1160900);


        char option = menuPrincipal(entrada);
        if (option == 'a'){
            System.out.println("¿ Cuanto desea retirar ?");
            int retiro = entrada.nextInt();

            transaccion.retirarSaldo(retiro, transaccion.obtenerSaldo());
        }

    }

    private static char menuPrincipal(Scanner entrada){
        System.out.println("BIENVENIDO QUE DESEAS HACE: \n\n a.)Retiro\n\n b).Consignación");
        char entradaMenu = entrada.nextLine().charAt(0);
        return entradaMenu;
    }
    
}
