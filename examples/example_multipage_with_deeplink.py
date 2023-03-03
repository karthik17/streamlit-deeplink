import streamlit as st
from st_deeplink import deep_link

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")


def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")
    option = deep_link(st.selectbox)(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'),
        key='contact_method')
    st.write('You selected:', option)


def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")
    options = deep_link(st.multiselect)(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'],
        key='colors')
    st.write('You selected:', options)


page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}


def run():
    selected_page = deep_link(st.sidebar.selectbox)("Select a page", page_names_to_funcs.keys(), key='page')
    page_names_to_funcs[selected_page]()


if __name__ == "__main__":
    if 'is_first_time' not in st.session_state:
        st.session_state['is_first_time'] = True
    try:
        run()
    except Exception as ex:
        raise ex
    finally:
        if st.session_state['is_first_time']:
            st.session_state['is_first_time'] = False
