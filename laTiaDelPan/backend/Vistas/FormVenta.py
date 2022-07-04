from django import forms
from backend.models import Producto
#from Controladores.ControladorProductos import ControladorProductos

class FormVenta(forms.ModelForm):
    codigo = forms.CharField(label='Escanee el producto: ', widget=forms.widgets.TextInput())
    
    def __init__(self, *args, **kwargs):
        super(FormVenta, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    
    class Meta:
        model = Producto
        field = ['PROD_CODIGO']
        exclude = ['PROD_NOMBRE', 'PROD_VALOR', 'PROD_STOCK', 'PROV_RUT', 'CAT_ID', 'PROD_ESTADO']