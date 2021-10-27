import streamlit as st
import time
from transformers import pipeline

COUNTRY_MAP = {
    'angielski': 'en',
    'niemiecki': 'de'
}

FLAGS_MAP = {
    'angielski': '🇬🇧',
    'niemiecki': '🇩🇪'
}

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

with st.spinner(text='Uruchamiam się ....'):
    time.sleep(2)

st.title('Zajęcia 2. Aplikacja do tłumaczenia tekstu')

st.text('Jest to aplikacja służąca do tłumaczenia tekstu angielskiego na niemiecki.')

option1 = st.selectbox(
    "Język pierwotny",
    [   'Angielski'
    ]
)

option2 = st.selectbox(
    "Język docelowy",
    [   'Niemiecki'
    ]
)

if option1 != option2:
    text = st.text_area(label="Wpisz {0} tekst {2} aby przetłumaczyć go na {1} {3}".format(option1, option2, FLAGS_MAP[option1.lower()], FLAGS_MAP[option2.lower()]))
    if text:
        with st.spinner(text='Pracuję...'):
            classifier = pipeline("translation_{0}_to_{1}".format(COUNTRY_MAP[option1.lower()], COUNTRY_MAP[option2.lower()]))
            try: 
                answer = classifier(text)
                st.success('Done')
                st.header("Przetłumaczony tekst: ")
                st.code(answer[0]['translation_text'])
                
            except Exception:
                st.error("Nie mogłem przetłumaczyć tego tekstu 😢")
else:
    st.error("Język pierwotny oraz język docelowy muszą się różnić")
