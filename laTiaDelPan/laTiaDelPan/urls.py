"""laTiaDelPan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views as frontend_views
from backend import views as backend_views
from backend.Vistas import VistaCategoria
from backend.Vistas import VistaProveedor
from backend.Vistas import VistaUsuario
from backend.Vistas import VistasProducto
from backend.Vistas import VistaVenta
from backend.Vistas import VistaFacturaProv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend_views.login),
    path('principal/', frontend_views.paginaPrincipal),
    path('analisis/', frontend_views.analisisVenta),

    path('usuario/', VistaUsuario.usuario),
    path('crearUsu/', VistaUsuario.nuevoUsuario),
    path('editUsu/', VistaUsuario.editarUsuario),
    path('eliminarUsu/', VistaUsuario.eliminarUsuario),

    path('categoria/', VistaCategoria.categoria),
    path('crearCate/', VistaCategoria.nuevaCategoria),
    path('editCate/', VistaCategoria.editarCategoria),
    path('eliminarCate/', VistaCategoria.eliminarCategoria),

    path('proveedor/', VistaProveedor.proveedor),
    path('nuevoProv/', VistaProveedor.nuevoProv),
    path('editProv/', VistaProveedor.editarProv),
    
    path('producto/', VistasProducto.producto),
    path('crearProd/', VistasProducto.nuevoProducto),
    path('editProd/', VistasProducto.editProducto),

    path('facturaProveedor/', VistaFacturaProv.factura),
    path('facturaProveedor/obtenerProducto', VistaFacturaProv.postProducto, name="post_productos"),
    

    path('venta/', VistaVenta.venta),
    path('venta/obtenerProducto', VistaVenta.postProducto, name="post_producto"),
    path('realizarVenta/', VistaVenta.realizarVenta, name="post_venta")
]
