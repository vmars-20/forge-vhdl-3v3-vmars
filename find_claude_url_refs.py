#!/usr/bin/env python3
"""
Recursively search for misleading references to 'claude.ai/'
(should be 'claude.ai/code/' for Claude Code Web UI)
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Directories to skip
SKIP_DIRS = {
    '.git', '__pycache__', 'node_modules', '.venv', 'venv',
    '.pytest_cache', '.mypy_cache', 'build', 'dist', '*.egg-info'
}

# File extensions to search
TEXT_EXTENSIONS = {
    '.md', '.txt', '.py', '.sh', '.yaml', '.yml', '.json',
    '.toml', '.rst', '.html', '.xml', '.cfg', '.ini'
}

def should_skip_dir(path: Path) -> bool:
    """Check if directory should be skipped."""
    return any(skip in path.parts for skip in SKIP_DIRS)

def should_search_file(path: Path) -> bool:
    """Check if file should be searched."""
    return path.suffix in TEXT_EXTENSIONS or path.name in ['LICENSE', 'README']

def search_file(file_path: Path) -> list[tuple[int, str]]:
    """
    Search file for misleading claude.ai/ references.
    Returns list of (line_number, line_content) tuples.
    """
    matches = []

    # Pattern to find claude.ai URLs that DON'T have /code/
    # Matches: https://claude.ai/ or http://claude.ai/ or just claude.ai/
    # But NOT: https://claude.ai/code/
    pattern = re.compile(r'(https?://)?claude\.ai/(?!code/)')

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, start=1):
                if pattern.search(line):
                    matches.append((line_num, line.rstrip()))
    except Exception as e:
        print(f"⚠️  Error reading {file_path}: {e}")

    return matches

def main():
    """Main search function."""
    repo_root = Path(__file__).parent
    results = defaultdict(list)

    print("🔍 Searching for misleading 'claude.ai/' references...")
    print("    (Should be 'claude.ai/code/' for Claude Code Web UI)")
    print()

    # Walk through all files
    for file_path in repo_root.rglob('*'):
        # Skip directories and unwanted files
        if file_path.is_dir() or should_skip_dir(file_path) or not should_search_file(file_path):
            continue

        # Search file
        matches = search_file(file_path)
        if matches:
            rel_path = file_path.relative_to(repo_root)
            results[rel_path] = matches

    # Print results
    if not results:
        print("✅ No misleading 'claude.ai/' references found!")
        return

    print(f"❌ Found {len(results)} file(s) with misleading references:\n")

    total_matches = 0
    for file_path in sorted(results.keys()):
        matches = results[file_path]
        total_matches += len(matches)

        print(f"📄 {file_path}")
        for line_num, line in matches:
            print(f"   Line {line_num:4d}: {line}")
        print()

    print("━" * 80)
    print(f"📊 Summary: {total_matches} match(es) in {len(results)} file(s)")
    print()
    print("💡 Recommendation:")
    print("   Replace 'https://claude.ai/' with 'https://claude.ai/code/'")
    print("   for Claude Code Web UI references")

if __name__ == '__main__':
    main()
