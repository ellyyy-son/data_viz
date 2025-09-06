import streamlit as st  
from streamlit import components

st.title("Topic Modeling on P-Pop related Reddit and Youtube Comments ✨")

with st.expander('Introduction'):
    st.write("""
    The contemporary Pinoy Pop (P-Pop) movement represents a significant cultural and musical evolution, aiming to transcend the local range and gain international traction. This phenomenon is deeply rooted in the historical evolution of Filipino popular music, which began with the emergence of Original Pilipino Music (OPM) in the late 1970s (Spotify, 2019). The genre was a mix of rock, folk, and ballads that often served as social commentary and reflected multiple Filipino realities. 

    In the early 2000s, groups like SexBomb Girls and Viva Hot Babes were also popular groups that introduced the pop group format. This laid the groundwork for a music scene that was culturally affirming and reflective of national identity. As globalization expanded and the Korean Wave (Hallyu) and J-pop gained prominence, the Filipino pop genre shifted towards an "idol group" format, characterized by rigorous training, intense choreography, and high production values (Tautho, 2023). This new style mirrors the trends that have made Korean and Japanese popular music globally dominant, captivating Generation Z and reshaping mainstream Filipino culture. 

    Within this flourishing landscape, two groups stand out: SB19 and BINI. Both have contributed significantly to putting Filipino music on the international map and have cultivated a dedicated global following. Indeed, contrasting both groups based on their origin and internal support serves as a foundation for understanding their identity. 

    BINI was formed in 2019 through ABS-CBN’s Star Hunt Academy, an idol training program (ABS-CBN, 2019). BINI's rise is characterized by their meticulously crafted image as the "Nation's Girl Group" and their viral hits like "Pantropiko" and "Karera." However, this institutional support has also become a source of public contention, with a vocal segment of their fandom expressing frustration over what they perceive as "lackluster promotion" and strategic missteps by their management. Issues also surrounded their members with a video leak involving inappropriate behavior. Additionally, their recent video “BINI Tries & Rates Filipino Snacks” with the YouTube channel PeopleVsFood gained negative attention from netizens. 

    In contrast, SB19’s narrative is one of creative autonomy earned through struggle. They were formed in 2018 under the Korean management company ShowBT Philippines, where they endured rigorous K-pop–style training without compensation. Their journey sparked disputes over their identity as a group, eventually leading to their departure from ShowBT and the establishment of their own company (Kang, 2023).
    """)

with st.expander('Research Questions'):
    st.write("""
    - What are the main topics discussed in recent online comments about BINI and SB19?  
    - Which topics are linked to positive vs negative comments about BINI and SB19?  
    """)

with st.expander('Methodology'):
    st.write("""
    The study is based on scraping a large, unstructured corpus of text data from online platforms, including YouTube and Reddit. These platforms are central to the online discourse surrounding P-Pop, providing opportunities for raw discourse analysis through comments and discussions. For the YouTube data collection, the researchers gathered five videos each from both BINI and SB19’s official channels to see the patterns projected on their own platforms. Additionally, ten videos from external channels concerning each group were used for reference. For Reddit data collection, comments from Filipino subreddits that are active with P-Pop discussions were retrieved, namely r/ChikaPH, r/PPOPcommunity, and r/PinoyCelebs. Additionally, comments from both r/BINI and r/SB19 were retrieved.

    To prepare this raw data for analysis, a series of critical preprocessing steps were undertaken. The researchers first identified the type of data that was collected and ensured the consistency and quality of these data. Consequently, tokenization took place, a process that breaks down the text into individual words or tokens, along with the removal of common English and Filipino stopwords (e.g., "the," "naman," "a") that do not contribute to the analysis. Additionally, domain-specific stopwords were also determined and removed. The tokenization was done using Python’s SciKit-Learn CountVectorizer module.

    Once tokenization was completed, the resulting document-term matrix was processed using the Latent Dirichlet Allocation (LDA) algorithm for topic modeling. The topics were then visualized with pyLDAvis, which provided an interactive representation of the model. This visualization was subsequently analyzed to identify the dominant topics present within the comments.
    """)

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
    st.write("""
    The topic’s top terms included ‘talented,’ ‘best,’ ‘proud,’ ‘success,’ and ‘hit,’ showing a picture of comments commending the groups for their artistry. This shows that people enjoy the music they produce, the performances they deliver, and the creative content they release, all of which contribute to a sense of pride in the groups’ accomplishments. The comments also highlight their talent and emphasize how the groups represent the country well, not losing to others. 

    Comments include:

    “Salamat OG blooms di nyo sila pinabayaan habang kame ay di pa blooms. Again nakakaproud sila, they made it!”

    “I’m A’TIN pero sobrang nkaka proud tlga tong dlwang group na to. Just look at them, sariling atin yan.”

    “Sobrang talented nila, and hanga ako dahil self managed na pala sila under 1Z entertainment. Taas ng standards na sinet nila. Artist sila, pero sila na din ung composer, producer, mix and match, creative director sa mga MV nila lahat na kaya sobrang natutuwa ako sa group nila. Naiinis ako sa sarili ko dati na parang tinawanan ko pa sila.”

    However, along with these terms is the word “K-Pop.” The simultaneous mention of the word shows us that people are often comparing the groups to K-Pop ones, but not necessarily in a bad way. Many comments recall how some listeners initially dismissed the groups as “K-Pop wannabes,” but later grew to appreciate them. These stories often highlight fans who shifted from being K-Pop followers to P-Pop supporters, with some even encouraging others to make the same transition. 

    Comments include:

    “Same, galit na galit ako sa kanila dati kasi nga Kpopanget at wannabe Kpop. Look at me now, lagi nang updated at gusto pumunta sa mga cons nila. Sila lang siguro yung dating hater ka maging fan ka pag nakilala mo sila at talagang nakinig ka sa music nila.”

    “Nakakatuwa actually na andaming nang nakikilalang Ppop artists na may talent talaga ha, as in may boses and galaw — same with BINI. Not naman a hater of Kpop, pero I really think it's time that we support, be proud and love our own.”
    """)

