from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")
for linea in lineas[2:]:
    print("-", linea)

productos = lineas[2:]
total = 0
for linea in productos:
    precio = linea.split("$")[1].replace(".", "")
    total += int(precio)

print("Total de productos:", len(productos))
print("Valor del inventario: $" + str(total))