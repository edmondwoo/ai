
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image
import streamlit_pandas as sp
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.sidebar.header("Plotting Demo")

image = Image.open('LSTM.jpg')

st.title('Cryptocurrency')

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

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"], key="1")

with st.sidebar.header('2. Upload your second CSV data'):
    uploaded_file_2 = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"],key="2")
    
toc.placeholder()





toc.header("Data Source")
toc.subheader('BTC Data Source')
# Pandas Profiling Report(BTC)
if uploaded_file is not None:
    @st.cache(allow_output_mutation=True)
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
toc.subheader('IXIC Data Source')
if uploaded_file_2 is not None:
    @st.cache(allow_output_mutation=True)
    def load_csv_2():
        csv = pd.read_csv(uploaded_file_2)
        return csv
    df1 = load_csv_2()
    pr1 = ProfileReport(df1, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df1)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr1)

toc.title("Libaray")
toc.subheader('yfinance')
st.write('Yahoo! Finance is a media property that is part of the Yahoo! network. It provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content. It also offers some online tools for personal finance management. In addition to posting partner content from other web sites, it posts original stories by its team of staff journalists. It is ranked 20th by SimilarWeb on the list of largest news and media websites.')
toc.subheader('pandas')
st.write(' it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license. The name is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.')
toc.subheader('LSTM')
st.write('Long Short Term Memory Networks is an advanced RNN, a sequential network, that allows information to persist. It is capable of handling the vanishing gradient problem faced by RNN. A recurrent neural network is also known as RNN is used for persistent memory.')
st.write('Let’s say while watching a video you remember the previous scene or while reading a book you know what happened in the earlier chapter. Similarly RNNs work, they remember the previous information and use it for processing the current input. The shortcoming of RNN is, they can not remember Long term dependencies due to vanishing gradient. LSTMs are explicitly designed to avoid long-term dependency problems.')
st.image(image, caption='LSTM Model')



toc.title("Crytocurrency")
st.write('Cryptocurrency is a relatively new medium of exchange that’s gained popularity in the past decade. Crypto cheerleaders think the future of finance is cryptocurrency rather than stocks and conventional forms of currency, while others believe that the unregulated nature of cryptocurrency makes it too risky to support a full-fledged financial system. Cryptocurrencies lack government backing, and how much the market will bear determines their value.')
st.write('Cryptocurrencies are maintained on decentralized networks of computers spread around the world. Strong cryptography provides security to transactions and storage, hence the term “cryptocurrency.” A cryptocurrency owner must use a password of at least 16 characters to gain access.')
toc.header("Is Cryptocurrency similar to Stocks")
st.write('As more and more investors and speculators flock towards cryptocurrencies as an asset class, many have started likening them to stocks. While crypto and stocks do indeed share certain characteristics, they are fundamentally different.')
toc.header('Similarities')
toc.subheader('1. Risk and volatility')
st.write('It should be no surprise that cryptocurrency asset prices have been quite volatile. In Figure 1 below, from the Refinitiv market data system, you can see that the price of Bitcoin (in orange) and the tech-heavy NASDAQ 100 stock index have experienced quite a lot of change over the last five years.')

if uploaded_file and uploaded_file_2 is not None:
    df['Date'] = pd.to_datetime(df['Date'])
    df1['Date'] = pd.to_datetime(df1['Date'])
    fig=plt.figure(figsize=(9,8))
    ax = sns.lineplot(data=df,y='Close' ,x='Date' ,label='BTC')
    sns.lineplot(data=df1,ax = ax,y='Close' ,x='Date' ,label='IXICT')
    st.pyplot(fig)



st.write('It means that both holders of Bitcoin or a basket of technology stocks would have experienced price changes over the past five years. But the degree of price changes with Bitcoin is significantly higher, as shown in Figure 2.')

if uploaded_file and uploaded_file_2 is not None:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Close_pct_change']=df['Close'].pct_change()
    df1['Date'] = pd.to_datetime(df1['Date'])
    df1['Close_pct_change']=df1['Close'].pct_change()
    fig=plt.figure(figsize=(9,8))
    ax = sns.lineplot(data=df,y='Close_pct_change' ,x='Date' ,label='BTC')
    sns.lineplot(data=df1,ax = ax,y='Close_pct_change' ,x='Date' ,label='IXICT')
    st.pyplot(fig)



