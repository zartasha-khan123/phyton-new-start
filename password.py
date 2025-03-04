import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    common_passwords = ["password123", "12345678", "qwerty", "admin", "letmein"]
    
    if password in common_passwords:
        return "❌ Weak Password - Too common! Choose a more unique one."
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "\n".join(feedback) + "\n❌ Weak Password - Improve it using the suggestions above."

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Check your password security and get suggestions to improve it!")

password = st.text_input("Enter your password:", type="password")
if password:
    result = check_password_strength(password)
    st.write(result)

if st.button("🔑 Generate Strong Password"):
    st.success("Suggested Strong Password: " + generate_strong_password())
