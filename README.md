# Separador de Traduções

Aplicativo Streamlit para separar traduções em Português, Inglês e Espanhol e gerar uma lista de tags para Java.

## Requisitos

- Python 3.10 ou superior
- Dependências listadas em `requirements.txt`

## Instalação e execução

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

No Windows:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Depois de iniciar, abra o endereço local exibido pelo Streamlit, geralmente `http://localhost:8501`.

## Formatos de entrada

### Chave seguida das traduções

Informe a chave em uma linha e, nas três linhas seguintes, as traduções em qualquer ordem. O app tenta identificar o idioma de cada texto. Linhas vazias são ignoradas.

```text
class.generic.label.exemplo
Texto em Português
Text in English
Texto en Español
```

Repita o mesmo formato para cada chave.

### Chave e valor na mesma linha

Também é possível informar pares `chave=valor`:

```text
class.generic.label.exemplo=Texto em Português
```

Nesse formato, o idioma também é identificado automaticamente. A detecção é feita pela biblioteca Lingua e pode falhar em palavras muito curtas ou ambíguas.

## Resultados

O app apresenta quatro abas:

- **Tags para o Java:** lista de chaves únicas, formatada para uso no código Java.
- **Português:** conteúdo no formato `.properties`, com opção de download.
- **Inglês:** conteúdo no formato `.properties`, com opção de download.
- **Espanhol:** conteúdo no formato `.properties`, com opção de download.

Use o controle **Modo escuro** no cabeçalho para alternar a aparência da interface.
