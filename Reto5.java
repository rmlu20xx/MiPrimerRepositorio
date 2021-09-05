package reto.pkg2;

import java.time.LocalDate;
import java.util.Scanner;

public class Reto5 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);  
            String Placa;
            int DiasDesdeUltimoMantenimiento;
            boolean TieneSeguro;
            String Cedula;
            int Edad;
            String Nombre;
            String Fecha;
            int HorasAlquiler;
            boolean aplicaDescuento;
            
//****************************************************************************************************************************
//****************************************************************************************************************************
      Cliente cliente1 = new Cliente("1015143634",23,"Juan");
      Cliente cliente2 = new Cliente("1364726437",33,"Mateo");
      Cliente cliente3 = new Cliente("9685432432",43,"Ana");
      Cliente cliente4 = new Cliente("1015143634",23,"Juan");
      Cliente cliente5 = new Cliente("4567987652",50,"Alfredo");
      Cliente cliente6 = new Cliente("5468978655",58,"Gloria");
      Cliente cliente7 = new Cliente("1015143634",23,"Juan");
      
      Alquiler historial0 = new Alquiler(cliente1);
      Alquiler historial1 = new Alquiler(cliente2);
      Alquiler historial2 = new Alquiler(cliente3);
      Alquiler historial3 = new Alquiler(cliente4);
      Alquiler historial4 = new Alquiler(cliente5);
      Alquiler historial5 = new Alquiler(cliente6);
      Alquiler historial6 = new Alquiler(cliente7);
      
      Alquiler[] historial_1 = new Alquiler[7];
      
      historial_1[0]=historial0;
      historial_1[1]=historial1;
      historial_1[2]=historial2;
      historial_1[3]=historial3;
      historial_1[4]=historial4;
      historial_1[5]=historial5;
      historial_1[6]=historial6;
      
//****************************************************************************************************************************
//****************************************************************************************************************************

      Cliente cliente8 = new Cliente("9078968512",58,"Camila");
      Cliente cliente9 = new Cliente("1364726437",33,"Mateo");
      Cliente cliente10 = new Cliente("9685432432",43,"Ana");
      Cliente cliente11 = new Cliente("847534654",38,"Liliana");
      Cliente cliente12 = new Cliente("4567987652",50,"Alfredo");
      Cliente cliente13 = new Cliente("5468978655",58,"Gloria");
      Cliente cliente14 = new Cliente("0896756443",23,"Mario");
      
      Alquiler historial7 = new Alquiler(cliente8);
      Alquiler historial8 = new Alquiler(cliente9);
      Alquiler historial9 = new Alquiler(cliente10);
      Alquiler historial10 = new Alquiler(cliente11);
      Alquiler historial11 = new Alquiler(cliente12);
      Alquiler historial12 = new Alquiler(cliente13);
      Alquiler historial13 = new Alquiler(cliente14);
      
      Alquiler[] historial_2 = new Alquiler[7];
      
      historial_2[0]=historial7;
      historial_2[1]=historial8;
      historial_2[2]=historial9;
      historial_2[3]=historial10;
      historial_2[4]=historial11;
      historial_2[5]=historial12;
      historial_2[6]=historial13;

//****************************************************************************************************************************
//****************************************************************************************************************************
      
      Auto auto1 = new Auto("DST196",2,true);
            
      Alquiler alquiler0 = new Alquiler(cliente1, auto1, LocalDate.parse("2021-06-12"),48);
      Alquiler alquiler1 = new Alquiler(cliente2, auto1, LocalDate.parse("2021-07-12"),30);
      Alquiler alquiler2 = new Alquiler(cliente1, auto1, LocalDate.parse("2021-07-14"),25);
      Alquiler alquiler3 = new Alquiler(cliente3, auto1, LocalDate.parse("2021-07-14"),12);
      Alquiler alquiler4 = new Alquiler(cliente1, auto1, LocalDate.parse("2021-07-16"),8);
      
      Alquiler[] alquileres = new Alquiler[5];
      
      alquileres[0]=alquiler0;
      alquileres[1]=alquiler1;
      alquileres[2]=alquiler2;
      alquileres[3]=alquiler3;
      alquileres[4]=alquiler4;
      
//****************************************************************************************************************************
//****************************************************************************************************************************      
      System.out.print("Digite la Cedula del cliente = ");
      Cedula = entrada.nextLine();
      System.out.print("Digite la Edad del cliente = ");
      Edad = entrada.nextInt();
      System.out.print("Digite el Nombre del cliente = ");
      entrada.nextLine();
      Nombre = entrada.nextLine();
      
      System.out.print("Digite el Número de la Placa del Vehiculo = ");
      Placa = entrada.nextLine();
      System.out.print("Digite los dias que lleva desde el último mantenimiento = ");
      DiasDesdeUltimoMantenimiento = entrada.nextInt();
      System.out.print("Indique si el Vehiculo tiene seguro o no = ");
      TieneSeguro = entrada.nextBoolean();
      System.out.print("Indique la Fecha (Año-Mes-Dia) del Alquiler = ");
      Fecha = entrada.next();
      System.out.print("Indique la cantidad de horas de alquiler = ");
      HorasAlquiler=entrada.nextInt();
      System.out.print("Indique si tiene (true) o no (false) descueento = ");
      aplicaDescuento = entrada.nextBoolean();
      
     
      
      Cliente cliente = new Cliente(Cedula,Edad,Nombre);
      Auto Vehiculo = new Auto(Placa,DiasDesdeUltimoMantenimiento,TieneSeguro);
      Alquiler alquiler = new Alquiler(cliente, Vehiculo, LocalDate.parse(Fecha),HorasAlquiler);
      Alquiler historial = new Alquiler(cliente);
      
      System.out.println("El vehiculo de placas "+Vehiculo.getPlaca());
      System.out.println("Requiere mantenimiento ? = "+Vehiculo.NecesitaMantenimiento());     
      System.out.println("Se puede rentar ? = "+Vehiculo.SePuedeRentar());
      System.out.println("Nombre del Cliente = "+cliente.getNombre());
      System.out.println("La edad de Cliente = "+cliente.getEdad());
      System.out.println("la cedula del Cliente = "+cliente.getCedula());
      
      System.out.println("El valor de descuento es = "+alquiler.ObtenerDescuento(alquileres));
      System.out.println("El costo del alquiler es = "+alquiler.CalcularCosto(aplicaDescuento));
      
      System.out.println("Se le puede alquilar al Cliente = "+historial.PuedeAlquilar(historial_1,cliente));
      System.out.println("Se le puede alquilar al Cliente = "+historial.PuedeAlquilar(historial_2,cliente));
      
      /*
      if  (alquiler.ObtenerDescuento(alquileres)==2||alquiler.ObtenerDescuento(alquileres)==5){
            aplicaDescuento = true;
            System.out.println("El costo total con descuento es = "+alquiler.CalcularCosto(aplicaDescuento));
          }else{
            aplicaDescuento = false;      
            System.out.println("El costo total sin descuento es = "+alquiler.CalcularCosto(aplicaDescuento));
            }
    */
    
    }
    
}
