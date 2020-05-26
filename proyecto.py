from py2neo import Graph
graph = Graph("http://neo4j:holagrupo@127.0.0.1:7474/db/data")
#se guardan todos los nombres de los canales en una lista
names=graph.run("MATCH (a:canal) RETURN a.name").data()
#hello=graph.run("MATCH (:canal { name: 'Blogilates' })--(d:duracion) RETURN d.name").data()
#print(hello)
tamaño=len(names) #Se guarda el tamaño de la lista
nombres=[]#Se guarda en una lista solamente como nombres y no como diccionario
cualidades=[]
w=0
d=0
di=0
e=0
t=0
s=0
duracionElegida=0
while(w<tamaño):
    diccionario=names.pop()
    nombre1=diccionario.get('a.name')
    nombres.append(nombre1)
    w=w+1
names=graph.run("MATCH (a:canal) RETURN a.name").data()
op=input("Bienvenido a nuestro programa \n\nQuieres....\n1.Ir al sistema de recomendacion \n2.Alterar base de datos\n\nIngresa el numero de tu opcion: ")
if (op=="1"):
    print("\n***********************************************************************************\nSe te mostrara una serie de preguntas con sus opciones numeradas, por favor ingresa el numero de la opcion que te gustaria escoger")
    duracionElegida=input("\n***********************************************************************************\nDe las duraciones que usted preferiria que dure los videos del canal de Youtube en promedio, Cual preferiria...\n1. menos de 15min \n2. 15 min promedio \n3. 30 min promedio \n4. 45 min promedio \n5. 1 hora promedio \n6. mas de 1 hora\n\nIngresa el numero de tu opcion: ")
    dinamicidadElegida=input("\n***********************************************************************************\nDesea que el canal tenga videos de ejercicios… \n1.Activo (vídeos donde se estará moviendo con mucha frecuencia, donde tendrá una actividad cardiaca alta) \n2. Pasivos (Tipo de ejercicios en donde no se habrá de mover demasiado seguido \n\nIngresa el numero de tu opcion: ")
    ejercicioEscogido=input("\n***********************************************************************************\nDesea que el tipo de ejercicio sea… \n1. Yoga \n2. Crossfit \n3. Tai Chi \n4. Calistenia \n5. Pilates \n6. Cardio \n7. Body Building \n8. Zumba\n9.Aerobicos\n\nIngresa el numero de tu opcion: ")
    liveEscogido=input("\n***********************************************************************************\nDesea que el canal tenga clases en vivo… (si se le es indiferente por favor seleccionar 2) \n1. Si  \n2. No\n\nIngresa el numero de tu opcion: ")
    p=0
    po=0
    suma=0
    while p<1:
        nombre=nombres.pop()
        listaDuracion=graph.run("MATCH (:canal { name: '"+nombre+"' })--(d:duracion) RETURN d.name").data()
        dicDuracion=listaDuracion.pop()
        duracion=dicDuracion.get('d.name')
        
        listaDinamicidad=graph.run("MATCH (:canal { name: '"+nombre+"' })--(di:dinamicidad) RETURN di.name").data()
        dicDinamicidad=listaDinamicidad.pop()
        dinamicidad=dicDinamicidad.get('di.name')
        
        listaEjercicios=graph.run("MATCH (:canal { name: '"+nombre+"' })--(e:ejercicio) RETURN e.name").data()
        dicEjercicios=listaEjercicios.pop()
        ejercicio=dicEjercicios.get('e.name')
        
        listaTipo=graph.run("MATCH (:canal { name: '"+nombre+"' })--(t:video) RETURN t.name").data()
        dicTipo=listaTipo.pop()
        tipo=dicTipo.get('t.name')
        
        listaLink=graph.run("MATCH (a:canal) WHERE a.name='"+nombre+"' RETURN a.link").data()
        dicLink=listaLink.pop()
        
        if(duracion=="menos 15 min"):
            d="1"
        else:
            if(duracion=="15 min promedio"):
                d="2"
            else:
                if(duracion=="30 min promedio"):
                    d="3"
                else:
                    if(duracion=="45 min promedio"):
                        d="4"
                    else:
                        if(duracion=="1 hora promedio"):
                            d="5"
                        else:
                            d="6"
        if(dinamicidad=="Activo"):
            di="1"
        else:
            di="2"
        if(ejercicio=="Yoga"):
            e="1"
        else:
            if(ejercicio=="Crossfit"):
                e="2"
            else:
                if(ejercicio=="Tai Chi"):
                    e="3"
                else:
                    if(ejercicio=="Calistenia"):
                        e="4"
                    else:
                        if(ejercicio=="Pilates"):
                            e="5"
                        else:
                            if(ejercicio=="Cardio"):
                                e="6"
                            else:
                                if(ejercicio=="Body Building"):
                                    e="7"
                                else:
                                    if(ejercicio=="Zumba"):
                                        e="8"
                                    else:
                                        e="9"
        
        if(tipo=="Pre Grabadas"):
            t="2"
        else:
            t="1"
        if((duracionElegida==d)and(dinamicidadElegida==di)and(ejercicioEscogido==e)and(liveEscogido==t)):
            print("\n*************************************************************************\nHemos encontrado un canal para ti!")
            print("Te recomendamos el canal: "+nombre)
            print("Con link: ")
            print(dicLink)
            p+=1
        else:
            po+=1
        if(po==tamaño):
            print("\n**************************************************************************\nLo sentimos pero no encontramos un canal de YouTube que recomendarte, pero te invitamos que agregues a nuestra base de datos si quisieras\n")
            p+=1
        else:
            p=p
    print("\n****************************************************************************\nGracias por usar nuestro sistema de recomendacion\n")
