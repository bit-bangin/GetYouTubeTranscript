from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

# Function to extract video ID from URL
def extract_video_id(url):
    '''
    Function to extract the video ID from a YouTube URL.

    Parameters:
    url (str): The YouTube URL.

    Returns:
    str: The extracted video ID.
    '''

    # Parse the URL
    parsed_url = urlparse(url)

    # Extract the video ID from the 'v' query parameter
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        return video_id[0]
    else:
        return None

# Function to obtain transcript
def get_transcript(video_id):
    '''
    Function to get the transcript of a YouTube video.

    Parameters:
    video_id (str): The YouTube video ID.

    Returns:
    list: The video transcript.
    '''

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to format transcript
def format_transcript(transcript):
    '''
    Function to format the transcript.

    Parameters:
    transcript (list): The transcript data as a list of dictionaries.

    Returns:
    str: The formatted transcript as a single string.
    '''

    # Use a list comprehension to extract the 'text' from each dictionary.
    texts = [segment['text'] for segment in transcript]

    # Join the strings in the texts list into a single string.
    formatted_transcript = ' '.join(texts)

    return formatted_transcript
"""
# Function to output transcript (print)
def output_transcript(transcript):
  '''
  Function to output the transcript to the console.
  
  Parameters:
  transcript (str): The reformatted transcript.
  
  Returns:
  None
  '''
  print(transcript)
 """
# Function to output transcript (save)
def output_transcript(transcript, filename):
  '''
  Function to output the trasncript to a file. 

  Parameters:
  transcript(str): The reformatted transcript.

  Returns:
  None
  '''
  # Open the specified file in write mode ('w').
  # If file already exists - overwrite. If new - create.
  with open(filename, 'w') as file:
    # Write the transcript to the file.
    file.write(transcript)

# Main function
def main(url, filename):
    '''
    Main function to get and output the transcript of a YouTube video.

    Parameters:
    url (str): The YouTube video URL.
    filename (str): The name of the file (within cd) to which to save transcript.

    Returns:
    None
    '''

    # Extract the video ID from the URL.
    video_id = extract_video_id(url)

    # Get the transcript.
    transcript = get_transcript(video_id)

    # Format the transcript.
    formatted_transcript = format_transcript(transcript)

    # Output the transcript.
    output_transcript(formatted_transcript, filename)

# Test the main function
main("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "transcript.txt")
