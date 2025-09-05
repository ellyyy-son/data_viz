import streamlit as st  
from streamlit import components

st.title("Topic Modeling on P-Pop related Reddit and Youtube Comments ✨")

with st.expander('About the Dataset'):
    st.header("PPop")
    st.markdown(
    """
    What the data was gathered:
    - Data gathered consisted of metrics from Facebook, Spotify, X, Instagram, YouTube, and TikTok, covering 17 different P-Pop groups.
    - Top 5 songs per artist were analyzed for their features, covering Energy, Acousticness, Valence, Tempo, Loudness, and Danceability.
    """
    )
st.write("\n")
st.write("\n")
st.set_page_config(
    layout="wide")
lda = 'static/lda.html'
with open(lda, 'r', encoding='utf-8') as f:  
    html_string = f.read()

components.v1.html(html_string, width=1300, height=800)

st.write("\n")
st.write("\n")
st.write("\n")

st.header("Topic 1")
with st.container(border=True):
    st.subheader("Recognition of BINI and SB19 in the Music Industry")
    st.write("The topic’s top terms included ‘talented’, ‘best’ ‘proud’, ‘success’, and ‘hit’, showing a picture of comments commending the groups for their artistry. This shows that people enjoy the music they produce, the performances they deliver, and the creative content they release, all of which contribute to a sense of pride in the groups’ accomplishments. The comments also highlight their talent and emphasize how the groups represent the country well, not losing to others.")
    st.write("However, along with these terms is the word “K-Pop”.  The simultaneous mention of the word shows us that people are often comparing the groups to K-Pop ones, but not necessarily in a bad way. Many comments recall how some listeners initially dismissed the groups as “K-Pop wannabes,” but later grew to appreciate them. These stories often highlight fans who shifted from being K-Pop followers to P-Pop supporters, with some even encouraging others to make the same transition.")

st.write("\n")
st.header("Topic 2")
with st.expander("Topic 2"):
    st.subheader("Public Discourse and Fandom Tensions between BINI and SB19 related to Issues and Management")
    st.markdown(
    """
    What the data was gathered:
    - Data gathered consisted of metrics from Facebook, Spotify, X, Instagram, YouTube, and TikTok, covering 17 different P-Pop groups.
    - Top 5 songs per artist were analyzed for their features, covering Energy, Acousticness, Valence, Tempo, Loudness, and Danceability.
    """
    )

st.write("\n")
st.header("Topic 3")
with st.container("Topic 3"):
    st.subheader("Commercialization and Accessibility of Promotional Activities")
    st.write("")

st.write("\n")
st.header("Topic 4")
with st.expander("Topic 4"):
    st.subheader("Negativity surrounding BINI’s Filipino snack video")
    st.write("d")