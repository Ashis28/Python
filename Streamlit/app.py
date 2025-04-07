import streamlit as st

st.title("Hello My first streamlit line")		#title
st.header("header")								#Header
st.subheader("subheader")
st.text("Text")


st.markdown("### 3#markdown")					#Markdown
st.markdown("## 2#markdown")

st.info("Information")							#Information
st.success("Success")							#Success
st.warning("Warning")							#Warning
st.error("Error!")
st.exception(ZeroDivisionError("Div not possible"))#Exception


st.subheader('Write')							#Write
st.write('range(1,10)')
st.write(range(1,10))
st.write(1+2*6)


st.write('code')								#Code
st.code('for i in range(1,10):'
			'print(i)')
st.write('Aligned cod is :')
st.code('x=10\n'
	 	 'for i in range(x):\n'
	     '\tprint(i)')


st.write('Checkbox')							#Checkbox
st.checkbox('Male')
if(st.checkbox('Adult')):						#Checkbox with validation
	st.write('You are an Adult!')


st.subheader('Radio Buton')						#Radio Button
radioChoises = st.radio('Select genders',('Male','Female','Others'))
if(radioChoises=='Male'):
	st.write('You are a Male')
elif(radioChoises=='Female'):
	st.write('You are a Female')
elif(radioChoises=='Others'):
	st.write('You are Others')


st.subheader('Select box')						#Select Box
selectBox = st.selectbox('Data Science :', ['Data Analysis','Web Scrapping',
		'Machine Learning','Deep Learning','NLP','Computer Vision',
		'Image Processing'])
st.write('You have Selected' , selectBox )


st.subheader('Multiple Selectbox')				#Multiselectbox
multiSelBox = st.multiselect('Data Science :', ['Data Analysis','Web Scrapping',
		'Machine Learning','Deep Learning','NLP','Computer Vision',
		'Image Processing'])
st.write('You have Selected ',multiSelBox)
st.write('You have Selected ',len(multiSelBox),'Courses')

st.subheader('Button')							#Button
if(st.button('Click Here')):
	st.write("Thanks for Clicking")

st.subheader('Slider')							#Slider
vol = st.slider('Select the volume',0,100,step=2)
st.write('Volume is ',vol)

st.subheader('Text input')						#Text-Input
username = st.text_input('username :')
password = st.text_input('password :',type = 'password')

st.write('Welcome ',username,'To streamlit')
st.write('password is :',password)

st.subheader('Text Area')						#Text Area
st.text_area('Write Here')

st.subheader('Input Number')					#Number-Input
st.number_input("Select your age :",17,40)

st.subheader('Input Date')						#Date-Input
st.date_input("Date")

st.subheader('Input Time')						#Time-Input
st.time_input('TIme')