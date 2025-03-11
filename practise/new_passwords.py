import streamlit as st

import random # buildin module

import string # buildin module #specific provide letters and digits

def check_password(length,use_digits,use_special):
    # generate a random password
    characters = string.ascii_letters #provide letters and digits
    if use_digits:
        characters += string.digits  #adds numbers (0-9) to the characters
        if use_special:
            characters += string.punctuation #provide special characters like ! @ # $ % ^ & *
            
            return ''.join(random.choice(characters) for _ in range(length)) #returns a random password of the specified length (_) "KEY WORD" PYTHON KO BATATA HAIN KAY USER KITNAY LETERS DAYNAY WALA HAIN

st.title("🔐 Password Generator")

length =st.slider("Select Password Length", min_value=6, max_value=32,value=12)
use_digits = st.checkbox("Include Digits")        
use_special = st.checkbox("Include Special Characters")
        
if st.button("Generate Password"):
            password = check_password(length,use_digits,use_special)
            st.write(f"Your Strong Password: `{password}`")
            
st.write("---------------------------------------")  
            
st.write("Build with ❤️ by [Zartash Imran](https://github.com/zartasha-khan123/phyton-new-start)")