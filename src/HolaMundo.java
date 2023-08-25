public class HolaMundo {
    public static void main(String []args){

        // Funcionamiento de break

      /*  for(var i = 0; i<3; i++){
            // Imprimimos solo los numeros pares
            if(i % 2 == 0){
                System.out.println("i : "+ i);
                break;  // Rompe la ejecución de todo el ciclo for
            }
        }
      */

        // Uso y funcionamiento de Continue
        for(var i = 0; i<3; i++){
            // Imprimimos solo los numeros pares
            if(i % 2 != 0){
                continue; // Continue ejecutando la siguiente iteración del ciclo for
            }
            System.out.println("i : "+ i);
        }

        /*
        * Uso de etiquetas
        * --> Se emplea el uso de etiquetas para indicar un salto a una parte especifica del programa
        * Aunque no es recomendable su uso..
        * inicio:
        * for (var i = o ; i<10 ; i++){
        *   if (i % 2 !=0) {
        *       break inicio;
        *   }
        * }
        * */
    }
}
