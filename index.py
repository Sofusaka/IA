informacion = [
    "embrión sobre la radícula presenta una mancha de color crema.",
    "La raíz presenta mancha color crema.",
    "lesiones presenta un moho de color verde-azul.",
    "Presencia de hongos Aspergillus y Penicillium.",
    "semilla en etapa de precalentamiento y germinación.",
    "semilla presenta parches blancos.",
    "semilla presenta restos de pulpa.",
    "ambiente húmedo presenta fructificaciones.",
    "utiliza pesticidas a base de BHC-gama, cobre y mercurio.",
    "La emergencia de la radícula se retarda.",
    "la radícula se desarrolla de color marrón e hinchada anormalmente.",
    "No presenta mohos.",
    "Manchas translúcidas en las hojas de color marrón oscuro.",
    "manchas se secan y su centro es de color gris.",
    "presentan añublo de las hojas.",
    "se secan las lesiones en su área central de color gris.",
    "Están en un ambiente con humedad alta.",
    "deficiencias en la fertilización.",
    "Se presentan en las palmas jóvenes (3 a 5 años).",
    "Hojas Amarillas",
    "nivel freático superficial.",
    "Deficiencia de nitrógeno",
    "flechas afectadas por pudrición color crema a pardo.",
    "Las hojas inferiores, medias y basales conservan su aspecto y color verde normales.",
    "Los tejidos basales de las flechas se pudren totalmente.",
    "Floración femenina intensiva.",
    "Origen fisiogénico.",
    "Producción excesiva de racimos.",
    "Origen genético.",
    "Se secan progresivamente las hojas centrales de la corona.",
    "Presentan larvas de Tiquadra, Cephaloleia, Herminode, insulsa, Brassolis sophorae.",
    "Invasión por patógenos débiles como petalotipsis.",
    "Presencia de un subsuelo muy ácido.",
    "Puntas de los folíolos se secan.",
    "Procesos de desnitrificación.",
    "Restricción en disponibilidad del nitrógeno.",
    "Hongos invasores Fomes y Ganoderma.",
    "El tronco se quiebra a una altura aproximada de 2 metros del suelo.",
    "presencia de hongo Fusariumfusarium oxysporum.",
    "Coloración marrón bronceada.",
    "necrosis de la lámina foliar.",
    "Se pudren las inflorescencias.",
    "Presencia del hongo Cortisium koleroga.",
    "Presencia de maleza.",
    "presencia de nemátodo Radinaphelenchus cocophillus.",
    "Presencia de agente vector Rhynchophorus palmarum.",
    "Compactación anormal de las flechas y hojas jóvenes de la corona.",
    "las inflorescencias abortan."
]


sintomas_seleccionados=[]
informacion_dict = {}
for i, observacion in enumerate(informacion):
    informacion_dict[i + 1] = observacion



numero = int(input("Ingrese el número de síntoma a ingresar: "))

print("**Menú de opciones:**")
for observacion in informacion_dict.items():
        print(f" {observacion}")



while numero>0:
    opcion = int(input("Seleccione una opción: "))
    sintomas_seleccionados.append(opcion)
    if opcion == 0:
        break
    print(f"\n-Síntoma seleccinado: {informacion_dict[opcion]}")
    numero=numero-1



print("===============Síntomas seleccionados===============")

for sintoma in sintomas_seleccionados:
    print({informacion_dict[sintoma]})

print("===============ENFERMEDAD===============")

while True:

        if 35 and 36 in sintomas_seleccionados:
         sintomas_seleccionados.append(22)
         print("Deficiencia de nitrógeno")
       
         ##solucionar loop

        if 20 in sintomas_seleccionados:

            if 32 and 33 and 34 in sintomas_seleccionados:
                sintomas_seleccionados.append(44)
                print("Deficiencia de magnesio")

            if 35 and 36 in sintomas_seleccionados:
                sintomas_seleccionados.append(22)
                print("Deficiencia de nitrógeno")

            if 19 and 21 and 22 in sintomas_seleccionados:
                print("Amarillamiento de las hojas inferiores")
                break
            if 23 and 24 and 25 in sintomas_seleccionados:
                print("Amarillamiento letal de las hojas jóvenes ")
                break

            if 30 and 31 in sintomas_seleccionados:
               print("Pudrición letal de la flecha y el cogollo")
               break
            
            if 37 and 38 in sintomas_seleccionados:
                print("Pudrición de la parte superior del tronco ")
                break

            if 13 and 14 and 15 and 17 in sintomas_seleccionados:
                print("Secamiento por Hongo Botryodiplodia")
                break

            print("Deficiencia de magnesio ")
            print("Deficiencia de nitrógeno ")
      
        if 26 and 27 and 28 and 29:
            print("Doblamiento de la base de las hojas")
            break
        
        if 17 in sintomas_seleccionados:
            if 13 and 14 and 15 and 20 in sintomas_seleccionados:
                print("Secamiento por Hongo Botryodiplodia")
                break
            elif 16 and 18 in sintomas_seleccionados:
                print("Secamiento por Melanconium")
                break
            elif 43 and 44 in sintomas_seleccionados:
                print("Mal de hilachas")
                break
        
        if 39 and 40 and 41 and 42 in sintomas_seleccionados:
            print("Secamiento letal o marchitez vascular")
            break
        
        if 46 in sintomas_seleccionados:
            if 45 and 47 and 48 in sintomas_seleccionados:
                print("Anillo Marrón")
                break
            if 30 and 31 and 20 in sintomas_seleccionados:
                print ("Pudrición letal de la flecha y el cogollo")
                break
                
        if 1 and 2 and 3 and 4 in sintomas_seleccionados:
            print("Germen Marrón")
            break
        elif 5 and 6 and 7 and 8 in sintomas_seleccionados:
            print("Pudrición de la semilla")
            break
        elif  9 and 10 and 11 and 12 in sintomas_seleccionados:
            print("Fitotoxicidad por pesticidas")
            break

   