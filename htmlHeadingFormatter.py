import argparse

def get_tabs(line):
    return len(line) - len(line.lstrip('\t'))

def process_line(lines, level):
    result = ""
    while lines:
        line = lines[0].strip()
        current_level = get_tabs(lines[0])
        content = line.lstrip('\t')
        if current_level == level:
            result += '\t' * (level + 1) + f'<li><a href="#Heading{len(headings) - len(lines) + 1}">{content}</a>'
            lines.pop(0)
            if lines and get_tabs(lines[0]) > level:
                result += '\n' + '\t' * (level + 2) + '<ul>'
                result += process_line(lines, level + 1).strip()
                result += '\n' + '\t' * (level + 2) + '</ul>'
            result += '</li>\n'
        else:
            break
    return result

def generate_html(input_file, output_file):
    global headings
    with open(input_file, 'r') as raw_file:
        headings = raw_file.readlines()

    navigation_menu = process_line(headings.copy(), 0)

    with open(output_file, 'w') as html_file:
        html_file.write('### Navigation Menu ###\n\n<ul>\n')
        html_file.write(navigation_menu)
        html_file.write('</ul>\n\n### Headings ###\n\n')

        for i, line in enumerate(headings):
            line = line.strip().lstrip('\t')
            level = 2 + get_tabs(headings[i])
            heading_id = f'Heading{i + 1}'
            html_file.write(f'<h{level} class="wp-block-heading" id="{heading_id}">{line}</h{level}>\n')

        print(f"Successfully created {len(headings)} headings with navigation links in '{output_file}'")

# The rest of the code remains the same


def main():
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