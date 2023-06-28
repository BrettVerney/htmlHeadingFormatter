import argparse
import os

def get_tabs(line):
    """Returns the number of leading tabs in a line."""
    return len(line) - len(line.lstrip('\t'))

def get_heading_line(heading, index, level):
    """Formats a heading line."""
    heading_id = f'Heading{index+1}'
    return f'<h{level+2} class="wp-block-heading" id="{heading_id}">{heading}</h{level+2}>\n'

def get_nav_line(heading, index, level):
    """Formats a navigation line."""
    heading_id = f'Heading{index+1}'
    nav_line = '\t' * level + f'<li><a href="#{heading_id}">{heading}</a>\n'
    return nav_line

def generate_html(input_file, output_file):
    """Reads from an input file, generates HTML and writes to an output file."""
    with open(input_file, 'r') as raw_file, open(output_file, 'w') as html_file:
        headings = raw_file.readlines()

        html_file.write('### Navigation Menu ###\n\n<ul>\n')
        level = 0
        for i, line in enumerate(headings):
            line = line.strip()
            current_level = get_tabs(line)
            line = line.lstrip('\t')

            if current_level > level:
                html_file.write('<ul>\n')
            elif current_level < level:
                html_file.write('</ul>\n' * (level - current_level))

            html_file.write(get_nav_line(line, i, current_level))

            level = current_level
        html_file.write('</ul>\n' * (level + 1))

        html_file.write('\n### Headings ###\n\n')

        for i, line in enumerate(headings):
            line = line.strip().lstrip('\t')
            html_file.write(get_heading_line(line, i, get_tabs(headings[i])))

        print(f"Successfully created {len(headings)} headings with navigation links in '{output_file}'")

def main():
    """Main function to parse command line arguments and call the function to generate HTML."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input file name", default="headings-raw.txt")
    parser.add_argument("-o", "--output", help="Output file name", default="headings-html.txt")
    args = parser.parse_args()

    try:
        generate_html(args.input, args.output)
    except IOError as e:
        print(f"Operation failed: {e}")

if __name__ == "__main__":
    main()