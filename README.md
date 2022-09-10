# Skill_ed
 python programme to extract data , analyse and arrive at a conclusion of essential skills for various job profiles
 the programme employs selenium to scrap data from python and uses plotly to convert it to useful visulization , a basic webapp is developed using the streamlit module

# Data collection
 the data is collected using selenium webcrawler ,it automtes the search bar in linked-in and searches for specific job roles and extract data through x-path method,the   extracted data is converted into .json file type the data pipeline was integrated to clean and extract only necessary information

# Data cleaning 
 removing unnecessary punctuation marks
 splitting the data
 converting data into readable pandas format
 finding most recurred skills using iterators and dictionary
 coverting the json file into excel sheets

# Visualization 
 using pandas and streamlit , excel sheet is formatted and displayed as a bar chart respresenting a specific job role and the most recurrd skills with  plotly
 streamlit enables the multi-selection of various job roles
