# This file contains code to check status of a website url and get the response and relevant information.

import requests
from requests import Response


def normalise_url(url : str) -> str:
    """Takes a url string (complete or incomplete) and returns a complete url (starting https://)

    Args:
        url (str): website domain name or complete url given by the user.

    Returns:
        str: complete url starting with https://
    """
    
    if url.startswith(("https://", "http://")):
        return url
    else:
        return f"https://{url}"

def check_website(url : str, timeout : int = 10) -> Response | None:
    """Sends a GET request to the given url and returns response from it if possible, otherwise prints the error occured.

    Args:
        url (str): url to which GET request is to be sent.
        timeout (int, optional): time allowed in seconds to get the response. Defaults to 10.

    Returns:
        requests.Response | None: returns requests.Response object if the GET request is sent (no matter the response), otherwise prints the error message and returns None.
    """
    
    try:
        headers : dict[str, str] = {'Accept-Encoding': 'gzip, deflate'}   # To avoid Error: Already at the end of a Zstandard frame.
        response : Response = requests.get(normalise_url(url), timeout=timeout, headers=headers)
        return response
    except Exception as error:
        print(f"\nError: {error}\n")
        return None

def website_diagnostics_display(get_response : Response, display_headers : bool = True) -> None:
    """Takes the requests.Response object and prints its attributes in a readable format.

    Args:
        get_response (requests.Response): Response object passed as the input.
        display_headers (bool, optional): prints header information if set to True, otherwise not. Defaults to True.

    Returns:
        None: everything is printed to the console directly, does not return anything.
    """
    
    print(f"Status Code  : {get_response.status_code} ({get_response.reason})")
    print(f"Elapsed Time : {get_response.elapsed.total_seconds()}")
    print(f"Content-Type : {get_response.headers.get("Content-Type", "")}")
    print(f"Encoding     : {get_response.encoding or "N/A"}")
    
    if display_headers:
        print("Headers      :")
        for header_type, header_value in dict(get_response.headers).items():
              print(f"    # {header_type} : {header_value}")
    
    print("")
    return None


if __name__ == "__main__":
    user_input_url : str = input("\nEnter a Website URL or Domain: ")
    user_input_url_response : None | Response = check_website(user_input_url)
        
    if user_input_url_response != None:
        print(f"\n==== Website Diagnostics for {user_input_url} ====\n")
        website_diagnostics_display(user_input_url_response, display_headers=False)
    else:
        print("Onto sending GET request to your given URL we received the above error.\n")

# Good Work! However, I believe the code lacks some annotation (commenting).