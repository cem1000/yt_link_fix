import streamlit as st

def is_short_youtube_url(url):
    return 'youtu.be/' in url

def fix_youtube_url(url):
    if is_short_youtube_url(url):
        video_id = url.split('youtu.be/')[1]
        url = f'https://www.youtube.com/watch?v={video_id}'
    return url

def app():
    # Set page config
    st.set_page_config(page_title='YouTube URL Converter', page_icon=':movie_camera:')
    
    # Add header
    st.title('YouTube URL Converter')
    
    # Add About section
    st.sidebar.title('About')
    st.sidebar.write('This app helps you convert short YouTube URLs to long form URLs. Simply enter a YouTube URL and click the "Convert" button to get the long form URL. If the URL is already in the long form, the app will let you know. Try it out now!')
    
    # Add text input
    st.write('Enter a YouTube URL:')
    url = st.text_input('', '')
    
    # Add convert button
    if st.button('Convert'):
        if url:
            fixed_url = fix_youtube_url(url)
            if fixed_url == url:
                st.write("Looks like your URL is already in the right format, good job! :sunglasses:")
            else:
                st.write(f"Here's the fixed URL:")
                st.write(fixed_url)
        else:
            st.write('Please enter a YouTube URL.')
    
if __name__ == '__main__':
    app()
