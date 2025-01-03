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
        # filtered_lines.extend(lines[:2])
        filtered_lines.extend(lines[:1])
        
        # Process lines starting from the 3rd line
        #for i in range(2, len(lines) - 1, 2):  # Increment by 2 for metadata and URL pairs
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
output_file = 'lemoTVSports.m3u'  # Path to save the filtered file

# Updated group titles
group_titles = [
    'Sport Cricket', 'IN: Indian South', 'IN: Indian Entertainment',
    'ESPN Events 200 VIP channels', 'USA NFL - Sunday Ticket', 'Sport Cycling',
    'USA Local - MISC', 'BR: Brazil Sports', 'USA Bally Sports', 'DE: Germany Sport',
    'FR: France Sports', 'USA NBA', 'CA: Canada Super Sports',
    'Sport Tennis', 'CA: Canada Sports', 'USA Local - CBS',
     'USA MLB', 'SE: Sweden Sport', 'Sport NCAA Women Basketball',
    'USA NBC Sports', 'Africa Super Sports', 'USA NFL - Sunday Ticket',
    'USA Local - ABC', 'IT: Sky Sports', 'DK: Denmark Sport',
    'USA Local - NBC', '24/7 Sports Replay', 'USA Sports', 'UK: Sport',
    'USA NCAAF', 'CH: Switzerland Sport', 'Latino Sports', 'UK: EPL Games',
    'USA NHL', 'CAR: Caribbean Sport', 'USA Bein Sports', 'Sport Golf',
    'USA Local - FOX', 'Olympics Events 2024', '4K UHD 3840P', '4K RELAX 1920P',
    'US| NBA PACKAGE', 'US| NFL PACKAGE', '|EN| 4K MOVIES', '|EN| NETFLIX', '|EN| TOP SERIES',
    'ASIA | INDIA NEWS', 'UK| NEWS', 'US| NEWS NETWORK'
]

filter_by_group_title_from_url(url, output_file, group_titles)