st.write('This chart has the same price history over the past five years but overlayed with the price change as a proxy for price volatility. The line in blue is the one-year percentage change in the price of Bitcoin, and the yellow line represents the same one-year percentage change in the NASDAQ 100 index. Here, you can clearly see that the volatility for Bitcoin is much higher.')
toc.subheader('2.How they are transacted')
st.write('Another similarity between cryptocurrencies and stocks is the way that both assets are bought and sold. Platforms such as Robinhood, Wealthsimple, and SoFi have started blurring the lines between digital assets and legacy financial products. Users can access and trade their stocks and cryptocurrencies using the same frictionless platform.')
toc.subheader('3.Scams')
st.write('Given the temptation of quick money, it is no surprise that both equities and cryptocurrencies suffer from fraudulent behavior. One of the most common is the “Pump and Dump” scam. Like we often see in penny stocks, unscrupulous parties artificially inflate the price of the cryptocurrency through false or exaggerated statements, celebrity “endorsements,” or simply investor greed (FOMO).')
st.write('Once the price goes up, the fraudster unloads its holdings and, in most cases, disappears. Crypto data firm Chainalysis estimates that there were $2.8bn in crypto “pump and dump” scams for 2021.')
toc.subheader('4. More and more common investors')
st.write('Despite the nascent nature of cryptocurrencies, more and more institutional investors are investing in cryptocurrencies, digital assets, blockchain technology, and decentralized finance (DeFI). These professional investors will require greater transparency, liquidity, and regulation in cryptocurrency assets, which can be viewed as a positive for the market as a whole.')
toc.header('Differences')
toc.subheader('1.Supply')
st.write('Some cryptocurrencies are limited in their supply, the most famous being Bitcoin. However, other cryptocurrencies do not have a ceiling on how much cryptocurrency can eventually be mined or minted. Stocks, on the other hand, tend to be less variable, as the amount of shares outstanding is controlled and ultimately backed by the operations of the issuing company.')
st.write('Another thing to consider is the absolute size difference between global stock markets and cryptocurrencies. As of 2021, the amount of stocks outstanding globally was estimated to be 106 trillion, while the total size of crypto markets was only 2.6 trillion, a mere 2.5% of the much larger equity, or stock market.')
toc.subheader('2.Regulation')
st.write('Equities, or stocks, are generally scrutinized by securities and other regulators in their country of origin. Additionally, for stocks that trade in an organized exchange, the exchange also provides oversight of the company and may delist the company should anything go wrong. While by no means does this provide a guarantee, it is certainly more than any safeguards when investing in cryptocurrencies.')
st.write('Furthermore, cryptocurrencies are based on the concept of decentralization, which allows the trustless peer-to-peer exchange of value over the internet without any intermediaries. As a matter of fact, the appeal of cryptocurrencies for many is the fact that the identities of the sender and receiver of cryptos are hidden, unlike traditional stocks.')
toc.subheader('3.Purpose')
st.write('Speaking of exchanging value, many cryptocurrencies were designed as transactional cryptocurrencies, which means that they are meant to be a sort of digital currency or coin.')
st.write('On the other hand, when one purchases a stock, they are buying a fractional ownership share in the issuing company. However, when one purchases a cryptocurrency, they are not necessarily getting a fractional ownership of the blockchain – just a medium of exchange.')
st.write('Yes, there are projects that are a token that may represent partial ownership and voting rights for a project. Still, for the most part, a cryptocurrency is closer to owning a currency or commodity, like gold.')
toc.subheader('4.Technology')
st.write('The last and most important difference between stocks and cryptocurrencies is the blockchain technology that underpins all cryptocurrencies. Many cryptocurrencies allow for programming to be added, changing the nature of the crypto asset into ‘programmable money.')
st.write('Other use cases can be built upon certain cryptocurrencies, such as smart contracts and other DeFi uses, like Dapps (decentralized applications). The only uses for stocks are capital appreciation, dividend cash flow, and voting rights.')

toc.title('The factors affect the Crytocurrency')
toc.subheader('1.Supply and demand')
st.write('Cryptocurrency’s value is determined by supply and demand. When demand increases faster than supply, the price increases. Bitcoin, for instance, has a fixed supply of 21 million Bitcoins. Others, like Ethereum, have no supply cap. Some governing teams dictate their entire cryptocurrency’s suppl, soy they can decide to release more tokens to the public or burn them to manage the money supply. Some cryptocurrencies have ways to “burn” – or send to an unrecoverable address on the blockchain – existing tokens to prevent the circulating supply from growing too large. Demand can also increase as a currency gains awareness or its utility increases, especially if it becomes an investment.')
toc.subheader('2.Production Cost')
st.write('New cryptocurrency tokens are produced through a “mining” process. The miners have to use a computer to verify the next block on the blockchain. The more competition there is to mine a certain cryptocurrency, the more difficult it is to mine because miners race to solve a complex math problem in order to verify a block. So, the cost to mine increases as the team needs more powerful equipment – such as computers – to mine successfully. As mining costs increase, the cryptocurrency also increases in value. Miners won’t mine if the value of the currency they’re mining isn’t enough to offset their costs. So, as long as there’s demand to use blockchain, the price will have to increase.')
toc.subheader('3.Node Counts')
st.write('Node counts show how many active wallets exist in the same network so you can find out the community’s strength.  A high count means a stronger community and increases the chances for that currency to weather a potential crisis. You can check the currency’s home page or Google search to learn the count. If you compare it and its total market capitalization with a popular currency, you can see how node count influences price.')

# toc.title('PredictionofBitcoin')
# st.write('Cryptocurrency is a relatively new medium of exchange that’s gained popularity in the past decade. Crypto cheerleaders think the future of finance is cryptocurrency rather than stocks and conventional forms of currency, while others believe that the unregulated nature of cryptocurrency makes it too risky to support a full-fledged financial system. Cryptocurrencies lack government backing, and how much the market will bear determines their value.')
# st.write('Cryptocurrencies are maintained on decentralized networks of computers spread around the world. Strong cryptography provides security to transactions and storage, hence the term “cryptocurrency.” A cryptocurrency owner must use a password of at least 16 characters to gain access.')

# toc.header("Subheader 2")
toc.generate()


