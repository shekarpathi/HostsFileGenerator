import requests

def filter_by_group_title_from_url(url, output_file, group_titles):
    """
    Fetches an M3U file from a URL, filters lines based on 'group-title' values,
    and writes the results to a new file, including the first two lines.

    Parameters:
        url (str): URL to fetch the M3U file from.
        output_file (str): Path to the output filtered M3U file.
        group_titles (list): List of 'group-title' values to filter by.
    """
    try:
        # Fetch the M3U file content
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()

        # Prepare the filtered lines
        filtered_lines = []
        
        # Copy the first two lines as is
        filtered_lines.extend(lines[:1])
        
        # Process lines starting from the 3rd line
        for i in range(1, len(lines) - 1, 2):  # Increment by 2 for metadata and URL pairs
            metadata_line = lines[i]
            url_line = lines[i + 1]
            
            # Check if 'group-title' contains any of the specified group_titles
            if any(f'group-title="{title}"' in metadata_line for title in group_titles):
                filtered_lines.append(metadata_line.strip())
                filtered_lines.append(url_line.strip())
        
        # Write the filtered lines to the output file
        with open(output_file, 'w') as file:
            file.write('\n'.join(filtered_lines))
        
        print(f"Filtered lines saved to {output_file}")
    except requests.RequestException as e:
        print(f"Failed to fetch the file: {e}")

# Example usage
url = 'http://ky-iptv.com:25461/get.php?username=JeganMogan&password=6784352467&type=m3u_plus&output=mpegts'
url = 'http://line.myox.me/get.php?username=9ae0eda6a1&password=478b2eef3ba7&type=m3u_plus&output=ts'
output_file = 'lemoTVAll.m3u'  # Path to save the filtered file

