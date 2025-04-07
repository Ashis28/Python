import streamlit as st
import pandas as pd

st.subheader("Uploading the file")
df = st.file_uploader('Upload the file here' ,type = ['xlsx','csv'])

if df is not None:
	if df.name.endswith('.csv'):
		data = pd.read_csv(df)
	else:
		data = pd.read_excel(df)

	st.write("### Preview of the file ")
	st.table(data.head())


st.subheader("Dealing with images")
st.image('C:/Users/ashis/OneDrive - Lovely Professional University/Documents/Gfg/Streamlit/files/img.png')

st.subheader("Dealing with image while uploading")
img_file = st.file_uploader('Upload the image here',type = ['png','jpeg'])
if img_file is not None:
	st.image(img_file)


st.subheader("Working with videos")
vid_file = st.file_uploader("Upload video filel :",type = ['mkv','mp4'])
if vid_file is not None:
	st.video(vid_file,start_time = 5)

st.subheader("Working with audios")
audio_file = st.file_uploader("Upload audio file: ",type = ['mp3','wav'])
if audio_file is not None:
	st.audio(audio_file.read())
	