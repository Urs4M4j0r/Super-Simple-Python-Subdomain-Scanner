#Import statements
import queue
import requests
import threading
import time
import random
import sys
import getopt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#initialize queue for use in threading
q = queue.Queue()

#Set variable to false for now
timed = False

#Get command line argument. the 1: is to drop the first element so the name of the script isn't pulled. ie if you typed 'python3 myscript.py -x' the first element would be myscript.py which we don't need
argumentList = sys.argv[1:]

#Set the available command line arguments. The : signified that it requires an argument itself. ie 'python3 myscript.py -d example' instead of 'python3 myscript.py -d'
options = "htd:"

#Specify the longer versions of the above. Gives the option to use '--help' instead of '-h' for example. The = signify that an argument is required just like : above.
long_options = ["help", "domain=", "time"]

#Define worker function
def worker():
    #Make sure the workers can access the queue by making it a global variable
    global q

    #Create a list of user agents
    userAgents = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')

    while True:
        #Select a random user agent from the above list
        randAgent = random.choice(userAgents)

        #Set the headers to use the selected random user agent
        headers = {'User-Agent': randAgent}

        #grab a url from the queue
        item = q.get()

        #Try to get the url using the defined header. After 3 seconds give up. 
        try:
            check = requests.get(item, headers=headers, timeout=3)
            print(item)
        
        #If an exception occurs, skip that URL and move on
        except:
            pass

        #Tell the queue that all the work is done, allowing the threads to join
        q.task_done()

#Define the run function
def run(domain, timed):

    #Using tkinter, create a windows for wordlist file selection
    Tk().withdraw()

    #Get the path and name of the selected file
    filename = askopenfilename()

    #Print so it's easier to read
    print('Subdomains Discovered')
    print('-' * 50)

    #Get the starting time for use with -t/--time
    start_time = time.time()

    #Make sure the workers can access the queue by making it a global variable
    global q

    #Create 10 threads and have them run the worker function
    for i in range(10):
        threading.Thread(target=worker, daemon=True).start()

    #Open the wordlist file and create the URLs to check and place them in the queue
    with open(filename,'r') as inf:
        for line in inf:
            url = 'https://' + line.strip() + '.' + domain
            q.put(url)

    #Once task_done, continue main execution
    q.join()
    
     #Print so it's easier to read
    print('-' * 50)
    print('\nScan complete')

    #Calculate the execution duration
    duration = time.time() - start_time

    #If the -t/--time arguments were passed, print execution time
    if timed:
        print(str(round(duration,3)) + ' seconds')

#Print the help menu
def printHelp():
    print('Simple Python Subdomain Discovery')
    print('*' * 50)
    print('-h or --help')
    print('help, print this dialog\n')
    print('-t or --time')
    print('Flag to enable tracking runtime\n')
    print('-d or --domain')
    print('The target domain\n')
    print('Example:')
    print('python3 subs.py -d example.com -t')

#If no arguments are passed, print help
if len(argumentList) == 0:
    printHelp()

else:
    try:
        #Using the argumentList, options and long_options set above, get the arguments and their values
        arguments, values = getopt.getopt(argumentList, options, long_options)

        #Loop through the arguments and values
        for currentArgument, currentValue in arguments:

            #If the argument matches, do
            if currentArgument in ('-h','--help'):
                #Print help and exit
                printHelp()
                break
            
            elif currentArgument in ('-d', '--domain'):
                #Retrieve the value passed with -d/--domain for use in script
                domain = currentValue
                
                #Ensure we don't have any unwanted prefixes
                domain = domain.removeprefix('http://')
                domain = domain.removeprefix('https://')
                domain = domain.removeprefix('www.')
               
            elif currentArgument in ('-t', '--time'):
                #Set timed to true so the script will print execution time at the end
                timed = True
                
        #Run the scanner agains the entered domain. Also passing timed so the script knows to print execution time or not
        run(domain, timed)

    #If there's an error with the arguments, print it.
    except getopt.error as err:
        print(str(err))
    
