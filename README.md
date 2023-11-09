# 74cms-weixin-sqli
This script is designed to test for SQL injection vulnerabilities in the 74CMS `weixin.php` file. The vulnerability arises due to the lack of customization of the `libxml_disable_entity_loader` function, allowing XML External Entity (XXE) Injection, leading to SQL injection vulnerabilities.
