import streamlit as st
from streamlit_option_menu import option_menu

from login import login_page
from signin import signin_page
PAGES = {
    "Login": login_page,
    "Sign Up": signin_page
}

def main():
        with st.sidebar:
            selected = option_menu(
                menu_title="Welcome !",  # required
                options=["Login", "Create Account",], 
                icons=["house", "envelope"],
                menu_icon="cast",  # optional
                default_index=0,  # optional
                # orientation="horizontal",

            )
    
        if selected == "Login":
            login_page()
                
        if selected == "Create Account":
            signin_page()
if __name__ == "__main__":
    main()