else:
    if(op=="2"):
        op2=input("\n***********************************************************************************\n\nGracias por ayudarnos con nuestro sistema de recomendacion\nDeseas...\n1.Agregar a la base de datos \n2.Eliminar de la base de datos\n\nIngresa el numero de tu opción:")
        if(op2=="1"):
            print("Muy Bien! Te haremos preguntas respecto al canal de YouTube que quieres agregar y nosotros lo agregaremos a la base de datos")
            nombreCanal=input("\n***********************************************************************************\nComo se llama tu canal?\n")
            linkCanal=input("\n***********************************************************************************\nIngrese el link del canal que desea agregar")
            duracionCanalProvisional=input("\n***********************************************************************************\nCuanto duran, en promedio,los videos de su canal?...\n1. menos de 15min \n2. 15 min promedio \n3. 30 min promedio \n4. 45 min promedio \n5. 1 hora promedio \n6. mas de 1 hora\n\nIngresa el numero de tu opcion: ")
            dinamismoCanalProvisional=input("\n***********************************************************************************\nSu canal tiene videos de ejercicios… \n1.Activos (vídeos donde se estará moviendo con mucha frecuencia, donde tendrá una actividad cardiaca alta) \n2. Pasivos (Tipo de ejercicios en donde no se habrá de mover demasiado seguido \n\nIngresa el numero de tu opcion: ")
            ejercicioCanalProvisional=input("\n***********************************************************************************\nEn que tipo de ejercicio encaja su canal… \n1. Yoga \n2. Crossfit \n3. Tai Chi \n4. Calistenia \n5. Pilates \n6. Cardio \n7. Body Building \n8. Zumba\n9.Aerobicos\n\nIngresa el numero de tu opcion: ")
            tipoCanalProvisional=input("\n***********************************************************************************\nSu canal tiene clases en vivo? \n1. Si  \n2. No\n\nIngresa el numero de tu opcion: ")
            crearNodo= "CREATE (a:canal{name:'"+nombreCanal+"',link:'"+linkCanal+"'})"
            graph.run(crearNodo).data()
            if(duracionCanalProvisional=="1"):
                duracionCanal="menos 15 min"
            else:
                if(duracionCanalProvisional=="2"):
                    duracionCanal="15 min promedio"
                else:
                    if(duracionCanalProvisional=="3"):
                        duracionCanal="30 min promedio"
                    else:
                        if(duracionCanalProvisional=="4"):
                            duracionCanal="45 min promedio"
                        else:
                            if(duracionCanalProvisional=="5"):
                                duracionCanal="1 hora promedio"
                            else:
                                duracionCanal="mas 1 hora"
            graph.run("MATCH (a:canal),(b:duracion) WHERE a.name='"+nombreCanal+"' AND b.name='"+duracionCanal+"' CREATE (b)-[d:duracion]->(a)").data()
            if(dinamismoCanalProvisional=="1"):
                dinamismoCanal="Activo"
            else:
                dinamismoCanal="Pasivo"
            graph.run("MATCH (a:canal),(b:dinamicidad) WHERE a.name='"+nombreCanal+"' AND b.name='"+dinamismoCanal+"' CREATE (b)-[di:esDinamico]->(a)").data()
            if(ejercicioCanalProvisional=="1"):
                ejercicioCanal="Yoga"
            else:
                if(ejercicioCanalProvisional=="2"):
                    ejercicioCanal="Crossfit"
                else:
                    if(ejercicioCanalProvisional=="3"):
                        ejercicioCanal="Tai Chi"
                    else:
                        if(ejercicioCanalProvisional=="4"):
                            ejercicioCanal="Calistenia"
                        else:
                            if(ejercicioCanalProvisional=="5"):
                                ejercicioCanal="Pilates"
                            else:
                                if(ejercicioCanalProvisional=="6"):
                                    ejercicioCanal="Cardio"
                                else:
                                    if(ejercicioCanalProvisional=="7"):
                                        ejercicioCanal="Body Building"
                                    else:
                                        if(ejercicioCanalProvisional=="8"):
                                            ejercicioCanal="Zumba"
                                        else:
                                            ejercicioCanal="Aerobicos"
            graph.run("MATCH (a:canal),(b:ejercicio) WHERE a.name='"+nombreCanal+"' AND b.name='"+ejercicioCanal+"' CREATE (b)-[e:es_ejercicio]->(a)").data()
            if(tipoCanalProvisional=="1"):
                tipoCanal="En Vivo"
            else:
                tipoCanal="Pre Grabadas"       
            graph.run("MATCH (a:canal),(b:video) WHERE a.name='"+nombreCanal+"' AND b.name='"+tipoCanal+"' CREATE (b)-[e:tipoVideo]->(a)").data()
            print("Se ha añadido con exito tu canal a nuestra base de datos, a continuacion te mostraremos los nombres de los canales existentes y deberias de encontrar el tuyo entre ellos :)\n")
            print("\n**************************************************************************\n")
            names=graph.run("MATCH (a:canal) RETURN a.name").data()
            print(names)
            print()
            print()
            print("Gracias por usar nuestro programa")
        else:
            print("\n**************************************************************************\nA continuacion se te mostraran todos los nombres de los canales que tenemos en nuestra base de datos, por favor ingresa EXACTAMENTE IGUAL, el canal que deseas eliminar")
            print()
            names=graph.run("MATCH (a:canal) RETURN a.name").data()
            print(names)
            print()
            nombreBorrar=input("\n**************************************************************************\nIngresa el nombre del canal que quieres borar: \n")
            graph.run("MATCH (Canal:canal{name:'"+nombreBorrar+"'}) DETACH DELETE Canal").data()
            print()
            print("\n**************************************************************************\nSe te mostrara de nuevo los nombres y ya no deberias de ver ese nombre en la lista")
            print()
            names=graph.run("MATCH (a:canal) RETURN a.name").data()
            print(names)
            print()
            print()
            print("Gracias por usar nuestro programa")
    else:
        print("Has ingresado una opción inválida, por favor, intentalo de nuevo")