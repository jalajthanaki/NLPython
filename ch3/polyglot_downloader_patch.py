#!/usr/bin/env python3
"""
Patch script to fix polyglot downloader HTTP 403 error.
This script patches the polyglot library's downloader.py to add User-Agent headers.

Usage:
    python3 polyglot_downloader_patch.py
"""

import os
import sys
import site

def find_polyglot_downloader():
    """Find the polyglot downloader.py file in site-packages."""
    site_packages = site.getsitepackages()
    
    for sp in site_packages:
        downloader_path = os.path.join(sp, 'polyglot', 'downloader.py')
        if os.path.exists(downloader_path):
            return downloader_path
    
    user_site = site.getusersitepackages()
    downloader_path = os.path.join(user_site, 'polyglot', 'downloader.py')
    if os.path.exists(downloader_path):
        return downloader_path
    
    return None

def patch_downloader(downloader_path):
    """Patch the downloader.py file to add User-Agent header."""
    print(f"Patching {downloader_path}...")
    
    with open(downloader_path, 'r') as f:
        content = f.read()
    
    if 'User-Agent' in content and 'Mozilla/5.0' in content:
        print("Already patched! No changes needed.")
        return True
    
    if 'from six.moves.urllib.request import Request' not in content:
        content = content.replace(
            'from six.moves.urllib.request import urlopen',
            'from six.moves.urllib.request import urlopen, Request'
        )
    
    old_code = '        data = urlopen(index_url).read()'
    new_code = '''        req = Request(index_url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()'''
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        
        with open(downloader_path, 'w') as f:
            f.write(content)
        
        print("Successfully patched!")
        return True
    else:
        print("Warning: Could not find the exact code to patch.")
        print("The polyglot library may have been updated.")
        return False

def main():
    print("Polyglot Downloader Patcher")
    print("=" * 50)
    
    downloader_path = find_polyglot_downloader()
    
    if not downloader_path:
        print("Error: Could not find polyglot downloader.py")
        print("Make sure polyglot is installed: pip install polyglot")
        sys.exit(1)
    
    print(f"Found polyglot at: {downloader_path}")
    
    try:
        success = patch_downloader(downloader_path)
        if success:
            print("\nPatch applied successfully!")
            print("You can now use polyglot without HTTP 403 errors.")
        else:
            print("\nPatch failed. Manual intervention may be required.")
            sys.exit(1)
    except Exception as e:
        print(f"\nError during patching: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
