import codecs
import re
from idlelib import replace


def delete_html_tags(html_file, result_file='cleaned.txt'):
    text_free_tags = ""
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.readlines()
        long_line = ""
        terminator = '\r'
        all_str = len(html)
        for line in html:
            if html.index(line) == all_str - 1:
                terminator = ''
            line = line.rstrip().replace('\r',' ')
            if line.startswith("<") and line.endswith(">"):
                text_free_tags += re.sub(r'<[^>]*>', ' ', line) + terminator
            elif line.endswith(">"):
                long_line += line
                text_free_tags += re.sub(r'<[^>]*>', ' ', long_line) + terminator
                long_line = ""
            elif len(line) == 0:
                text_free_tags += '\r'
            else:
                long_line += line

    with open(result_file, 'w', encoding='utf-8') as result_file:
        result_file.write(text_free_tags)
        result_file.close()


delete_html_tags("draft.html", "cleaned.txt")
