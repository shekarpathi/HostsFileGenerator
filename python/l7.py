import requests
from bs4 import BeautifulSoup
import html
from datetime import datetime
import random
import string


def filter_by_group_title_from_url(url, output_file, group_titles):
    """
    Fetches an M3U file from a URL, filters lines based on 'group-title' values,
    and writes the results to a new file, including the first two lines.

    Parameters:
        url (str): URL to fetch the M3U file from.
        output_file (str): Path to the output filtered M3U file.
        group_titles (list): List of 'group-title' values to filter by.
    """
    try:
        # Fetch the M3U file content
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()

        # Prepare the filtered lines
        filtered_lines = []

        # Copy the first two lines as is
        # filtered_lines.extend(lines[:2])
        filtered_lines.extend(lines[:1])

        # Process lines starting from the 3rd line
        # for i in range(2, len(lines) - 1, 2):  # Increment by 2 for metadata and URL pairs
        for i in range(1, len(lines) - 1, 2):  # Increment by 2 for metadata and URL pairs
            metadata_line = lines[i]
            url_line = lines[i + 1]

            # Check if 'group-title' contains any of the specified group_titles
            if any(f'group-title="{title}"' in metadata_line for title in group_titles):
                filtered_lines.append(metadata_line.strip())
                filtered_lines.append(url_line.strip())

        # Write the filtered lines to the output file
        with open(output_file, 'w') as file:
            file.write('\n'.join(filtered_lines))

        print(f"Filtered lines saved to {output_file}")
    except requests.RequestException as e:
        print(f"Failed to fetch the file: {e}")

def generate_random_email():
    # List of random email providers
    email_providers = ['gmaill.com', 'yahooo.com', 'outloook.com', 'hotmaill.com', 'protonmaill.com', 'iicloud.com']

    # Generate a random username (8-12 characters long, alphanumeric with underscores)
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_letters + string.digits + '_', k=username_length))

    # Ensure username contains at least one number and one underscore
    while not any(char.isdigit() for char in username) or '_' not in username:
        username = ''.join(random.choices(string.ascii_letters + string.digits + '_', k=username_length))

    # Choose a random email provider
    email_provider = random.choice(email_providers)

    # Combine username and email provider
    random_email = f"{username}@{email_provider}"

    return random_email

def getCSRFTokenForLayerseven():
    # URL to send the request to
    url = "https://panel.layerseven.ai/sign-in"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response has cookies and extract the csrftoken
    csrftoken = response.cookies.get("csrftoken")

    # Print the extracted csrftoken
    if csrftoken:
        # print("csrftoken:", csrftoken)
        return csrftoken
    else:
        print("No csrftoken found in the response cookies.")
        return None


# def getnewDuckAddress1():
#     # URL to send the request to
#     url = "https://quack.duckduckgo.com/api/email/addresses"
#     headers = {
#         "Authorization": "Bearer xtnkrtadqkrdaajcunq6pdos8qzrs6j5at8enrdcz0nwbqiwy7ixefnyhv2bct"
#     }
#
#     # Send the POST request
#     response = requests.post(url, headers=headers)
#     # Check if the response is valid
#     if response.status_code == 201:
#         response_json = response.json()
#         address = response_json.get("address")
#         if address:
#             modified_address = f"{address}@duck.com"
#             print("Modified Address:", modified_address)
#             return modified_address
#         else:
#             print("'address' key not found in the response JSON.")
#             return None
#     else:
#         print("Request failed with status code:", response.status_code)
#         return None

def getMiddlewareToken(csrftoken,email):
    print("csrftoken passed to getMiddlewareToken: " + csrftoken)
    # URL to send the request to
    url = "https://panel.layerseven.ai/sign-up"
    headers = {
        "Cookie": "csrftoken="+ csrftoken+"; sessionid=""; email="+email+"; picture=None",
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the input field with name 'csrfmiddlewaretoken'
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})

    # Extract the value attribute
    if csrf_token and 'value' in csrf_token.attrs:
        print("csrfmiddlewaretoken:", csrf_token['value'])
        return csrf_token['value']
    else:
        print("csrfmiddlewaretoken not found.")
        return None


