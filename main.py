import os
from dotenv import load_dotenv
import streamlit as st
from analysis_detailed import analysis_details
from speech_toText import recognize_from_audio
import pandas as pd
load_dotenv()
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient



endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
key = os.environ["AZURE_LANGUAGE_KEY"]
import streamlit as st
import time
st.set_page_config(page_title="Sentiment Analysis ", page_icon=":smiley:", layout="wide")
# with st.sidebar:
#     file = st.file_uploader("Upload a file", type=["csv"])
#     if file is not None:
#         with st.spinner("Loading..."):
#             time.sleep(3)
#         st.success("File uploaded Done!")

def create_sidebar():
    with st.sidebar:
        st.header("Upload Audio Files")
        st.write("Upload Customer Audio for Customer Sentiment Analysis ")
        files = st.file_uploader("Upload a file", type=["mp3","wav"])
        if files:
            st.success(f"File '{files.name}' uploaded successfully!")
        else:
            st.warning("No files were uploaded.")
    return files

# Directory to save the uploaded audio
FilePath = "uploads"

def save_uploaded_audio(audio):
    # Create directory if it doesn't exist
    if not os.path.exists(FilePath):
        os.makedirs(FilePath)
    
    # Timestamp to avoid overwriting
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    
    # Construct full file path
    file_path = os.path.join(FilePath, f"{timestamp}_{audio.name}")
    
    # Save the file
    with open(file_path, "wb") as f:
        f.write(audio.getbuffer())
    
    return file_path  # Return the file path

def get_last_uploaded_file(directory):
    # Get list of files and sort by modification time (newest first)
    files = os.listdir(directory)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
    
    # Return the most recently uploaded file path if files exist
    if files:
        return os.path.join(directory, files[0])
    else:
        return None

def bulk_files_analysis(df):
    reviews = {}
    for index, row in df.iterrows():
        text = row['Title']
        # print(reviews)
        doc_result = bulk_file_sentiment_analysis([text])
        reviews[text]= f"{str(doc_result)}"
    return reviews
        

def get_data():
    file = st.file_uploader("Upload a file", type=["csv"])
    if file is not None:
        with st.spinner("Loading..."):
            time.sleep(3)
        st.success("File uploaded Done!")        
        df = pd.read_csv(file)
        # st.write(df.shape[0])
        with st.expander("View Data"):            
            if int(df.shape[0])>0:
                st.dataframe(df,use_container_width=True)
                return df


# documents = [
# This product so far has not disappointed. My children love to use it and I like the ability to monitor control what content they see with eases
# ]

st.title("Sentiment Analysis for Customer Reviews ")
def sentiment_analysis(documents): 
    if len(documents)!=0:
        
        text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))   
        result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
        # st.divider()
        doc_result = [doc for doc in result if not doc.is_error]
        st.subheader("Sentiment Analysis")
        if doc_result[0].sentiment == "positive":
            st.markdown(f"<p style='color:green; font-weight:bold;'>Overall sentiment : {doc_result[0].sentiment}</p>", unsafe_allow_html=True)
        elif doc_result[0].sentiment == "negative":
            st.markdown(f"<p style='color:red; font-weight:bold;'>Overall sentiment : {doc_result[0].sentiment}</p>", unsafe_allow_html=True)
        elif doc_result[0].sentiment == "neutral" or doc_result[0].sentiment == 'mixed':
            st.markdown(f"<p style='color:blue; font-weight:bold;'>Overall sentiment :Neutral </p>", unsafe_allow_html=True)
        # st.text(f"Overall sentiment: {doc_result[0].sentiment}")
        st.divider()
    return doc_result
def bulk_file_sentiment_analysis(documents): 
    if len(documents)!=0:
        
        text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))   
        result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
        # st.divider()
        doc_result = [doc for doc in result if not doc.is_error]
    return doc_result[0].sentiment
        
            

tab1,tab2,tab3=st.tabs(["Text Analysis","Audio to Text","Bulk file Analysis"])
with tab1:
    documents = [st.text_area("Enter your text here",max_chars = 300,placeholder="Enter the Text here ")]
    if len(documents)!=0 and st.button("Analyze"):
        doc_result = sentiment_analysis(documents)
        # value = analysis_details(doc_result)

    # st.write(doc_resultce_scores)

with tab2:
    # filename="test_data2.wav"
    # When a file is uploaded
    # File upload
    value = create_sidebar()
    if value:
        # Save the uploaded audio
        saved_file_path = save_uploaded_audio(value)
        
        # Retrieve the last uploaded file
        last_uploaded_file = get_last_uploaded_file(FilePath)
        # st.write(f"Last uploaded file: {last_uploaded_file}")
        
        # Check if a valid file path is retrieved and play the audio
        # if last_uploaded_file:
            # Display audio using the full path to the file
            
            # text = recognize_from_audio(last_uploaded_file)
        # st.write(f"Uploaded an audio file {last_uploaded_file}")
        if last_uploaded_file:
            st.audio(last_uploaded_file, format="audio/mp3" if last_uploaded_file.endswith(".mp3") else "audio/wav")
        
            
            
        if last_uploaded_file and st.button("SUBMIT"):
            
            
            text = recognize_from_audio(last_uploaded_file)
            sentiment_analysis(text)
    else:
        st.warning("No files were uploaded,Please Upload the audio files")
        # st.write(text)
        # st.divider()
        # text = [text]
        
with tab3:
    df = get_data()
    if df is None or df.shape[0] == 0:
        st.warning("No files were uploaded, Please Upload the CSV files")
    else:
        reviews = bulk_files_analysis(df)
        st.dataframe(reviews, use_container_width=True)







