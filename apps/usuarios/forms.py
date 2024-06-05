from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    
    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    
    email = forms.EmailField(
        label = 'E-mail',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    
    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    
    confirmar_senha = forms.CharField(
        label = 'Confirmar Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha mais uma vez'
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if  ' ' in nome:
                raise forms.ValidationError('Não é possível inserir espaços dentro do campo Nome de Cadastro')
            else:
                return nome
    
    
    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        
        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError('As senhas não são iguais')
            else:
                return confirmar_senha
            