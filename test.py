import streamlit as st
import os
import time
from sentiment_text import sentiment_analysis, recognize_from_audio

# File upload
value = st.file_uploader("Upload a file", type=["mp3","wav"])

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

# When a file is uploaded
if value:
    # Save the uploaded audio
    saved_file_path = save_uploaded_audio(value)
    
    # Retrieve the last uploaded file
    last_uploaded_file = get_last_uploaded_file(FilePath)
    st.write(f"Last uploaded file: {last_uploaded_file}")
    
    # Check if a valid file path is retrieved and play the audio
    if last_uploaded_file:
        # Display audio using the full path to the file
        st.audio(last_uploaded_file, format="audio/mp3" if last_uploaded_file.endswith(".mp3") else "audio/wav")
        # text = recognize_from_audio(last_uploaded_file)
        # # st.write(text)
        # # st.divider()
        # # text = [text]
        
        # sentiment_analysis(text)
