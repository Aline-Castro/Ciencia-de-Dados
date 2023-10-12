# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time

st.set_page_config(
    page_title="EBAC | Módulo 15 | Streamlit I | Exercício 1",
    # page_icon="https://ebaconline.com.br/favicon.ico",
    page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAhFBMVEX///8EBwgAAADW1tZmZ2dqbGzr7OwUFhf4+Phtb29QUlPx8vJ+gIAAAwX8/Pzu7++Sk5SHiYlCRETIyckgIiK7vLwYGhvk5OSsra20tbUvMTKfoKDe3t7Cw8MpKyzS09OWmJijpKQ5OjtFRkc1NzhZW1t4eXoOEBFUVleFhoYdHx8kJyhyIAHNAAALl0lEQVR4nO1daXuyOhDVYRFFQEFkVRAF1P7//3fBBQMkLBL60ufmfGppSnKyTmZOwmzGwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMAwAYS8gAF/E/91wb6D5MuVJzYQcFP/SQkHQgz3fLltjB+YYwEQ/psyDoLPZ23D+8gTbUUgmFP0/llBv4W/AiUr+fkkvZ9ICZFgTvHwL0vbH+pBh1fJ12+K65wymaIuNb5xatDcd3sBbF/PjEVjG/6xbiqmBRsQ3g+NPZnip6n/CMRPe8GyeGrcSRQh1v5hab8BnuHssCCsh2fr35X1OxAYzswtDreNT3wTt+Rp4kTLtCAxnElYkLPNFh268ChRJDLsCVloXGL6A8CeFEN5SZkgPYp0GEr0CVKjSIWhSruL0qRIpw3NtMEK+p7hmTxz/zbDmTmnTxF0GgRpMVQ9hTZFiDgaBKmtFmo4B4UmIAqoEKTGcKbe6C74kUGHID2GM5mjCmr2Lz2GUwVj+Pfx/2LIy834k87gEsOf66oJZ/uXKdJxCCEM50rbGnUiveXQY3X27Y62yuFGxagRmzyHVTsqxTuDJVv5cbpmGJwh6pTYWcCFxqrfhyHBFvaTbJ+TdtzoGC4osG9PbG2z7Qoc7eE9tRfDbDKq+xKzRoG8fTcdAm+quYNHZ9hUg10V5F6fR0JhsPOyJ8P6UBQvz90vQNxe39ziHUJoCX448E442MPei6ECca2hxLfzGKC9uo2XL0ABszmh83YawOZrau8C9hqHUX0cirs+DF+7yIkyVGCHmdv+FMO29TDFFesvMYTLuhEJdnUal6EyPKpesbzVJuBfMDLDwQ7FwXuLXgzNrnOpXSTsbCwRC/irDE9FwYkm7gPqpmtVdCjgrzJcFyH15kiyJMB78husi/hdhueCod6YWIsKhoP3FzQZthumUcHw3pi410vbCjiYodu9MNaxYLjrypCm5f0dQzkuOlTr4vwR6sC90R/K9TF2WzCYYTHtZRZDW9q4yEtplACqRVXAuWWb1Y7hvrZDUZpjS2kcJAYH54bJVNKL3hwO9g0NZxi8GbZ1U4lHjHz4afBQHAppJAz3YwxnyO2K4jR3KbsUKAaenPK9GtJYLCgwlJef8jRtyP2yZhUWRIvTKURnsBquSabg87Y/b2iwsSy3RDBLPCeYnEH0eSGFQD4Fhsbu84o7adxwVYK5mwlbH1yM1BgFLSsFhioiuIU7ttSa96mFeTEaQTnVvCKqeUHeJlBwexMYGtsNHrg2shGZAii3WhLJ4wEhmH4Sw3ljoMuBZq/RFUUZT23CHYnBZ4xPWI7RZQBcIeE+Sjgr5GNA/z7fINJOgCMvCIlnn+wwEYQsJZr0SiNygVXQlopcBgiYFcEsKW6zUrp6gSj7HVklFNhqfCU1QLpIF8+f0L/sqSjKtY+5X6igZx5Z4oR1nKhV0Rfa6pW/6H7eQ2pvrabLnyV0Yl3c+fFuBSLv3SdMIDYhQYolXjv6JJ8zUScJFT01sp8PEwX4IkAm1qq4nPMO95JzJ4qQPtZAadMuoYIrvQNI1i0FQA7NyHxT9oD3DQXndvGeAvfX/8qbllYEiGnKrSXHvaE9wrqQsyeGSa24qW8///VaLCSSeWxIrpRqnArE8rTMEaX6CqxJw19O3ObxeyyF1DhhT0ie8YtOg7eFLTBS0nrYMDpUTrjUp8Q3PzepbBNUR3ChRjKfVVe3XzgQYBJMmk1zwN7YPPTsFQ1eXjFYY8gI1zXT4rw9TfvAg2/a60u5zIvYdkiFlgLHccKEz7Ue/NpzHJOKpnRkSH4QBMbByWEaQcC1TRqqLIqWZYljjz0GBgYGBgYGBgYGht9GroCSDO95gNs2LaIiahzIt3gz4rF/SbScVaTr0c/L7Znu3ew3fcuJ2m/QlPwk32C6iT/K5Q2SfxD2L/czIHv0p2PaDYOxN6iiwae5KyTLNeUN6jcaieZ2UXdTIx4UgIs35uUtlhMX2ef5Ub5kRDvxJHYlmrfBYjoCuM21lD+4tM4gPqCacRu9t9tsL1DN+ZV/kEQVzxvENDOwkn3nE+cAP12OHvSBZlxrLmLlEyoaDtWp1l8bRyoHyd+wTH1Rzx+OFPPwunVQtH4vDq3JPPCiumc4Z3imtjipYT0DpSRrz9aMWv6LkApFc3vEVq9C8+I0KaoQfC5/7ipeJss41o8vH38lUTpckSWZwg92eOS+fZue/1QqBf+yylv8JIeA8y1RljVRtHwuCOz4Xh0qRazsS6iifb7j+OUliA9Uo2voBXTZoh4HYr0DymLAX8rlGXTrgcp57pzA7yJwdP3fEqrRcbcWqfOp4lova9NWX1f0YZNip5eM34pcgm/xkfwAbJsXcx9Vxnx93kN11gvs9JKRXp7GuF7Te06Y2SrXOrK0ExqCh8sXl1fIXkwafrA+jBOeCdw0A0DSpfpM9BaT3gpXVdxEKXb1y6zBDeXhh2SbzZiib3c8kmqjDHe97A6VIwy/7NnFE6dyHF5DxDO9Tu3I5ha/ecn4xZO6jRHVNMGqq7tBemzO6vTyY9LJWBuyb3FD5Zbdpj7ptiKtDmloTKV7FkBE97DosFdUrTXe+MyNQ2eSkfuPairbxLU1gBYIpOG3iCgan1SB6MLaRKCiE5OGn8uXfT7+CK6Db3H7NEnzpbt+uCLtjaJtxVowozmlqxIpABWvNzDkaq6XYvit7Orwc3JDYExHcC9IhbZPgRWBoRysdoTZU6l7QrXHLhyo3WE2GOuXtg/git9eaIczaXVwBatWKdL1mViB3UQoqsZjHwU7UrcKSfzOWFmeVqQGfiqLYy4tBpfkALdwsujsHwQPbyAgDIWpMJyJ9s+V2KNMjDA92xuZpNVvkgyzZiQabFpVSJ3Ru6858qw7UYZkGOUmzGyzaFOfXhD8NYbSEkr8sr1Ri3H21xj6Hzs0G377dfs1aH+Noejc5g+SkOvXu+yN/hrDrJ9y9nmfDz/b71TgiTJsdpZq/npldjUzp8nQaNvcqd1DN1NkKDlHUKpnKJoR4A9o5pggQ2u5gHn3235V2RHysIcr4MOO02Po688iwU+nQKl8u9zhuT26n08Yv+jkGErFSTVIO33jav1hAPPjtubbnhzDw77THv8Dp3JpWtUGLxgqE2GInk/v9nGk0slipbaPmlwbor42khejjE1lO5XvhdefBXVqDFWkRWDZzWipfckt92fEwauzTo0hctb7dbK3HbiDwlln1c1HQ06MIbo56hq3mFlnQtRwdzImxxDd38Kla1BarOjyPp11nziyMiWGoo7O/D0+WiSaAiE8ml6V4oXjMJS0DBbX6d0y6kYD6OXelLkbNkiD8B6HocU/RU/rDoEgOSlJQJc9Y0eqeDviIzWjMnxpMRTgWwXAYumzQKQbvhshbVZYrcKIDEt6mpbD2quyZCj5Sr0n2UlKPNfebX3tB7WkiUrIMVlLqNxm9bXKVD1sCIpr5WcEzUJF13Y8B1q9aSTRiCsy3obrutqh+uERq2uDNPIwurpBkPRywSHdL43AFx+fe1AlWfS5wBTSanmUgZ+zzLWJuPhbrh1aB1Sj33h96X6VhJ7nhdvk6uL0pQr2uqGeOR8E3A0g+d5jaVLUt6nbdo0wpqaHX3mfw9jqBFOHp9iMUthX550RXNIKSHM2VmpD9/PRqt148womd5fm/SqWsdrX65juh4dVf0m6LqYOBdIVZZmPzAm1Oob94HugS5BMXunGMdvUjaDzUf1bde/RdD3mV5BtQely7inyRtJpaWFZ20fr63loFma4I55dey0ifNcP4XwD0VmWzq6F9LNQ/QO/2ytVms+lY3HXT62XzQyEFtz2eUPmC3JEkDUMhSxym7Ouu+jFeYob6fryYP3GIVLJ2kRzOOpbf8TcVEmSg3ApvLEMOa3pa8e0s5e9JPi97BgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGJ74D5yAv1/ehoqRAAAAAElFTkSuQmCC",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown('''
<img src="data:image/png;base64,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" alt="ebac-logo">

---

# **Profissão: Cientista de Dados**
### **Módulo 15** | Streamlit I | Exercício 1

Aline de Castro Santos<br>
Data: Outubro de 2023.

---
            ''', unsafe_allow_html=True)

st.title('Viagens de Uber em NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Carregando dados...')
data = load_data(10000)
data_load_state.text("Pronto! (usando st.cache_data)")

if st.checkbox('Mostrar dados brutos'):
    st.subheader('Dados brutos')
    st.write(data)

st.subheader('Número de viagens por hora')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Algum número no intervalo 0-23
hour_to_filter = st.slider('hora', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de todas as viagens de Uber às %s:00' % hour_to_filter)
st.map(filtered_data)

# Análise de tendências ao longo do tempo
if st.checkbox('Mostrar tendências ao longo do tempo'):
    st.subheader('Número de viagens por dia')
    hist_values = np.histogram(data[DATE_COLUMN].dt.day, bins=30, range=(1,31))[0]
    st.bar_chart(hist_values)

# Análise geográfica mais detalhada
if st.checkbox('Mostrar análise geográfica detalhada'):
    st.subheader('Mapa de todas as viagens')
    st.map(data)