# Updated group titles
group_titles = [
'24/7 MOVIES & SERIES','4K NETFLIX MOVIES' '4K UHD 3840P','APPLE+ MOVIES' 'ASIA | BENGALI/BANGLA','ASIA | BHOJPURI/ODISHA' 'ASIA | ENGLISH','ASIA | INDIA' 'ASIA | INDIA EU','ASIA | INDIA EU HEVC' 'ASIA | INDIA MOVIES','ASIA | INDIA NEWS' 'ASIA | KANNADA','ASIA | MALAYALAM' 'ASIA | MARATHI','ASIA | PAKISTAN' 'ASIA | PREMIUM VIP','ASIA | SPORTS' 'ASIA | TAMIL','ASIA | TELEGU' 'AT| CANAL+ ONLINE SPORT ᴿᴬᵂ','AUSTRALIA' 'BE| SPORTS','BR| ESPN/DISNEY+ SPORT' 'BULGARIA','BY| BELARUS' 'CA| ENGLISH','CA| FRENCH' 'CA| LOCALS','CA| ROGERS ROGERS SUPER SPORTS' 'CA| SPORT','CA| SPORTSNET' 'CZ| SPORTS','DE| BUNDESLIGA' 'DE| BUNDESLIGA REPLAY','|DE| DISNEY+' 'DE| FORMULA 1 PPV','DENMARK SPORT HD & HEVC' 'DE| SKY GO SPORT','DE| SKY MAX PPV 4K' 'DE| SPORT DEUTSCHLAND PPV','DE| SPORT ᴴᴰ ᵃᵐᶻ ᴳᴼᴸᴰ' 'DE| SPORT ᴿᴬᵂ ᵃᵐᶻ ᴳᴼᴸᴰ','DE| SPORTS' 'DE| SPORT TOTAL PPV','DE| WOW SPORT RAW VIP' 'DE| WOW SPORTS VIP','DISNEY+ KIDS' 'DISNEY+ MOVIES','|EN| 4K CLASSIC MOVIES' '|EN| 4K MOVIES','|EN| 4K SERIES' '|EN| ACTION/THRILLER','|EN| ACTORS & DIRECTORS' '|EN| ADVENTURE MOVIES','|EN| AMAZONE PRIME' '|EN| APPLE TV+','|EN| CBS/PARAMOUNT+' '|EN| COMEDY','|EN| COMEDY SERIES' '|EN| DISNEY+','|EN| DISNEY+ SERIES' '|EN| DOCUMENTARIES','|EN| DOCUMENTARY' '|EN| DRAMA/COMEDY','|EN| DRAMA/CRIME' '|EN| ENGLISH SERIES','|EN| HBO MAX' '|EN| HULU','|EN| HULU/FX/FOX/ABC' '|EN| KOREAN DRAMA','|EN| LATEST RELEASES' '|EN| MUSIC/CONCERTS','|EN| NBC/PEACOCK' '|EN| NETFLIX','|EN| MUSIC/CONCERTS' '|EN| NETFLIX KIDS','|EN| NEW RELEASED' '|EN| MUSIC/CONCERTS','|EN| PIXAR MOVIES' '|EN| STAND-UP COMEDY','|EN| TURKISH SERIES SUB' '|EN| TV MOVIES','|EN| UK MOVIES' '|EN| UK SERIES','|FI| FINLAND' 'FINLAND','FR| EUROSPORTS' 'FR| SPORTS HD','|IN| HINDI 2019/2020' '|IN| HINDI CLASSIC','|IN| HINDI MOVIES 4K' '|IN| HINDI MOVIES COLLECTION','|IN| HINDI TV SHOWS' '|IN| KANNADA MOVIES','|IN| MAHARATI TV SHOWS' '|IN| MARATHI MOVIES','|IN| TAMIL CLASSIC' '|IN| TAMIL DUBBED','|IN| TAMIL MOVIES' 'IT| FORMULA 1 / MOTOGP','IT| NOW SPORT ᴴᴰ' 'IT| NOW SPORT ᴿᴬᵂ','IT| SKYGO SPORTS' 'IT| SPORT','JAPAN' 'LAT| PANAMA','LAT| PELICULA' 'LAT| PERU','LAT| PUERTO RICO' 'LAT| R. DOMINICANA','LAT| URUGUAY' 'LAT| VENEZUELA','LATVIA' 'LITHUANIA','MACEDONIA' 'MALAYSIA','MALTA' 'MONTENEGRO','NEPAL' 'NL| CANAL+ ONLINE SPORT ᴿᴬᵂ','NL| ESPN PPV' 'NORWAY SPORT HD & HEVC','NZ| NEW ZEALAND' 'NZ| SKY SPORTS NZ','|PH| CLASSIC' '|PH| COMEDY','|PH| COMIC STAND UP' '|PH| DOCUMENTARY','|PH| DRAMA' '|PH| HORROR','PHILIPPINES' '|PH| NEW RELEASED','|PH| PHILIPPINES SERIES' '|PH| ROMANCE','|PK| NAATS' '|PK| PAKISTANI MOVIES','|PK| PAKISTAN SERIES' 'PL| CANAL+ ONLINE SPORT ᴴᴰ','PL| CANAL+ ONLINE SPORT ᴿᴬᵂ' 'PL| EUROSPORTS','|PL| FILMY 4K' '|PL| SPORT','|RU| RUSSIA SERIES' 'RUSSIA','SERBIA' 'SINGAPORE','SLOVENIA' '|SO| SOMALIA INDIA SERIES','|SO| SOMALI MOVIES' 'SOUTH KOREA','SWEDEN SPORT HD & HEVC' 'SWITZERLAND','TAIWAN' 'THAILAND','TR| TURKIYE' 'UK| 24/7 MOVIES & SERIES','UK| CHAMPIONSHIP' 'UK| EPL PREMIERE LEAGUE','UK| ESPN+ PPV' 'UK| EUROSPORTS','UK| EUROSPORT XTRA' 'UK| FA PLAYER','UK| FORMULA 1 + MOTOGP' 'UK| LA LIGA TEAM PPV','UK| LEAGUE ONE' 'UK| LEAGUE TWO','UK| LIGUE 1 PPV' 'UK| MATCHROOM PPV','UK| NATIONAL LEAGUE' 'UK| NEWS','UK| OTHER SPORTS' 'UKRAINE','UK| RUGBY PPV' 'UK| SCOTTISH FOOTBALL','UK| SERIE A TEAM PPV' 'UK| SKY SPORTS RED BUTTON','UK| SKY SPORT+ VIP' 'UK| SKY STORE','UK| SOCCER REPLAY' 'UK| SPORTS','UK| SPORTS HEVC' 'UK| SUPERCROSS PPV','UK| SUPER LEAGUE+ PPV' 'UK| TNT SPORTS EVENT','UK| WORLD SPORTS' 'US| ABC NETWORK','US| B/R MAX SPORTS PPV' 'US| CBS NETWORK','US| CINEMANIA HOLLYWOOD' 'US| CINEMANIA TV SHOWS','US| CW/MY NETWORK' 'US| DISNEY+ NETWORK','US| ENTERTAINMENT' 'US| ESPN PLAY','US| ESPN PLUS' 'US| FOX NETWORK','US| HULU NETWORK' 'US| MLB PACKAGE','US| MLS NETWORK' 'US| MOVIES NETWORK','US| NAT GEO+ NETWORK' 'US| NBA PACKAGE','US| NBC NETWORK' 'US| NCAAF PACKAGE','US| NETFLIX PPV' 'US| NEWS NETWORK','US| NFL PACKAGE' 'US| NHL PACKAGE','US| PBS NETWORK' 'US| PEACOCK NETWORK','US| PEACOCK PPV' 'US| SPORTS NETWORK','US| STARZ NETWORK' 'US| TELEMUNDO NETWORK','US| TENNIS CHANNEL PLUS' 'US| VIX+ DEPORTES','US| WNBA PACKAGE' 'UZBEKISTAN','VIETNAM' 'VP| VIAPLAY PPV [MULTI AUDIO]','WORLD CRICKET' 'WORLDCUP 2022'
]

filter_by_group_title_from_url(url, output_file, group_titles)
