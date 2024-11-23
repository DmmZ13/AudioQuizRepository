from django import forms
from .models import Classe, Deck, Card, Mensagem, Arquivo
from accounts.models import Usuario  # Supondo que o modelo de usuário esteja em `usuarios.models`

from django import forms
from .models import Classe, Usuario

class ClasseForm(forms.ModelForm):
    alunos = forms.ModelMultipleChoiceField(
        queryset=Usuario.objects.filter(tipo=False),  # Filtrar apenas alunos (tipo=False)
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Estilo dropdown múltiplo
        required=False,  # Torna opcional selecionar alunos no momento da criação
        label="Alunos"
    )

    class Meta:
        model = Classe
        fields = ['turma', 'idioma', 'poster', 'alunos']
        labels = {
            'turma': 'Turma',
            'idioma': 'Idioma',
            'poster': 'Poster',
        }

    def save(self, commit=True):
        # Salvar a classe e associar os alunos selecionados
        classe = super().save(commit=False)
        if commit:
            classe.save()
            self.save_m2m()  # Salvar relações Many-to-Many (alunos associados à classe)
        return classe

# Formulário para o modelo Deck
class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['nome', 'n_cartoes']
        labels = {
            'nome': 'Nome do Deck',
            'n_cartoes': 'Número de Cartões',
        }


# Formulário para o modelo Card
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['lado_frente', 'lado_tras', 'dica_1', 'dica_2', 'dica_3', 'n_revisoes', 'maduro', 'data_ultima_revisao']
        labels = {
            'lado_frente': 'Lado Frente',
            'lado_tras': 'Lado Trás',
            'dica_1': 'Dica 1',
            'dica_2': 'Dica 2',
            'dica_3': 'Dica 3',
            'n_revisoes': 'Número de Revisões',
            'maduro': 'Maduro',
            'data_ultima_revisao': 'Última Revisão',
        }
        widgets = {
            'data_ultima_revisao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# Formulário para o modelo Mensagem
class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['conteudo', 'tipo', 'resposta_para']  # Removido 'usuario'
        labels = {
            'conteudo': 'Conteúdo',
            'tipo': 'Tipo',
        }
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'tipo': forms.Select(choices=Mensagem.TIPOS),
            'resposta_para': forms.HiddenInput(),  # Oculto no formulário padrão
        }

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['nome']  # Removido 'usuario'
        labels = {
            'nome': 'Nome do Arquivo',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do arquivo'}),
        }