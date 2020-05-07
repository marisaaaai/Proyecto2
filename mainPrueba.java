/*Programa de prueba sobre esquema de sistema de recomendacion
* Grupo:
* Maria Morales 19145
* Luis Garcia 19344
* Maria Montoya 19169
* Universidad del Valle de Guatemala*/
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.util.*; 

public class mainPrueba{
	public static void main(String[]args){
		Scanner scan = new Scanner(System.in);
		ArrayList<String> nombre = new ArrayList<String>();
		ArrayList<String> link = new ArrayList<String>();
		ArrayList<String> datos = new ArrayList<String>();
		//Se muestra mensaje de bienvenida
		System.out.println("Bienvenido a nuestra sistema de recomencione \nUsted ha ingresado aqui porque quiere alguna recomendacion sobre canales de YouTube");
		System.out.println("A continuacion se le harán una serie de preguntas para que podamos recomendarlo algo de su gusto");
		System.out.println("\nUsted preferiria que los videos del canal duraran.... \n1.<15 min\n2.15 min promedio \n3.30 min promedio\n4. 45min promedio \n5.1 hora promedio \n6. >1 hora \nPor favor ingrese el numero de su eleccion: ");
		int duracionEscogida = scan.nextInt();
		System.out.println("\nDesea que el canal tenga videos de ejercicios… \n1.Activo (vídeos donde se estará moviendo con mucha frecuencia, donde tendrá una actividad cardiaca alta) \n2. Pasivos (Tipo de ejercicios en donde no se habrá de mover demasiado seguido)\nPor favor ingrese el numero de la opcion escogida: ");
		int dinamismoEscogido = scan.nextInt();
		System.out.println("\nDesea que el tipo de ejercicio sea… \n1. Yoga \n2. Crossfit \n3. Tai Chi \n4. Calistenia \n5. Pilates \n6. Cardio \n7. Body Building \n8. Zumba \nPor favor ingrese el numero de la opcion escogida: ");
		int ejercicioEscogido = scan.nextInt();
		System.out.println("\nDesea que el canal tenga clases en vivo… (si se le es indiferente por favor seleccionar 1) \n1. No  \n2. Si\nPor favor Ingrese su opcion escogida: ");
		int liveEscogido = scan.nextInt();
		Scanner s = null;
		String archive = "baseDatos.txt";
		File fichero = new File(archive);
		String linea="";
		try{
			s = new Scanner(fichero);
            while(s.hasNextLine()){
                linea = s.nextLine();
                String data[] = linea.split(",");//se separa la informacion por las comas que tiene el string
                nombre.add(data[0]);
				link.add(data[1]);
				datos.add(data[2]);
				datos.add(data[3]);
				datos.add(data[4]);
				datos.add(data[5]);
            }
		}
        // se toman en cuenta las excepciones si no se encuentra el archivo
		catch(Exception ex){
            System.out.println("Se tuvo el siguiente error: "+ex.getMessage());
		}
		finally{
			try{
				if(s!=null){
					s.close();
				}
			}
			catch(Exception ex2){
				System.out.println("Se tuvo el error: "+ ex2.getMessage());
			}
		}
		int po=0;
		int p=0;
		boolean w=true;
		int d=0;
		int di=0;
		int e=0;
		int l=0;
		int largo=nombre.size();
		while(w!=false){
			if(datos.get(p).equals("<15min")){
				d=1;
			}
			else{
				if(datos.get(p).equals("15min promedio")){
					d=2;
				}
				else{
					if(datos.get(p).equals("30min promedio")){
						d=3;
					}
					else{
						if(datos.get(p).equals("45min promedio")){
							d=4;
						}
						else{
							if(datos.get(p).equals("1 hora promedio")){
								d=5;
							}
							else{
								d=6;
							}
						}
					}
				}
			}
			if(datos.get(p+1).equals("Activo")){
				di=1;
			}
			else{
				di=2;
			}
			if(datos.get(p+2).equals("Yoga")){
				e=1;
			}
			else{
				if(datos.get(p+2).equals("Crossfit")){
					e=2;
				}
				else{
					if(datos.get(p+2).equals("Tai Chi")){
						e=3;
					}
					else{
						if(datos.get(p+2).equals("Calistenia")){
							e=4;
						}
						else{
							if(datos.get(p+2).equals("Pilates")){
								e=5;
							}
							else{
								if(datos.get(p+2).equals("Cardio")){
									e=6;
								}
								else{
									if(datos.get(p+2).equals("Body Building")){
										e=7;
									}
									else{
										e=8;
									}
								}
							}
						}
					}
				}
			}
			if(datos.get(p+3).equals("Pre grabadas")){
				l=1;
			}
			else{
				l=2;
			}
			int[] cualidades = {d,di,e,l};
			if((cualidades[0]==duracionEscogida) && (cualidades[1]==dinamismoEscogido) && (cualidades[2]==ejercicioEscogido) && (cualidades[3]==liveEscogido)){
				w=false;
				System.out.println("Se le recomienda el canal: "+nombre.get(po) + "\nCon link: " +link.get(po));
				System.out.println("Gracias por usar nuestro sistema de recomendacion");
			}
			else{
				p=p+4;
				po=po+1;
			}
			if(po==largo){
				System.out.println("No se ha encontrado un canal con sus cualidades");
				System.out.println("Lo lamentamos, pero gracias por ingresar a nuestro sistema de recomendacion");
				w=false;
			}
		}
	}
}