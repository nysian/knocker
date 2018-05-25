Knocker.py

Simple port scanner that checks if a port is open or closed on a website
Knocker.py is run from the command line and user options are entered at runtime captured using argv
To run knocker open a command prompt
    Must type py knocker.py ‘website name’
    If only the above is entered the default settings will be used
Randomize ports default is on
Socket time out default is 3 seconds
Number of ports to “knock” on default is 65536

Randomizer (default value is 0)
    Enter 1 after the website name to go one by one through ports
    Ex: py knocker.py google.com 1
Timeout (default value is 3 seconds)
    Enter number of seconds after randomizer
    Ex: py knocker.py google.com 1 0.5
    Ex: py knocker.py google.com 0 0.5
Number of Ports (default value is 65536)
    Enter number of ports after timeout
    Ex: py knocker.py google.com 1 0.5 100
