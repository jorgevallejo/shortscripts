#! /usr/bin/env python3

# Jorge Vallejo Ortega - 27/11/2019
# Python 3.6

# mangadex_scp.py - Downloads manga from Mangadex

# It seems that you need to be logged to search.

# From the URL of the main, it is supposed to:
# Get the URL for each volume and chapter
# Download each page
# Save the pages in directories
# Zip directories
# Save the namefiles with .cbr extension


# Example URL:
# https://mangadex.org/search?title=oreimo
# https://mangadex.org/title/274/ore-no-imouto-ga-konna-ni-kawaii-wake-ga-nai


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get name from command line.
    name = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    name = pyperclip.paste()

#print(name)

webbrowser.open('https://mangadex.org/search?title=' + name)
