# Copyright (c) 2011, Peter Hajas
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted 
# provided that the following conditions are met:

# Redistributions of source code must retain the above copyright notice, this list of conditions and 
# the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions 
# and the following disclaimer in the documentation and/or other materials provided with the 
# distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER 
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT 
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# spuuf, a little utility to change your MAC address on your Mac.

# Just run "sudo python spuuf.py" and it'll take care of the rest!

# It doesn't totally work. Maybe you can fix it?

import subprocess
import sys
import time # probably the coolest thing I've ever written in software

# Check arguments
if len(sys.argv) < 2:
  print "Please run spuuf with an interface argument, like en1 (most Macs) or en0 (MacBook Air)"
  quit()

# First, disassociate with any current wireless network
subprocess.Popen('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -z', shell=True)

# Next, generate a random MAC address

# Grab the current time
currentTime = time.time()

# Make it into a string
currentTimeStr = str(int(time.time()))

# Add two arbitrary values to the end, no biggie
currentTimeStr+='64'

# Iterate through the string, building our MAC address
MACaddress = ''
for i, c in enumerate(currentTimeStr):
  if (i % 2) == 0:
    MACaddress+=c
  else:
    MACaddress+="%s:" % (c)

# Chop off the last colon. I'm sure there's an easier way than this...
MACaddress = MACaddress[0:17]

# Tell the user what's going on
print 'Setting new MAC address %s' % (MACaddress)

# Set our MAC address to this new value

command = 'sudo ifconfig %s ether %s' % (sys.argv[1], MACaddress)

print command

# Run the command 3 times (it seems to sometimes not stick, potential ifconfig issue?)

subprocess.Popen(command, shell=True)
time.sleep(1)
subprocess.Popen(command, shell=True)
time.sleep(1)
subprocess.Popen(command, shell=True)

