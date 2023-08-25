public class pasoPorReferencia {

    public static void main(String[] args) {
        
        Persona persona = new Persona();
        persona.cambiarNombre("Sergio Danilo");

        System.out.println("Nuevo nombre ingresado:   " + persona.obtenerNombre());

        modificarPersona(persona);
        System.out.println("Nuevo nombre: " + persona.obtenerNombre());

    }

    private static void modificarPersona(Persona personaArg){
        personaArg.cambiarNombre("Sabogal Quintin");
    }
    
}
