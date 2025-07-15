#!/usr/bin/env python3
"""
Script to update hardcoded scholar stats in generate.py with actual values.
This script is designed to be run as a pre-commit hook.
"""

import re
import sys
import os

try:
    from scholarly import scholarly
except ImportError:
    print("Error: scholarly module not found. Please install it with: pip install scholarly")
    sys.exit(1)

def get_actual_scholar_stats(scholar_id):
    """Fetch actual scholar stats from Google Scholar."""
    try:
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author, sections=['indices'])
        return {
            'hindex': author.get('hindex', 0),
            'citedby': author.get('citedby', 0)
        }
    except Exception as e:
        print(f"Error fetching Google Scholar data for {scholar_id}: {e}")
        return {'hindex': 0, 'citedby': 0}

def extract_scholar_id_from_yaml():
    """Extract scholar ID from cv.yaml file."""
    try:
        import yaml
    except ImportError:
        print("Error: yaml module not found. Please install it with: pip install PyYAML")
        sys.exit(1)
    
    try:
        with open('cv.yaml', 'r') as f:
            data = yaml.safe_load(f)
        return data.get('social', {}).get('google_scholar', '')
    except Exception as e:
        print(f"Error reading cv.yaml: {e}")
        return ''

def update_scholar_stats_in_generate_py(actual_stats):
    """Update the hardcoded scholar stats in generate.py."""
    generate_py_path = 'generate.py'
    
    # Read the file
    with open(generate_py_path, 'r') as f:
        content = f.read()
    
    # Pattern to match the hardcoded author dictionary
    pattern = r"author = \{'hindex': \d+, 'citedby': \d+\}"
    replacement = f"author = {{'hindex': {actual_stats['hindex']}, 'citedby': {actual_stats['citedby']}}}"
    
    # Check if pattern exists
    if not re.search(pattern, content):
        print("Warning: Hardcoded scholar stats pattern not found in generate.py")
        return False
    
    # Replace the pattern
    new_content = re.sub(pattern, replacement, content)
    
    # Write back to file
    with open(generate_py_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated scholar stats in generate.py: h-index={actual_stats['hindex']}, citations={actual_stats['citedby']}")
    return True

def main():
    """Main function to update scholar stats."""
    # Change to the repository root directory
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)
    
    # Extract scholar ID from cv.yaml
    scholar_id = extract_scholar_id_from_yaml()
    if not scholar_id:
        print("Error: Could not extract Google Scholar ID from cv.yaml")
        sys.exit(1)
    
    print(f"Fetching scholar stats for ID: {scholar_id}")
    
    # Get actual scholar stats
    actual_stats = get_actual_scholar_stats(scholar_id)
    
    # Update the generate.py file
    if update_scholar_stats_in_generate_py(actual_stats):
        print("Scholar stats updated successfully!")
    else:
        print("Failed to update scholar stats")
        sys.exit(1)

if __name__ == "__main__":
    main()
