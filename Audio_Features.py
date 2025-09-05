import streamlit as st
import pandas as pd
import plotly.graph_objects as go

feature_df = pd.read_csv('data/audio_features.csv')
features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness','normalized_loudness', 'speechiness', 'normalized_tempo', 'valence']

st.sidebar.write("Developed by Elly Olegario")
st.set_page_config(
    page_title="PPop Data Hunters",  
    page_icon=":bar_chart:",  
    layout="wide",  
)

st.title("PPop Data Hunters ✨")

with st.expander('About the Dataset'):
    st.header("PPop")
    st.markdown(
    """
    What the data was gathered:
    - Data gathered consisted of metrics from Facebook, Spotify, X, Instagram, YouTube, and TikTok, covering 17 different P-Pop groups.
    - Top 5 songs per artist were analyzed for their features, covering Energy, Acousticness, Valence, Tempo, Loudness, and Danceability.
    """
    )

    st.markdown(
    """
    How the data was retrieved:
    - All of the data was gathered personally by us using a combination of automated tools and manual methods.
    - We developed Python scripts that utilized various API endpoints to efficiently collect data, specifically for Spotify, X, and YouTube statistics such as follower counts, play counts, and other engagement metrics.
    - Engagement metrics from TikTok, Facebook, and Instagram was manually retrieved through direct platform interaction due to API limitations.
    - Since Spotify's audio features endpoint has been deprecated, we turned to the Reccobeats API to access key musical attributes like danceability, energy, valence, and more.
    """
    )

    st.write("### Preview", feature_df.head())


with st.expander('Data Features'):
    st.dataframe(feature_df.describe(), use_container_width=True)

fig = go.Figure()

st.write('\n')
st.write('\n')
st.write('\n')
st.header('Song Feature Check')
select = st.radio('Check:', ['One Song', 'Multiple Songs'])

if select == 'Multiple Songs':
    radar_song_select = st.multiselect("Select songs to compare:", options=feature_df['track_name'].unique(), default=['Aitakatta - Gustong Makita', 'Pag-ibig Fortune Cookie'])
    for song in radar_song_select:
        row = feature_df[feature_df['track_name'] == song][features].values.flatten().tolist()
        fig.add_trace(go.Scatterpolar(
            r=row + [row[0]],  
            theta=features + [features[0]],
            fill='toself',
            name=song
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    radar_song_select = st.selectbox("Select song:", options=feature_df['track_name'].unique())
    row = feature_df[feature_df['track_name'] == radar_song_select][features].values.flatten().tolist()
    fig.add_trace(go.Scatterpolar(
        r=row + [row[0]],  
        theta=features + [features[0]],
        fill='toself',
        name=radar_song_select
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

st.write('\n')
st.header('Feature Specific Information')
col1, col2= st.columns(2)
with col1:
    st.write('See the top or bottom songs per feature:')
    feature_option_1 = st.selectbox('Select a feature:', features, key = 'feature_1')
    choice = st.radio('See the:', ['Highest', 'Lowest'])
    number = st.number_input("Enter an integer", min_value=0,  max_value=84, value=1, step=1)
    if choice == 'Highest':
        top_songs = feature_df.nlargest(number, feature_option_1)
        st.bar_chart(data=top_songs, x='track_name', y=feature_option_1)
    else:
        bottom_songs = feature_df.nsmallest(number, feature_option_1)
        st.bar_chart(data=bottom_songs, x='track_name', y=feature_option_1)


with col2:
    st.write('See scatterplot of features:')
    feature_option_2 = st.selectbox('Select a feature:', features, key = 'feature_2')
    st.scatter_chart(data=feature_df, x='track_name', y=feature_option_2)



st.write('\n')
st.write('\n')
st.write('\n')
st.header('Artist Specific Information')
col1, col2= st.columns(2)
with col1:
    st.write("Compare Artist's songs per feature:")
    artist_option_1 = st.selectbox('Select an artist:', feature_df['artist_name'].unique(), key= 1)
    feature_option = st.selectbox('Select a feature:', features, key = 3)
    artist_songs_1 = feature_df[feature_df['artist_name'] == artist_option_1]
    artist_songs_1 = artist_songs_1[['track_name', feature_option]]
    st.bar_chart(data=artist_songs_1, x='track_name', y=feature_option)

with col2:
    st.write('See mean song features per artist:')
    artist_option_2 = st.selectbox('Select an artist:', feature_df['artist_name'].unique(), key = 2)
    artist_songs_2 = feature_df[feature_df['artist_name'] == artist_option_2]
    artist_features = artist_songs_2.describe()[features].iloc[1]
    st.bar_chart(data=artist_features, x=None, y='mean')
