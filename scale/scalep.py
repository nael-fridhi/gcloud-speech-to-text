import threading
import requests
from colorama import Fore, Style, init
from io import BytesIO
import random
import time
import json

# Initialize colorama
init()

def get_color_code(index):
    # Return ANSI color code for 256 colors (0-255)
    return f"\033[38;5;{index}m"


URL = "https://<serviceName>-<projectHash>-<region>.run.app/transcribe"
#URL = "http://127.0.0.1:8000/transcribe"

FILEs_PATH = ["audio3.wav"]  # Path to audio files

def stream_requests(url, color, path, i):
    start_time = time.time()  # Record start time
    try:
        with open(path, 'rb') as file:
            # Create a POST request with the file
            response = requests.post(url, files={'file': (path, file, 'audio/wav')}, stream=True)
            
            # Check if the request was successful
            response.raise_for_status()

            # Initialize an empty string to store the final transcript
            final_transcript = ""
            # Read and print the response in chunks
            for chunk in response.iter_lines():
                if chunk:
                    # Decode the chunk and try to load it as JSON
                    try:
                        data = json.loads(chunk.decode('utf-8', errors='replace'))
                        # Check if the chunk is a final result
                        if data.get('is_final', False):
                            # Append the transcript to the final transcript
                            final_transcript += data['alternatives'][0]['transcript']
                    except json.JSONDecodeError:
                        # If the chunk is not valid JSON, ignore it
                        pass

            # Print the final transcript after processing all chunks
            print(f"{color}Final transcript for Thread number {i}: {final_transcript}{Style.RESET_ALL}")

    except requests.RequestException as e:
        print(f"{color}Error: {e}{Style.RESET_ALL}")
    finally:
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"{color}Elapsed time for thread number {i} : {elapsed_time:.2f} seconds{Style.RESET_ALL}")

threads = []

# Start a thread for each color
for i in range(100):
    color_code = get_color_code(i)
    thread = threading.Thread(target=stream_requests, args=(URL, color_code, random.choice(FILEs_PATH), i))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
