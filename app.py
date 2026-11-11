import streamlit as st
from lingua import Language, LanguageDetectorBuilder

# Configuração da página
st.set_page_config(page_title="Separador de Traduções", layout="wide")

DETECTOR_IDIOMAS = LanguageDetectorBuilder.from_languages(
    Language.PORTUGUESE,
    Language.ENGLISH,
    Language.SPANISH,
).build()
modo_escuro = st.session_state.get("modo_escuro", False)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        color-scheme: light;
        --ink: #162f4b;
        --muted: #526b82;
        --paper: #f4f8fc;
        --surface: #ffffff;
        --line: #d8e2ee;
        --accent: #2868a8;
        --accent-strong: #174d80;
        --coral: #d95747;
        --control-bg: #edf4fb;
        --control-border: #cddced;
        --switch-off: #9aacbf;
        --switch-on: #2868a8;
    }

    [data-testid="stAppViewContainer"] {
        color: var(--ink);
        background-color: var(--paper);
        background-image:
            linear-gradient(135deg, rgba(255, 255, 255, .9), rgba(237, 244, 251, .88)),
            linear-gradient(rgba(40, 104, 168, .035) 1px, transparent 1px),
            linear-gradient(90deg, rgba(40, 104, 168, .035) 1px, transparent 1px);
        background-size: auto, 30px 30px, 30px 30px;
    }

    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 980px; padding: 3rem 1.5rem 4rem; }
    [data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] p,
    label, [data-testid="stCaptionContainer"] { color: var(--muted); }

    .eyebrow {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 14px;
        color: var(--accent);
        font: 700 11px/1 'DM Sans', sans-serif;
        letter-spacing: 0;
    }
    .eyebrow-mark { color: var(--coral); font-size: 16px; }
    .eyebrow-divider { color: #a4b8ae; }

    h1 {
        color: var(--ink) !important;
        font: 700 44px/1.08 'Space Grotesk', 'DM Sans', sans-serif !important;
        letter-spacing: 0 !important;
        margin-bottom: 28px !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, .88);
        border: 1px solid var(--line);
        border-radius: 10px;
        box-shadow: 0 12px 32px rgba(25, 57, 90, .055);
    }

    [data-testid="stCheckbox"] {
        min-height: 48px;
        padding: 6px 12px;
        background: var(--control-bg);
        border: 1px solid var(--control-border);
        border-radius: 8px;
    }
    [data-testid="stCheckbox"] label {
        min-height: 34px;
        gap: 10px;
        color: var(--ink);
        font: 700 15px/1.2 'DM Sans', sans-serif;
    }
    [data-testid="stCheckbox"] label p {
        color: var(--ink) !important;
        font: 700 15px/1.2 'DM Sans', sans-serif;
    }
    [data-testid="stCheckbox"] label > div:first-of-type {
        border-radius: 999px;
        background: var(--switch-off) !important;
        transition: background .16s ease;
    }
    [data-testid="stCheckbox"] label:has(input[role="switch"]:checked) > div:first-of-type {
        background: var(--switch-on) !important;
    }

    [data-testid="stTextArea"] label {
        color: var(--ink);
        font: 600 13px 'DM Sans', sans-serif;
    }
    [data-testid="stTextArea"] textarea {
        color: var(--ink);
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 7px;
        font: 14px/1.55 'DM Sans', sans-serif;
        transition: border-color .16s ease, box-shadow .16s ease;
    }
    [data-testid="stTextArea"] textarea::placeholder {
        color: #647a71 !important;
        opacity: 1 !important;
    }
    [data-testid="stTextArea"] textarea:focus {
        border-color: var(--accent);
        box-shadow: 0 0 0 3px rgba(40, 104, 168, .14);
    }

    [data-testid="stButton"] button[kind="primary"] {
        min-height: 42px;
        padding: 0 19px;
        color: #fff;
        background: var(--accent);
        border: 1px solid var(--accent);
        border-radius: 7px;
        font: 700 14px 'DM Sans', sans-serif;
        transition: background .16s ease, border-color .16s ease, transform .16s ease;
    }
    [data-testid="stButton"] button[kind="primary"] p { color: #fff !important; }
    [data-testid="stButton"] button[kind="primary"]:hover {
        background: var(--accent-strong);
        border-color: var(--accent-strong);
        transform: translateY(-1px);
    }

    [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--line);
    }
    button[data-baseweb="tab"] {
        min-height: 44px;
        color: var(--muted);
        border-radius: 6px 6px 0 0;
        font: 600 13px 'DM Sans', sans-serif;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: var(--accent-strong);
        background: rgba(40, 104, 168, .08);
        border-bottom: 2px solid var(--coral);
    }
    button[data-baseweb="tab"] p { color: inherit !important; }
    button[data-baseweb="tab"][aria-selected="true"] p { color: var(--accent-strong) !important; }

    [data-testid="stDownloadButton"] button {
        color: var(--accent-strong);
        background: #e9f1fb;
        border: 1px solid #cddbeb;
        border-radius: 7px;
        font: 600 13px 'DM Sans', sans-serif;
    }
    [data-testid="stDownloadButton"] button p { color: var(--accent-strong) !important; }
    [data-testid="stDownloadButton"] button:hover {
        color: #fff;
        background: var(--accent);
        border-color: var(--accent);
    }
    [data-testid="stDownloadButton"] button:hover p { color: #fff !important; }
    [data-testid="stAlert"] {
        border: 1px solid #c9dced;
        border-radius: 8px;
        background: #eaf3fb;
        color: var(--accent-strong);
    }
    [data-testid="stAlert"] p { color: var(--accent-strong) !important; }
    [data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) {
        background: #eaf3fb !important;
        border: 1px solid #c9dced;
        border-radius: 8px;
        color: var(--accent-strong) !important;
    }
    [data-testid="stAlertContentSuccess"] { color: var(--accent-strong) !important; }

    @media (max-width: 640px) {
        .block-container { padding: 1.5rem 1rem 2.5rem; }
        h1 { font-size: 34px !important; margin-bottom: 20px !important; }
        [data-baseweb="tab-list"] { gap: 2px; }
        button[data-baseweb="tab"] { padding: 0 8px; font-size: 12px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if modo_escuro:
    st.markdown(
        """
        <style>
        :root {
            color-scheme: dark;
            --ink: #e8f1fb;
            --muted: #b3c3d6;
            --paper: #111a26;
            --surface: #1a2735;
            --line: #3b5068;
            --accent: #347bb9;
            --accent-strong: #c2dcf5;
            --coral: #ff8c7c;
            --control-bg: #1b2b3c;
            --control-border: #425d79;
            --switch-off: #7189a3;
            --switch-on: #4a93d1;
        }
        [data-testid="stAppViewContainer"] {
            background-color: var(--paper) !important;
            background-image:
                linear-gradient(135deg, rgba(17, 26, 38, .97), rgba(23, 37, 54, .96)),
                linear-gradient(rgba(156, 187, 220, .035) 1px, transparent 1px),
                linear-gradient(90deg, rgba(156, 187, 220, .035) 1px, transparent 1px);
        }
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(26, 39, 53, .94);
            border-color: var(--line);
            box-shadow: 0 12px 32px rgba(0, 0, 0, .18);
        }
        [data-testid="stTextArea"] textarea {
            color: var(--ink);
            background: #172332;
            border-color: #405771;
        }
        [data-testid="stTextArea"] textarea::placeholder { color: #a9bdd2 !important; }
        [data-testid="stTextArea"] label { color: var(--ink); }
        [data-testid="stButton"] button[kind="primary"]:hover {
            background: #28649a;
            border-color: #28649a;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            background: rgba(85, 148, 207, .16);
        }
        [data-testid="stDownloadButton"] button {
            color: #cfe4f8;
            background: #20364d;
            border-color: #3c5a78;
        }
        [data-testid="stDownloadButton"] button p { color: #cfe4f8 !important; }
        [data-testid="stAlert"],
        [data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) {
            color: #d6e9fa !important;
            background: #1c3650 !important;
            border-color: #3a6388 !important;
        }
        [data-testid="stAlert"] p,
        [data-testid="stAlertContentSuccess"] { color: #d6e9fa !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

identificacao_coluna, tema_coluna = st.columns([3, 1], vertical_alignment="center")
with identificacao_coluna:
    st.markdown(
        '<div class="eyebrow"><span class="eyebrow-mark">✳</span> TRANSLATION DESK <span class="eyebrow-divider">/</span> PT · EN · ES</div>',
        unsafe_allow_html=True,
    )
with tema_coluna:
    st.toggle("Modo escuro", key="modo_escuro")

st.title("Separador de traduções")

with st.container(border=True):
    texto_usuario = st.text_area(
        "Texto de entrada",
        height=250,
        placeholder="iclass.generic.label.exemplo\nTexto em Português\nText in English\nTexto en Español",
    )
    processar = st.button("Processar e separar", type="primary")

if processar:
    if not texto_usuario.strip():
        st.warning("Por favor, cole algum texto antes de processar.")
    else:
        linhas_brutas = texto_usuario.strip().split('\n')

        portugues = []
        ingles = []
        espanhol = []
        tags_unicas = []

        ultima_chave = None
        proxima_posicao = 0
        resultados_por_idioma = {
            Language.PORTUGUESE: portugues,
            Language.ENGLISH: ingles,
            Language.SPANISH: espanhol,
        }
        chaves_vistas = set()

        for linha in linhas_brutas:
            linha = linha.strip()
            if not linha:
                continue

            if "=" in linha:
                chave, valor = (parte.strip() for parte in linha.split("=", 1))
                ultima_chave = None
                proxima_posicao = 0

                if chave not in chaves_vistas:
                    tags_unicas.append(f'"{chave}",')
                    chaves_vistas.add(chave)

            elif "." in linha and " " not in linha:
                ultima_chave = linha
                proxima_posicao = 0
                if linha not in chaves_vistas:
                    tags_unicas.append(f'"{linha}",')
                    chaves_vistas.add(linha)
                continue

            elif ultima_chave and proxima_posicao < 3:
                chave = ultima_chave
                proxima_posicao += 1
                valor = linha
            else:
                continue

            idioma = DETECTOR_IDIOMAS.detect_language_of(valor)
            destino = resultados_por_idioma.get(idioma)
            if destino is not None:
                destino.append(f"{chave}={valor}")

        st.success("Traduções separadas com sucesso!")

        # Abas na tela
        aba1, aba2, aba3, aba4 = st.tabs(["🏷️ Tags para o Java", "🇧🇷 Português", "🇺🇸 Inglês", "🇪🇸 Espanhol"])

        with aba1:
            resultado_tags = "\n".join(tags_unicas)
            st.text_area("Tags Java", resultado_tags, height=200)

        with aba2:
            resultado_pt = "\n".join(portugues)
            st.text_area("Português", resultado_pt, height=150)
            if portugues:
                st.download_button("Baixar messages_pt.properties", resultado_pt, file_name="messages_pt.properties", mime="text/plain", key="dl_pt")

        with aba3:
            resultado_en = "\n".join(ingles)
            st.text_area("Inglês", resultado_en, height=150)
            if ingles:
                st.download_button("Baixar messages_en.properties", resultado_en, file_name="messages_en.properties", mime="text/plain", key="dl_en")

        with aba4:
            resultado_es = "\n".join(espanhol)
            st.text_area("Espanhol", resultado_es, height=150)
            if espanhol:
                st.download_button("Baixar messages_es.properties", resultado_es, file_name="messages_es.properties", mime="text/plain", key="dl_es")
