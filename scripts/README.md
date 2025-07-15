# Scholar Stats Update Scripts

This directory contains scripts to automatically update hardcoded scholar statistics in `generate.py` with actual values from Google Scholar.

## Files

- `update_scholar_stats.py` - Main script that fetches actual scholar stats and updates generate.py
- `pre-commit` - Pre-commit hook that automatically runs the update

## Setup

1. Ensure you have the required dependencies:
   ```bash
   pip install scholarly PyYAML
   ```
2. Copy the `pre-commit` file to your `.git/hooks` directory:
   ```bash
   cp pre-commit ../.git/hooks/
   ```
3. The pre-commit hook is already set up and will automatically run before each commit.

## Manual Usage

To manually update the scholar stats:

```bash
# From the repository root
python3 scripts/update_scholar_stats.py
```

## How it works

1. The script reads your Google Scholar ID from `cv.yaml`
2. Fetches your current h-index and citation count from Google Scholar
3. Updates the hardcoded `author = {'hindex': xxx, 'citedby': xxx}` line in `generate.py`
4. The pre-commit hook ensures this happens automatically before each commit

## Note

The script only modifies the hardcoded fallback values in the exception handler. The actual logic that fetches scholar stats during resume generation remains unchanged.
