import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Tournament Simulator")

df = pd.DataFrame(
    [
       {"Round": 1, "Pod Size": 12, "Advance": 2, "Edge": 0.0},
       {"Round": 2, "Pod Size": 13, "Advance": 1, "Edge": 0.0},
       {"Round": 3, "Pod Size": 16, "Advance": 1, "Edge": 0.0}
   ]
)

dynamic_df = st.data_editor(df, num_rows="dynamic")

entries = st.slider("Number of Entries",min_value=1, max_value=150)
sims = st.slider("Number of Simulations to Run", min_value=1, max_value=1000)
entry_fee = st.number_input("Entry Fee",step=1)

round_list = dynamic_df['Pod Size'].tolist()
advance_list = dynamic_df['Advance'].tolist()
edge_list = dynamic_df['Edge'].tolist()

st.write("Total entries in contest")

contest_size = np.prod([a/b for a,b in zip(round_list,advance_list)]) * round_list[-1]
contest_size
