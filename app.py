import pandas as pd
import streamlit as st

sb = st.sidebar

df = pd.read_csv("./tag.csv", index_col=0, header=1)
st.set_page_config(layout="wide")

# Text

st.title("Graph Index")

option_datasets = [
    "All datasets (default)", "Manually select multiple datasets"
]
option_columns = ["All metrics (default)", "Manually select multiple columns"]
select_all_datasets = sb.selectbox("Select dataset(s) to view.",
                                   option_datasets,
                                   index=0)
select_all_columns = sb.selectbox("Select metrics(s) to view.",
                                  option_columns,
                                  index=0)
is_select_all_datasets = select_all_datasets == option_datasets[0]
is_select_all_columns = select_all_columns == option_columns[0]
indices = list(df.index) if is_select_all_datasets else sb.multiselect(
    "Select dataset(s) to view. Click 'x' on the right to cancel all selections.",
    list(df.index),
    default=list(df.index))
columns = list(df.columns) if is_select_all_columns else sb.multiselect(
    "Select column(s) to view.  Click 'x' on the right to cancel all selections.",
    list(df.columns), list(df.columns))

df_ = df[columns].loc[indices]
st.subheader("Datasets vs. Metrics")
st.dataframe(df_, height=1000)
st.subheader("Metrics vs. Datasets")
st.write("This is a transpose version of the first table.")
st.dataframe(df_.transpose().apply(pd.to_numeric), height=1000)