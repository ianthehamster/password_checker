# Password Security Check Website

This web application checks if a password has been exposed in a data breach using the Have I Been Pwned API. It securely hashes the password and sends the first five characters of the hash to the API to retrieve a list of suffixes. It then checks if the rest of the hash is in the list to determine if the password has been compromised.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ianthehamster/password_checker.git
   cd password_checker

2. Install the dependencies
   ```bash
   pip install Flask

3. Run the application:
   ```bash
   python app.py

4. Open your web browser and go to http://localhost:5000 to access the application

Usage
1. Enter a password in the input field on the homepage.
2. Click the "Check Password" button.
3. The application will display whether the password has been compromised and how many times it has been seen in data breaches.


Technologies Used
- Flask: Python web framework for the backend server.
- requests: HTTP library for making API requests.
- hashlib: Python library for secure hashing.
- HTML/CSS: Frontend design and structure.


Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.
