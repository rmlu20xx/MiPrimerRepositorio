package reto.pkg2;

public class Cliente {
    private String Cedula;
    private int Edad;
    private String Nombre;

    public Cliente(String cedula, int edad, String nombre) {
        Cedula = cedula;
        Edad = edad;
        Nombre = nombre;
    }

    public String getCedula() {
        return Cedula;
    }

    public int getEdad() {
        return Edad;
    }

    public String getNombre() {
        return Nombre;
    }
    
    
    
}
