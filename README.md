# Super-Simple-Python-Subdomain-Scanner
A very simple subdomain discovery tool written in python

# What is this?
This project is something I created to experiment with creating a simple subdomain discovery tool. I am often frustrated when trying to learn something new that every example I can find either has a lack of comments, or is very overcomplicated for learning.
<img src=https://media.tenor.com/u8YEMwIfJGMAAAAC/thanos.gif>

# What does it do?
Takes a selected list of subdomains and iterates through it, attempting a connection with each. If the connection is successful, the URL is printed. Includes threading and command line arguments too!

# How can I use it?
To use this project download/clone the repository and install needed dependencies. The table below shows what command line arguments are available.
|Argumnet| Purpose| Example|
|------|----------|--------|----------------------|
|-h/--help | Prints the help menu| python3 SSDSS.py -h |
|-t/--time | Tells the script to print the execution time when finished| python3 SSDSS.py -t -d example.com |
|-d/--domain | REQUIRED - Provides the domain to scan| python3 SSDSS.py -d example.com |

# Requirements
This script was written using Python v3.10.6 and require the following modules to work:
queue

# Disclaimer
The information provided by/with this project is for educational, informational, and entertainment purposes only.

# Donations
BTC - bc1q8wdfa8xvqhgdyudy9hdaqzelps2rarl9vzas4m <br/>
ETH - 0x77f533a7D98B6888f90543959fB5b8Ea3539eE0c <br/>
LTC - LSfCvorJ4FUUKZiKnw1f2xaH2akdUm44AS  <br/>
SHIB (of course)- 0x8126B2E305f46C202cFecD04b673A960142AC26B
