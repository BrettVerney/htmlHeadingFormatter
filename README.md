# htmlHeadingFormatter
This Python script aims to alleviate the task of creating HTML navigation and headings for blog writers and web developers. By reading an indented text file representing heading hierarchy, it generates a corresponding text file with HTML-formatted navigation links and headings. This tool is an efficient solution for those managing large, section-heavy web content, reducing manual effort and increasing productivity.

**Author:** Brett Verney</br>
**Version:** v1.0 | 28-06-2023

## Installation

No installation is required for this script. Just ensure you have Python 3.x installed on your machine.

## Usage

Run the script with Python, providing the input and output files as arguments:

```python htmlHeadingFormatter.py -i inputfile.txt -o outputfile.txt```


Replace `inputfile.txt` with the name of your input text file, and `outputfile.txt` with the name of the output HTML file you want to create.

If you run the script without specifying any arguments, it will default to using `headings-raw.txt` as the input file and `headings-html.txt` as the output file.

Here's an example of how your input file might look:

```
My Top Level Heading
	My Subheading
	Another Subheading
		A Lower Level Heading
Another Top Level Heading
```

Each tab character represents a new level in the heading hierarchy.

The script generates a text file with corresponding `<h2>`, `<h3>`, etc. HTML tags for each heading and an unordered list for navigation. An example of an output file:

```
### Navigation Menu ###

<ul>
<li><a href="#Heading1">My Top Level Heading</a>
<li><a href="#Heading2">My Subheading</a>
<li><a href="#Heading3">Another Subheading</a>
<li><a href="#Heading4">A Lower Level Heading</a>
<li><a href="#Heading5">Another Top Level Heading</a>
</ul>

### Headings ###

<h2 class="wp-block-heading" id="Heading1">My Top Level Heading</h2>
<h3 class="wp-block-heading" id="Heading2">My Subheading</h3>
<h3 class="wp-block-heading" id="Heading3">Another Subheading</h3>
<h4 class="wp-block-heading" id="Heading4">A Lower Level Heading</h4>
<h2 class="wp-block-heading" id="Heading5">Another Top Level Heading</h2>
```

Note that I have used a WordPress class "wp-block-heading" to style my headings. Feel free to update this with your own HTML code.

## Limitations

The script currently supports only tab-delimited text files as input and produces a text file as output.

It's recommended for use with small to moderate amounts of data. Performance may degrade with very large input files.

## Support

If you encounter any issues with this script, please open an issue on this repository.

## License

This script is available under the [MIT License](https://opensource.org/licenses/MIT).
