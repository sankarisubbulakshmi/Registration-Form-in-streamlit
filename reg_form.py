import streamlit as st
import pandas as pd
import sqlite3

def insert_sql():
    conn = sqlite3.connect("registerform.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registration_table (
        Name TEXT,
        Email TEXT,
        Password TEXT,
        City TEXT,
        State TEXT
    )
    ''')
    cursor.execute('''
    SELECT * FROM registration_table WHERE Email = ?
    ''', (data["Email"],))
    existing_record = cursor.fetchone()

    if existing_record is None:
        # Insert the record if it does not exist
        cursor.execute('''
        INSERT INTO registration_table (Name, Email, Password, City, State)
        VALUES (?, ?, ?, ?, ?)
        ''', (data["Name"], data["Email"], data["Password"], data["City"], data["State"]))
        conn.commit()
        print("Record inserted.")
    else:
        print("Record already exists.")

    # Close the connection
    conn.close()



st.set_page_config(
    page_title = "Registration_Form",
    page_icon = ":memo:"
)


st.markdown("""
<style>
body {
    background-color: #22a493; /* Change to your desired color */
}
</style>
""", unsafe_allow_html=True)

st.title("Registration Form")

data = {}

name = st.text_input("Name")
if name:
    data["Name"] = name

email = st.text_input("Mail")
if email:
    data["Email"] = email


paswrd = st.text_input("Password")
if paswrd:
    data["Password"] = paswrd

city = st.text_input("City")
if city:
    data["City"] = city

state = st.text_input("State")
if state:
    data["State"] = state

if name and email and paswrd and city and state:
    pass
else:
    st.warning("Please fill all the boxes")

# Create table if it doesn't exist



if st.checkbox("Accknowledgement"):
    if st.button("Register"):
        st.success("successfully registered")
        df = pd.DataFrame([data])
        st.write(df)
        insert_sql()
        st.success("your details successfully stored in sql")
        
     
else:
    if st.button("Register"):
        st.warning("please click the checkbox to register")

