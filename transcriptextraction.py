import requests
from bs4 import BeautifulSoup

url = 'https://lexfridman.com/category/transcripts/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all segments containing speaker name, timestamp, and text
    segment_elements = soup.find_all('div', class_='ts-segment')

    with open('podcast_transcripts.txt', 'w', encoding='utf-8') as file:
        for i, segment in enumerate(segment_elements):
            # Extract speaker name
            speaker_name = segment.find('span', class_='ts-name').get_text(strip=True)

            # Extract timestamp
            timestamp_element = segment.find('span', class_='ts-timestamp')
            timestamp_link = timestamp_element.find('a')
            timestamp_href = timestamp_link['href'] if timestamp_link else None

            # Extract text
            text = segment.find('span', class_='ts-text').get_text(strip=True)

            # Write the extracted information to the file
            file.write(f"Segment {i + 1}: Speaker: {speaker_name}, Timestamp: {timestamp_href}, Text: {text}\n")

    print('Transcripts saved to podcast_transcripts.txt')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
