'''
    --- Keyword Task Runner ---
    Author: Nicholas Ramsay

    This program runs applescripts via keyword detection.
'''

from subprocess import Popen, PIPE # for running the script

# Get arguments
args = sys.argv[:1]

if len(args) < 1:
    print('Error: Please provide keywords for the relevant script')
    exit()


# Script class
class script:
    def __init__(self, file_name, keywords):
        self.content = open(file_name,"r").read()
        self.keywords = keywords
        self.args = []
    def run(self):
        p = Popen(['osascript', '-'] + self.args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = p.communicate(self.content)
        return str(p.returncode) + stdout + stderr

# Define scripts
scripts = [
    script('brightness-decrement.applescript', ['decrease','decrement','brightness','screen']),
    script('brightness-decrement.applescript', ['decrease','decrement','brightness','screen'])
]

for (arg in args):
    for(script in scripts):
        for(keyword in script.keywords):
            if arg.lower() == keyword

# Run scripts
print(scripts[0].run())