st.write("\n")
st.header("Topic 2")
with st.container(border=True):
    st.subheader("Public Discourse and Fandom Tensions between BINI and SB19 related to Issues and Management")
    st.write(f"This topic, representing approximately 24.3% of the total tokens analyzed, captures a complex narrative centered on the perceived actions and strategies of BINI and SB19’s respective managements. The keywords indicate a public and fan discourse that is highly critical and emotionally charged.") 
    st.write(f"Key terms such as 'management', 'issue', 'kpop', 'toxic', and 'hate' co-occur frequently, highlighting a thematic cluster of frustration and conflict. The analysis suggests that a significant portion of the online conversation is driven by fans and the public debating and critiquing management decisions, which are often compared to the business models of K-pop companies.")
    st.write(f"Some of the comments were: 'oa gen z day kinacancel pansin toxic cancel culture,' 'wild thought answer sagutin basher inis sagot basher mapapahiya honesty panget content kasalanan management hayst,' and 'apology nitong apparently apology maraming hate natatanggap'")
    st.write(f"The topic also reveals a duality in fan sentiment. While words like happy and cute appear, they exist in close proximity to negative terms like downfall and mali (wrong), indicating a potential conflict between admiration for the artists themselves and dissatisfaction with the corporate hand guiding their career. The presence of words like public relations and statement further suggests that these online conversations are often reactive, driven by official communications or events that are perceived as missteps.")


st.write("\n")
st.header("Topic 3")
with st.container(border=True):
    st.subheader("Commercialization and Accessibility of Promotional Activities")
    st.write("""
    This topic represents 19.9% of all tokens that are analyzed and captures ideas related to the financial and logistical involvement of the fandoms for both BINI and SB19’s promotional activities like concerts and merchandise. Common terms seen in the analysis are “ticket”, “price”, “merch”, and “mahal” (expensive) which reveals a thematic cluster focused on the commercial transaction between artists and their fanbases.

    Some of the comments were: “almost reach believe ticket resold 2k plus dollar area grabeng mahal”.

    The topic reveals the concern of assessing these activities because of affordability. It shows the dedication of the fans as not merely passive consumers; they are actively discussing, and at times struggling with, the monetary costs of their support. This aligns with the concept of a fan community's sense of "collective investment” including time, money, and social capital in their idols' careers.

    However, there are negative comments regarding the quality of merchandise and performance. Merchandises such as totebags/ecobags have been criticized for their “bad” design and its subpar quality does not justify its prices. It shows that the topic of commercialization is not entirely about engaging with their idol’s activity but there is also an expectation of receiving quality fanservice as well.

    Some of the comments were: “chaka sako,” “...quality sirain tingnan itim mukhang sako garbage sizt price merch pinipintasan mamaya mahurt,” and “satire legit merch”.
    """)

st.write("\n")
st.header("Topic 4")
with st.container(border=True):
    st.subheader("Negativity surrounding BINI’s Filipino snack video")
    st.write("""
    This topic represents 19.3% of all the total tokens that are analyzed, and captures the discourse relating to BINI’s Filipino snack video. Common terms seen are “oa”, “toxic”, and “bash”, which reveals negative sentiments towards the video and the group’s reaction. 

    These terms suggest that viewers perceived the members’ responses as exaggerated or inauthentic, sparking criticism and online ridicule. With this very specific topic comprising 19.3% of topics, it is evident that the issue generated substantial attention and became a major point of recent discussion within the community. 

    Comments include:

    “Still some of their reactions were uncomfortable to watch. Kinda crazy because it’s been barely a year since they achieved fame and parang biglang 180 change.”

    “Whoever even decided to shoot that foodtrip vid was pretty stupid. Like what were they selling there? Filipino food? BINI's quirkiness? BINI's relatability? Wala sila naachieve dun.”

    “Arent they Filipino? Is this their first time?”
    """)