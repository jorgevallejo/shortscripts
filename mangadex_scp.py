#! /usr/bin/env python3

# Jorge Vallejo Ortega - 27/11/2019
# Python 3.6

# mangadex_scp.py - Downloads manga from Mangadex

# From the URL of the main, it is supposed to:
# Get the URL for each volume and chapter
# Download each page
# Save the pages in directories
# Zip directories
# Save the namefiles with .cbr extension


# Example URL:
# https://mangadex.org/title/274/ore-no-imouto-ga-konna-ni-kawaii-wake-ga-nai


import webbrowser, sys
if len(sys.argv) > 1:
    #Get address from command line.
    url = ' '.join(sys.argv[1:])

print(url)
# TODO: Get address from clipboard.
