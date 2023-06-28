# htmlHeadingFormatter
This script takes a plain text file with various headings and subheadings, and generates a corresponding HTML file with formatted headings and navigation links. 

**Author:** Brett Verney</br>
**Version:** v1.0 | 28-06-2023

## Installation

No installation is required for this script. Just ensure you have Python 3.x installed on your machine.

## Usage

Run the script with Python, providing the input and output files as arguments:

```python htmlHeadingFormatter.py -i inputfile.txt -o outputfile.html```


Replace `inputfile.txt` with the name of your input text file, and `outputfile.html` with the name of the output HTML file you want to create.

If you run the script without specifying any arguments, it will default to using `headings-raw.txt` as the input file and `headings-html.txt` as the output file.

Here's an example of how your input file might look:

My Top Level Heading
	My Subheading
	Another Subheading
		A Lower Level Heading
Another Top Level Heading

Each tab character represents a new level in the heading hierarchy.

The script generates an HTML file with corresponding `<h2>`, `<h3>`, etc. tags for each heading, as well as an unordered list for navigation.

## Limitations

The script currently supports only tab-delimited text files as input, and produces an HTML file as output.

It's recommended for use with small to moderate amounts of data. Performance may degrade with very large input files.

## Support

If you encounter any issues with this script, please open an issue on this repository.

## License

This script is available under the [MIT License](https://opensource.org/licenses/MIT).
