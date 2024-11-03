import random
import string
import requests
import sys
from bs4 import BeautifulSoup

def generate_random_email():
    """Generates a random email address."""
    domains = ["example.com", "test.com", "dummy.com", "mail.com"]
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_password():
    """Generates a random password."""
    length = random.randint(8, 16)  # Password length between 8 and 16 characters
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def submit_random_data(endpoint, soup):
    """Submits gibberish to all text input fields found on the page."""
    inputs = soup.find_all('input', type='text')
    
    # Generate random data for each input field
    data = {}
    for input_tag in inputs:
        if input_tag.get('name'):
            # Generate random gibberish for input fields
            gibberish = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
            data[input_tag.get('name')] = gibberish
    
    # If there are no input fields to submit, exit
    if not data:
        print("No text input fields found to submit gibberish.")
        return

    # Determine the method and action for submission
    action = soup.find('form')['action'] if soup.find('form') else endpoint
    method = soup.find('form')['method'] if soup.find('form') else 'GET'

    try:
        # Construct full URL if action is relative
        if not action.startswith(('http://', 'https://')):
            action = endpoint + action

        for _ in range(100000):  # Send 100000 attempts
            # Prepare data for this submission
            submission_data = {k: generate_random_email() if 'email' in k else generate_random_password() for k in data.keys()}
            
            if method.lower() == 'post':
                response = requests.post(action, data=submission_data)
            else:
                response = requests.get(action, params=submission_data)

            if response.status_code in [200, 201]:
                print(f"Submitted gibberish data: {submission_data} - Status: Success")
            else:
                print(f"Attempt Failed - Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Check if the URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 login.py <URL>")
        return

    endpoint = sys.argv[1]
    
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            print("Page loaded successfully.")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Call the function to submit gibberish to any text input fields found
            submit_random_data(endpoint, soup)
        else:
            print(f"Failed to load the page - Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
