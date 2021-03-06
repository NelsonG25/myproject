from django.urls import path
from .views import index, login, factura, orden_compra, crear_producto, Agregar_proveedor,eliminar_proveedor,Modificar_proveedor,Listar_proveedor,Agregar_insumos,Listar_insumos,Modificar_insumos,Eliminar_insumos


urlpatterns = [
    path('', login, name="login"),
    path('index/', index, name="index"),
    path('agregar_proveedor/', Agregar_proveedor, name="agregar_proveedor"),
    path('eliminar_proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('modificar_proveedor/<id>/', Modificar_proveedor, name="modificar_proveedor"),
    path('listar_proveedor/', Listar_proveedor, name="listar_proveedor"),
    path('agregar_insumos/', Agregar_insumos, name="agregar_insumos"),
    path('listar_insumos/', Listar_insumos, name="listar_insumos"),
    path('modificar_insumos/<id>/', Modificar_insumos, name="modificar_insumos"),
    path('eliminar_insumos/<id>/', Eliminar_insumos, name="eliminar_insumos"),
    path('crear_producto', crear_producto, name="crear_producto"),
    path('orden_compra', orden_compra, name="orden_compra"),
    path('factura', factura, name="factura"),

]
