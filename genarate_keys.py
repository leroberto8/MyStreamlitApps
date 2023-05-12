import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["vvvv", "kkkkkk","tttttt"]
usernames= ["PP","TTT","HHH"]
passwords= ["aaaa12","wwwww331", "kkkjkjj"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hasher_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
    
