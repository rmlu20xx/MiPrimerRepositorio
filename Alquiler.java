package reto.pkg2;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Alquiler {
    private Cliente Cliente;
    private Auto Auto;
    private LocalDate Fecha;
    private int HorasAlquiler;

    public Alquiler(Cliente cliente) {
       Cliente = cliente; 
    }
    
    public Alquiler(Cliente cliente, Auto auto, LocalDate fecha, int horasAlquiler) {
        Cliente = cliente;
        Auto = auto;
        Fecha = fecha;
        HorasAlquiler = horasAlquiler;
    }

    public Cliente getCliente() {
        return Cliente;
    }

    public Auto getAuto() {
        return Auto;
    }

    public LocalDate getFecha() {
        return Fecha;
    }

    public int getHorasAlquiler() {
        return HorasAlquiler;
    }
    
    public int ObtenerDescuento(Alquiler[] alquileres){
        if ((Auto.NecesitaMantenimiento()!=true)&(Auto.SePuedeRentar()==true)){
           for (int i=0;i<alquileres.length;i++){
               //System.out.println("Entró a For ");
               if (((alquileres[i].getCliente().getNombre().equals(Cliente.getNombre())))&(alquileres[i].getCliente().getCedula().equals(Cliente.getCedula()))){
                   //System.out.println("Entró al If_1 ");
                   long restaDiasAlquiler = ChronoUnit.DAYS.between(alquileres[i].getFecha(), getFecha());
                   //System.out.println("resta = "+restaDiasAlquiler);
                if (restaDiasAlquiler<=30){
                   int horasAlquiler = alquileres[i].getHorasAlquiler()+getHorasAlquiler();
                   if (horasAlquiler<20){
                       return 0;
                   }else if(horasAlquiler>=20 & horasAlquiler<50){
                       return 2;
                   }
                       
                    return 5; 
                }
                      
               }
               
           }
            
           return 0;
        }
        
        return 0;
    }
    
    public double CalcularCosto(boolean aplicaDescuento){
        if (aplicaDescuento==true){
            double calcularCosto=(getHorasAlquiler()*5000)*0.98;
            return  calcularCosto;
        }
        double calcularCosto=(getHorasAlquiler()*5000);
        return calcularCosto;
    }
    
    public static boolean PuedeAlquilar(Alquiler[] historial, Cliente cliente){
        int contador = 0;
        for (int i=0;i<historial.length;i++){
               //System.out.println("Entró a For ");
               if (((historial[i].getCliente().getNombre().equals(cliente.getNombre())))&(historial[i].getCliente().getCedula().equals(cliente.getCedula()))){
                   //System.out.println("Entró al If_1 ");
                   contador =contador+1;
                   //System.out.println("resta = "+restaDiasAlquiler);
                    }
                }
                               
                if (contador >=3){
                   return false;
                   }return true;
                }
                       
                    
               
}
        
    

