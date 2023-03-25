import sys
import fitz  # PyMuPDF

# 20230325: text is empty #bug
def extract_highlights(file_path):
    # Open the PDF file
    pdf_document = fitz.open(file_path)
    highlighted_texts = []

    # Iterate through the pages
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

        # Get the annotations on the page
        annotations = page.annots()

        for annot in annotations:
            # Check if the annotation is a highlight
            if annot.type[1] == 'Highlight':

                # Get the highlighted text
                quad_points = annot.vertices
                quad_rects = [fitz.Quad(points).rect for points in zip(*[iter(quad_points)] * 4)]
                highlight = ""
                for rect in quad_rects:
                    words = page.get_textbox(rect)
                    if words:  # if there is text in the rectangle
                        highlight += words + " "

                # Get the highlight color
                color = annot.colors['stroke']

                # Add the text and color to the list
                highlighted_texts.append((highlight.strip(), color))

    # Close the PDF file
    pdf_document.close()

    return highlighted_texts

if __name__ == "__main__":
    file_path = "path.pdf"
    highlights = extract_highlights(file_path)

    for idx, (highlight, color) in enumerate(highlights):
        print(f"{idx + 1}. {highlight} (Color: {color})")