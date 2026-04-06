from graphviz import Digraph

# Crear el diagrama ER con Graphviz
dot = Digraph(comment="Diagrama ER - Sistema DONGLAI")
dot.attr(rankdir='LR', size='10')

# Entidades
entities = {
    "Producto": ["idProducto (PK)", "nombre", "descripcion", "precio", "stock", "idCategoria (FK)"],
    "CategoriaProducto": ["idCategoria (PK)", "nombreCategoria"],
    "Proveedor": ["idProveedor (PK)", "nombre", "contacto", "direccion"],
    "Compra": ["idCompra (PK)", "fecha", "idProveedor (FK)", "totalCompra"],
    "DetalleCompra": ["idDetalleCompra (PK)", "idCompra (FK)", "idProducto (FK)", "cantidad", "precioUnitario"],
    "Cliente": ["idCliente (PK)", "nombre", "apellido", "email", "telefono"],
    "Venta": ["idVenta (PK)", "fecha", "idCliente (FK)", "idEmpleado (FK)", "totalVenta"],
    "DetalleVenta": ["idDetalleVenta (PK)", "idVenta (FK)", "idProducto (FK)", "cantidad", "precioUnitario"],
    "Empleado": ["idEmpleado (PK)", "nombre", "apellido", "usuario", "contraseña", "rol"]
}

# Crear nodos para cada entidad
for entity, attributes in entities.items():
    label = f"<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0'>"
    label += f"<TR><TD BGCOLOR='lightblue'><B>{entity}</B></TD></TR>"
    for attr in attributes:
        label += f"<TR><TD ALIGN='LEFT'>{attr}</TD></TR>"
    label += "</TABLE>>"
    dot.node(entity, label=label, shape="plaintext")

# Relaciones
dot.edge("CategoriaProducto", "Producto", label="1..*")
dot.edge("Producto", "DetalleCompra", label="1..*")
dot.edge("Compra", "DetalleCompra", label="1..*")
dot.edge("Proveedor", "Compra", label="1..*")
dot.edge("Cliente", "Venta", label="1..*")
dot.edge("Empleado", "Venta", label="1..*")
dot.edge("Venta", "DetalleVenta", label="1..*")
dot.edge("Producto", "DetalleVenta", label="1..*")

# Guardar como archivo y mostrar
dot.format = 'png'
output_path = '/mnt/data/diagrama_ER_DONGLAI'
dot.render(output_path, cleanup=True)

output_path + ".png"
