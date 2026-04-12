import sys
import re

def check_md013(line, line_num):
    """Check MD013: line length > 200 chars (excluding table rows and code blocks)"""
    issues = []
    # Exclude table rows (lines starting with |)
    if line.startswith('|'):
        return issues
    # Check length
    if len(line) > 200:
        issues.append(f"Line {line_num}: MD013 violation - Line length {len(line)} > 200")
    return issues

def check_md022(lines):
    """Check MD022: Headings not surrounded by blank lines"""
    issues = []
    in_code_block = False
    for i, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if line.strip().startswith('#'):
            # Check if previous line exists and is not blank
            if i > 1 and lines[i-2].strip() != '':
                issues.append(f"Line {i}: MD022 violation - Heading not preceded by blank line")
            # Check if next line exists and is not blank
            if i < len(lines) and lines[i].strip() != '':
                issues.append(f"Line {i}: MD022 violation - Heading not followed by blank line")
    return issues

def check_md047(lines):
    """Check MD047: File not ending with a single newline"""
    if not lines:
        return []
    last_line = lines[-1]
    if last_line.strip() != '':
        return [f"End of file: MD047 violation - File should end with a single newline"]
    return []

def check_md060(lines):
    """Check MD060: Table separator must use | --- | style"""
    issues = []
    for i, line in enumerate(lines, 1):
        if '|' in line and re.search(r'\|---+\|', line):
            if not re.search(r'\|\s*---+\s*\|', line):
                issues.append(f"Line {i}: MD060 violation - Table separator must use '| --- |' style, not '|---|'")
    return issues

def main(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        issues = []
        in_code_block = False
        
        # Check MD013
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            if not in_code_block:
                issues.extend(check_md013(line, i))
        
        # Check MD022
        issues.extend(check_md022(lines))
        
        # Check MD047
        issues.extend(check_md047(lines))
        
        # Check MD060
        issues.extend(check_md060(lines))
        
        return issues
    except Exception as e:
        return [f"ERROR: {str(e)}"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_md.py <filepath>")
        sys.exit(1)
    
    issues = main(sys.argv[1])
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("CLEAN")
