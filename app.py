from flask import Flask, request, render_template
import requests
import hashlib

app = Flask(__name__)


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the API and try again."
        )
    return response

def get_password_leaks_count(hashes, hash_to_check): 
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes: 
    
    if h == hash_to_check:
      return int(count)
  return 0

def pwned_api_check(password): 
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:] # destructuriing the sha1password
  response = request_api_data(first5_char)
   
  return get_password_leaks_count(response, tail)
  


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/check", methods=["POST"])
def check_password():
    password = request.form["password"]
    count = pwned_api_check(password)
    return render_template("result.html", password=password, count=count)

if __name__ == '__main__':
    app.run(debug=True)