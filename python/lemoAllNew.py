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
        filtered_lines.extend(lines[:2])
        
        # Process lines starting from the 3rd line
        for i in range(2, len(lines) - 1, 2):  # Increment by 2 for metadata and URL pairs
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
url = 'http://ky-iptv.com:25461/get.php?username=DonnyNov28&password=7021128702&type=m3u_plus&output=mpegts'
output_file = 'lemoTVAll.m3u'  # Path to save the filtered file

# Updated group titles
group_titles = [
'24/7 Action',
'24/7 Action & Adventure',
'24/7 Adult',
'24/7 Cartoon',
'24/7 Classic Show',
'24/7 Classic Tv Series',
'24/7 Comedy',
'24/7 Cooking',
'24/7 Netflix',
'24/7 News',
'24/7 Reality Shows',
'24/7 Teen Cartoons',
'24/7 Toddler',
'24/7 Tv Series',
'4K Hindi Movies',
'AL: Albania Sport',
'AR: Arab BeIN sports VIP',
'AR: Arab Food Channels',
'AR: Arab News',
'AR: Arabic Sports',
'AR: Iraq',
'AR: Kuwait',
'AR: Lebanon',
'AR: Libya',
'AR: Qatar',
'ARG: Argentina News',
'ARG: Argentina Sports',
'Adults',
'Adults (18+)',
'Adults 24-7',
'Afghanistan',
'Africa Super Sports',
'Australia',
'Austria',
'Azerbaijan',
'BG: Bulgaria Sport',
'BIH: Bosnia Sport',
'BR: Brazil Sports',
'Bollywood',
'CA: Canada Local',
'CA: Canada News',
'CA: Canada Sports',
'CA: Canada Super Sports',
'CAR: Caribbean Sport',
'DE: Germany Sport',
'DK: Denmark Sport',
'ESPN Events 200 VIP channels',
'FR: Amazon Prime',
'FR: France Sports',
'Finland',
'French & English Movies 4K',
'GR: Greece Sports',
'HR: Croatia Sport',
'HU: Hungary Sport',
'Hindi Series',
'IN: India Kannada',
'IN: Indian Entertainment',
'IN: Indian Gujarat',
'IN: Indian Marathi',
'IN: Indian Music',
'IN: Indian Tamil',
'IT: Sky Sports',
'Iran',
'Israel',
'Japan',
'Kazakhistan',
'Korea',
'Latino Sports',
'MX: Mexico Sports',
'Macedonia',
'Malaysia',
'Malta',
'Mongolia',
'Montenegro',
'Movie-Action',
'Movie-Crime',
'Movie-Romance',
'Movies - Kannada',
'Movies - Malayalam',
'Movies - Tamil',
'Movies India',
'Movies-HBO',
'Movies-Netflix',
'Movies-New Releases',
  'NL: Netherland Sport',
'Nepal',
'NetFlix Series (Multi-Lang)',
'PK: Pakistan News',
'PK: Pakistan Sport',
'PL: Poland News',
'PL: Poland Sports',
'PT: Portugal News',
'PT: Portugal Sport',
'Pakistan Movies',
'Pakistani Drama Series',
'Pakistani Series',
'Palestine Series',
'Panama',
'Paraguay',
'Private (18+) Vods',
'Puerto Rico',
'RO: Romania News',
'RO: Romania Sports',
'SE: Sweden Sport',
'Series-Comedy',
'Sport Cricket',
'Sport Cycling',
'Sport NCAA Men Basketball',
'Sport Tennis',
'Tom & Jerry Collection',
'UK: News',
'UK: Sport',
'USA Bally Sports',
'USA Bein Sports',
'USA Local - ABC',
'USA Local - CBS',
'USA Local - FOX',
'USA Local - MISC',
'USA Local - NBC',
'USA Local Channels ( Full List )',
'USA MLB',
'USA NBA',
'USA NBC Sports',
'USA NCAAF',
'USA NFL - Sunday Ticket',
'USA NHL',
'USA News',
'USA Peacock Network',
'USA Sports',
'USA WNBA',
'Ukraine',
'VOD Adults',
'VOD DENMARK',
'VOD Nordic',
'VOD Norway'
]

filter_by_group_title_from_url(url, output_file, group_titles)
