import streamlit as st

class Toc:

    def __init__(self):
        self._items = []
        self._placeholder = None
    
    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=True):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()
    
    def placeholders(self, sidebar=False):
        self._placeholders = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)
    
    def _markdown(self, text, level, space=""):
        key = "".join(filter(str, text)).lower()
        print(text)
        key = key.replace(' ','-')
        key = key.replace('.','-')

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")

        
toc = Toc()

toc.title('Prediction of Bitcoin')
# st.write('Cryptocurrency is a relatively new medium of exchange that’s gained popularity in the past decade. Crypto cheerleaders think the future of finance is cryptocurrency rather than stocks and conventional forms of currency, while others believe that the unregulated nature of cryptocurrency makes it too risky to support a full-fledged financial system. Cryptocurrencies lack government backing, and how much the market will bear determines their value.')
# st.write('Cryptocurrencies are maintained on decentralized networks of computers spread around the world. Strong cryptography provides security to transactions and storage, hence the term “cryptocurrency.” A cryptocurrency owner must use a password of at least 16 characters to gain access.')

# toc.header("Subheader 2")
toc.generate()