public class Transaccion {

    int saldo;

    public void nuevoSaldo(int saldo){
        this.saldo = saldo;
    }

    public int obtenerSaldo(){
        return this.saldo;
    }

    public void consignarSaldo(int consignacion, int saldo){
        this.saldo = saldo + consignacion;
    }

    public void retirarSaldo(int consignacion, int saldo){
        this.saldo = saldo - consignacion;
        System.out.println("Retiro por:  $" + consignacion);
        System.out.println("Saldo actual :  $" + this.saldo);
    }

    
}
