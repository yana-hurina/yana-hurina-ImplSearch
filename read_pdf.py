import fitz
import re


class PDFSearcher:
    def __init__(self, filepath, prefix, suffix):
        self.filepath = filepath
        self.prefix = prefix
        self.suffix = suffix

    def search_in_pdf(self, search_dict):
        # Open the PDF file
        pdf = fitz.open(self.filepath)
        found_dict = {}

        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text()

            # Iterate through the dictionary obtained from the Excel file
            for tab_name, cells in search_dict.items():
                for cell_address, cell_data in cells.items():
                    # Define the pattern to match 'name:' followed by 'cell_data' followed by ','
                    pattern = re.escape(self.prefix) + r"\s*" + re.escape(str(cell_data)) + re.escape(self.suffix)

                    # Search for the pattern in the PDF text
                    if re.search(pattern, text, re.IGNORECASE):
                        # If found, add it to the found_dict with page number
                        if tab_name not in found_dict:
                            found_dict[tab_name] = {}
                        found_dict[tab_name][cell_address] = {
                            'Cell_data': cell_data,
                            'Page_number': page_num + 1  # Adding 1 because page_num starts from 0
                        }

        pdf.close()
        return found_dict
