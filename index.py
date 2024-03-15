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
    "machas están rodeadas por una zona de transición de color amarillento.",
    "manchas se secan y su centro es de color gris.",
    "presentan añublo de las hojas.",
    "se secan las lesiones en su área central de color gris",
    "Están en un ambiente con humedad alta",
    "deficiencias en la fertilización.",
    "Se presentan en las palmas jóvenes (3 a 5 años)",
    "Hojas amarillas",
    "nivel freático superficial.",
    "No presenta gran cantidad de boro.",
    "flechas afectadas por pudrición color crema a pardo.",
    "Las hojas inferiores, medias y basales conservan su aspecto y color verde normales.",
    "Los tejidos basales de las flechas se pudren totalmente",
    "tejidos basales con coloración blanco-amarillenta y olor fétido.",
    "Floración femenina intensiva",
    "Origen fisiogénico",
    "Producción excesiva de racimos",
    "Origen genético",
    "Se secan progresivamente las hojas centrales de la corona",
    "Presentan larvas de Tiquadra, Cephaloleia, Herminode, insulsa, Brassolis sophorae y Rhynchophorus palma.",
    "Invasión por patógenos débiles como petalotipsis",
    "Presencia de un subsuelo muy ácido.",
    "Puntas de los folíolos se secan",
    "Hay presencia de maleza",
    "Procesos de desnitrificación",
    "Restricción en disponibilidad del nitrógeno.",
    "Hongos invasores Fomes y Ganoderma",
    "El tronco se quiebra a una altura aproximada de 2 metros del suelo.",
    "Hojas de color amarillento.",
    "presencia de hongo Fusariumfusarium oxysporum",
    "Coloración marrón bronceada",
    "necrosis de la lámina foliar",
    "Se pudren las inflorescencias",
    "Presencia del hongo Cortisium koleroga.",
    "Presencia de maleza",
    "Están en un ambiente con humedad alta",
    "presencia de nemátodo Radinaphelenchus cocophillus",
    "Presencia de agente vector Rhynchophorus palmarum",
    "Compactación anormal de las flechas y hojas jóvenes de la corona",
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

for sintoma in sintomas_seleccionados:
     
    for sintoma in sintomas_seleccionados:

  if(sintoma==20):

    print("Amarillamiento de las hojas inferiores")
    print("Amarillamiento letal de las hojas jóvenes ")
    print("Pudrición letal de la flecha y el cogollo")
    print("Deficiencia de magnesio ")
    print("Deficiencia de nitrógeno ")
    print("Pudrición de la parte superior del tronco ")
    print("Secamiento por Hongo Botryodiplodia ")
