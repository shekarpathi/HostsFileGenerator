import requests
# git pull --rebase origin main
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
url = 'http://cf.shark-cdn.me/get.php?username=1fd6eb0eb8&password=b2f5bc7f2eb9a14e&type=m3u_plus&output=ts'
output_file = 'ss.m3u'  # Path to save the filtered file

# Open the file and read lines
with open('unique-group-titles', 'r') as file:
    # Read each line, strip newline characters, and add to the list
    group_titles = [line.strip() for line in file]
print(group_titles)

filter_by_group_title_from_url(url, output_file, group_titles)