def signupForLayerseven(csrftoken, email):
    # URL to send the request to
    url = "https://panel.layerseven.ai/v1/sign-up/"
    headers = {
        "Cookie": "csrftoken="+ csrftoken+"; sessionid=""; email="+email+"; picture=None",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    mwToken = getMiddlewareToken(csrftoken, email)
    print("=-------mwToken------=")
    print(mwToken)

    # duckAddress = getnewDuckAddress()
    duckAddress = email
    body = f"csrfmiddlewaretoken={mwToken}&email={duckAddress}&password=Lg6*%26bdHsKEC%23f5G"
    print("---------------")
    print (body)
    # Send a GET request to the URL
    response = requests.post(url, headers=headers, data=body, allow_redirects=False)
    # print(response.status_code)
    cookies = response.cookies
    for cookie in cookies:
        if (cookie.name == "session_id"):
            print(cookie.name, cookie.value)
            return cookie.value
    # print(response.status_code)
    #
    # # Check the response status and headers
    # print('Status Code:', response.status_code)
    # print('Location Header:', response.headers.get('Location'))


def checkoutLayerseven(csrftoken, session_id, email):
    # URL to send the request to
    url = "https://panel.layerseven.ai/checkout?free-trial=1"
    cookies = {
        'csrftoken': csrftoken, 'session_id': session_id, 'email': email, 'picture': 'None'
    }
    # Send a GET request to the URL
    response = requests.get(url, cookies=cookies, allow_redirects=True)
    cookies = response.cookies
    for cookie in cookies:
        print(cookie.name, cookie.value)
    print(response.status_code)
    html_content = response.text
    # print(html_content)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table with the specific class
    table = soup.find("table", class_="min-w-full divide-y divide-gray-300")

    # Extract the required string from the table
    required_url = None
    if table:
        required_url = table.find(string=lambda text: "http://cf.shark-cdn.me/get.php" in text)

    # Print the extracted URL
    if required_url:
        print("Extracted URL:", required_url)
        return required_url
    else:
        print("No matching URL found in the table.")

    #
    # # Check the response status and headers
    # print('Status Code:', response.status_code)
    # print('Location Header:', response.headers.get('Location'))


if __name__ == "__main__":
    email = generate_random_email()
    csrftoken = getCSRFTokenForLayerseven()
    session_id=signupForLayerseven(csrftoken, email)
    shankarURL=checkoutLayerseven(csrftoken, session_id, email)
    shankar_output_file = 'shan.m3u'  # Path to save the filtered file

    email = generate_random_email()
    csrftoken = getCSRFTokenForLayerseven()
    session_id=signupForLayerseven(csrftoken, email)
    shekarURL=checkoutLayerseven(csrftoken, session_id, email)
    shekar_output_file = 'shek.m3u'  # Path to save the filtered file

    email = generate_random_email()
    csrftoken = getCSRFTokenForLayerseven()
    session_id=signupForLayerseven(csrftoken, email)
    raghuURL=checkoutLayerseven(csrftoken, session_id, email)
    rag_output_file = 'rr.m3u'  # Path to save the filtered file

    email = generate_random_email()
    csrftoken = getCSRFTokenForLayerseven()
    session_id=signupForLayerseven(csrftoken, email)
    rangaURL=checkoutLayerseven(csrftoken, session_id, email)
    rang_output_file = 'rn.m3u'  # Path to save the filtered file

    email = generate_random_email()
    csrftoken = getCSRFTokenForLayerseven()
    session_id=signupForLayerseven(csrftoken, email)
    amitURL=checkoutLayerseven(csrftoken, session_id, email)
    amit_output_file = 'ah.m3u'  # Path to save the filtered file

    print(shankarURL)
    print(shekarURL)
    print(raghuURL)
    print(rangaURL)
    print(amitURL)

    # Open the file and read lines
    with open('unique-group-titles', 'r') as file:
        # Read each line, strip newline characters, and add to the list
        group_titles = [line.strip() for line in file]
    # print(group_titles)

    filter_by_group_title_from_url(shankarURL, shankar_output_file, group_titles)
    filter_by_group_title_from_url(shekarURL, shekar_output_file, group_titles)
    filter_by_group_title_from_url(raghuURL, rag_output_file, group_titles)
    filter_by_group_title_from_url(rangaURL, rang_output_file, group_titles)
    filter_by_group_title_from_url(amitURL, amit_output_file, group_titles)

