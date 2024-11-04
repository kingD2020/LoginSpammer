## Random Data Submission Script

A Python script to test web forms by automatically submitting random email and password data to a specified URL. It’s perfect for testing form handling, load resilience, or data validation on your own websites.

## Features

Random Email and Password Generation: Generates unique emails and passwords for each submission attempt.
Form Field Detection: Finds all text input fields on the target page and submits gibberish data.
Supports GET and POST: Submits forms using the correct HTTP method as defined on the page.
Mass Submission: Sends up to 100,000 random submissions for stress testing purposes.
Installation

## Prerequisites
Python 3.x
Required Python libraries:
requests
beautifulsoup4
Setup
Clone the repository and install dependencies:


```

git clone https://github.com/yourusername/random-data-submission.git
cd random-data-submission
pip install -r requirements.txt
```

Run the script with the target URL as a command-line argument:

```

python3 login.py <URL>
Replace <URL> with the page URL containing the form you want to test. For example:
```




generate_random_email(): Creates a random email with a randomly selected domain.
generate_random_password(): Generates a password with mixed characters of random length (8–16).
submit_random_data(): Sends random data to detected form fields using POST or GET based on the form’s method.
main(): Entry point for loading the target page and initiating the form submission process.
Important

This script is for educational and authorized testing purposes only. Using it on websites without permission may violate terms of service or legal regulations.

## License

This project is licensed under the MIT License. See LICENSE for more information.
