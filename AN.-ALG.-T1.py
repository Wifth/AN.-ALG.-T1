class PuestoTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

    def __str__(self):
        return (f"Código: {self.codigo} | Desc.: {self.descripcion} | Área: {self.areaSolicitante}"
                f"| Plazas: {self.plazasRequeridas} | Sueldo: S/.{self.sueldo:.2f}")
    
def BuscarPuesto(lst, puesto) -> bool:
    for s in lst:
        if s.codigo == puesto.codigo or s.descripcion == puesto.descripcion or s.areaSolicitante == puesto.areaSolicitante:
            return True
    return False
    
def OrdenarBurbuja(lst):
    n = len(lst)
    for mano in range(n-1):
        posMayor = mano
        for ver in range(mano + 1, n):
            if lst[ver].codigo > lst[posMayor].codigo:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[posMayor], lst[mano]

def OrdenarInserc(lst):
    n = len(lst)
    for paso in range(1,n):
        nueNum = paso
        while nueNum >= 1 and lst[nueNum] < lst[nueNum - 1]:
            lst[nueNum], lst[nueNum - 1] = lst[nueNum - 1], lst[nueNum]
            nueNum -= 1

lista = []
opc = 0
while opc != 9:
    print ("----------------------")
    print ("1. Agregar Puesto")
    print ("2. Mostrar Todo")
    print ("3. Borrar Puesto")
    print ("4. Buscar Sueldo")
    print ("5. Puestos a Contratar")
    print ("6. Salir")
    print ("----------------------")
    op = int(input("Ingrese opción: "))
    if op == 1:
        print("\n**Texto mínimo: 3 letras | Números mayores a 0**\n")
        codigo = 0
        while codigo <= 0:
            codigo = int(input("Código: "))
        desc = ""
        while len(desc) < 3:
            desc = input("Descripción: ")
        area = ""
        while len(area) < 3:
            area = input("Área Solicitante: ")
        plazas = 0
        while plazas <= 0:
            plazas = int(input("Plazas Requeridas: "))
        sueldo = 0.0
        while sueldo <= 0:
            sueldo = float(input("Sueldo: "))

        nuevo = PuestoTrabajo(codigo, desc, area, plazas, sueldo)
        if not BuscarPuesto(lista, nuevo):
            lista.append(nuevo)
            print("")
            print(nuevo)
            print("")
    elif op == 2:
        for p in lista:
            print(p)
    elif op == 3:
        OrdenarBurbuja(lista)
        for p in lista:
            print(p)

        borrar = int(input("Ingrese el Código del Puesto a Borrar: "))
        for idx, p in enumerate(lista):
            if p.codigo == borrar:
                del lista[idx]

        for p in lista:
            print(p)
    elif op == 4:
        break
    elif op == 5:
        break
    elif op == 6:
        break