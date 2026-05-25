class PuestoTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

    def __str__(self):
        return (f"Código: {self.codigo} | Desc.: {self.descripcion} | Área: {self.areaSolicitante} "
                f"| Plazas: {self.plazasRequeridas} | Sueldo: S/.{self.sueldo:.2f}")


def BuscarPuesto(lst, puesto) -> bool:
    for s in lst:
        if s.codigo == puesto.codigo or s.descripcion.lower() == puesto.descripcion.lower():
            return True
    return False


def OrdenarBurbuja(lst):
    """Ordena de mayor a menor por código (selección, no burbuja — se mantiene la lógica original)."""
    n = len(lst)
    for mano in range(n - 1):
        posMayor = mano
        for ver in range(mano + 1, n):
            if lst[ver].codigo > lst[posMayor].codigo:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[posMayor], lst[mano]


def OrdenarInserc(lst):
    """Ordena de menor a mayor por sueldo."""
    n = len(lst)
    for paso in range(1, n):
        nueNum = paso
        while nueNum >= 1 and lst[nueNum].sueldo < lst[nueNum - 1].sueldo:
            lst[nueNum], lst[nueNum - 1] = lst[nueNum - 1], lst[nueNum]
            nueNum -= 1


def input_int(prompt, min_val=None, max_val=None) -> int:
    """Solicita un entero con validación de tipo y rango opcional."""
    while True:
        try:
            valor = int(input(prompt))
            if min_val is not None and valor < min_val:
                print(f"  ✖ Debe ser mayor o igual a {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"  ✖ Debe ser menor o igual a {max_val}.")
                continue
            return valor
        except ValueError:
            print("  ✖ Ingrese un número entero válido.")


def input_float(prompt, min_val=None) -> float:
    """Solicita un float con validación de tipo y mínimo opcional."""
    while True:
        try:
            valor = float(input(prompt))
            if min_val is not None and valor < min_val:
                print(f"  ✖ Debe ser mayor o igual a {min_val}.")
                continue
            return valor
        except ValueError:
            print("  ✖ Ingrese un número válido.")


def input_str(prompt, min_len=3) -> str:
    """Solicita un string con longitud mínima."""
    while True:
        valor = input(prompt).strip()
        if len(valor) < min_len:
            print(f"  ✖ Mínimo {min_len} caracteres.")
            continue
        return valor


# ── Programa principal ──────────────────────────────────────────────────────
lista = []

while True:
    print("\n----------------------")
    print("1. Agregar Puesto")
    print("2. Mostrar Todo")
    print("3. Borrar Puesto")
    print("4. Buscar por Sueldo")
    print("5. Puestos a Contratar")
    print("6. Salir")
    print("----------------------")

    op = input_int("Ingrese opción: ", min_val=1, max_val=6)

    # ── 1. Agregar ───────────────────────────────────────────────────────────
    if op == 1:
        print("\n** Texto mínimo: 3 letras | Números mayores a 0 **\n")
        codigo = input_int("Código: ", min_val=1)
        desc   = input_str("Descripción: ")
        area   = input_str("Área Solicitante: ")
        plazas = input_int("Plazas Requeridas: ", min_val=1)
        sueldo = input_float("Sueldo: ", min_val=0.01)

        nuevo = PuestoTrabajo(codigo, desc, area, plazas, sueldo)
        if not BuscarPuesto(lista, nuevo):
            lista.append(nuevo)
            print(f"\n  ✔ Puesto agregado:\n  {nuevo}\n")
        else:
            print("\n  ✖ Ya existe un puesto con ese código o descripción.\n")

    # ── 2. Mostrar todo ──────────────────────────────────────────────────────
    elif op == 2:
        if not lista:
            print("\n  (Sin registros)\n")
        else:
            print()
            for p in lista:
                print(" ", p)
            print()

    # ── 3. Borrar ────────────────────────────────────────────────────────────
    elif op == 3:
        if not lista:
            print("\n  (Sin registros para borrar)\n")
        else:
            OrdenarBurbuja(lista)
            print("\n  Lista ordenada por código (mayor → menor):\n")
            for p in lista:
                print(" ", p)

            borrar = input_int("\n  Código a borrar: ", min_val=1)
            encontrado = next((p for p in lista if p.codigo == borrar), None)

            if encontrado:
                lista.remove(encontrado)
                print(f"\n  ✔ Puesto '{encontrado.descripcion}' eliminado.\n")
                if lista:
                    for p in lista:
                        print(" ", p)
                else:
                    print("  (Lista vacía)\n")
            else:
                print(f"\n  ✖ No se encontró el código {borrar}.\n")

    # ── 4. Buscar por sueldo ─────────────────────────────────────────────────
    elif op == 4:
        if not lista:
            print("\n  (Sin registros)\n")
        else:
            sueldo_buscado = input_float("\n  Ingrese el sueldo a buscar: S/.", min_val=0)
            resultados = [p for p in lista if p.sueldo == sueldo_buscado]
            if resultados:
                print(f"\n  Puestos con sueldo S/.{sueldo_buscado:.2f}:\n")
                for p in resultados:
                    print(" ", p)
                print()
            else:
                print(f"\n  ✖ No se encontraron puestos con sueldo S/.{sueldo_buscado:.2f}.\n")

    # ── 5. Puestos a contratar (ordenados por sueldo) ────────────────────────
    elif op == 5:
        if not lista:
            print("\n  (Sin registros)\n")
        else:
            OrdenarInserc(lista)
            total_plazas  = sum(p.plazasRequeridas for p in lista)
            costo_total   = sum(p.plazasRequeridas * p.sueldo for p in lista)

            print("\n  Puestos a contratar (orden ascendente por sueldo):\n")
            for p in lista:
                print(" ", p)
            print(f"\n  Total de plazas : {total_plazas}")
            print(f"  Costo mensual   : S/.{costo_total:,.2f}\n")

    # ── 6. Salir ─────────────────────────────────────────────────────────────
    elif op == 6:
        print("\n  Hasta luego.\n")
        break