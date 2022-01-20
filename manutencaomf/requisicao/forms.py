# IMPORT AREA
from dataclasses import fields
from django import forms
from .models import Solicitacao
# CODE AREA


class requisicaoForm(forms.ModelForm):
    
    class Meta:
        model = Solicitacao
        fields = ('fullname','factory','machine_code','sector','priority_type','issue_description')
        labels = {
            'fullname':'Nome do solicitante',
            'factory':'Fábrica',
            'machine_code':'Código da máquina',
            'sector':'Setor',
            'priority_type':'Tipo de prioridade',
            'issue_description':'Descrição do problema'
        }
    #fazer esse procedimento para as dopbox
    #colocar um rótulo inicial na listbox
    #no campo self.fields colocar o nome do item que vem da bd
    # nesse caso o FACTORY
    def __init__(self, *args, **kwargs):
        super(requisicaoForm,self).__init__(*args, **kwargs)
        self.fields['factory'].empty_label = "Selecione"

