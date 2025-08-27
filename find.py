# pip install PyMuPDF

import fitz

def search_keyword_in_pdf(file_path, keyword):
    try:
        doc = fitz.open(file_path)
        found = False
        
        for page in doc:
            text = page.get_text()
            if keyword.lower() in text.lower():  # case-insensitive search
                print(f"Keyword '{keyword}' found on page {page.number + 1}")
                found = True
                
        
        if not found:
            print(f"Keyword '{keyword}' not found in the document.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "2nd sem.pdf"
keyword = "2"

search_keyword_in_pdf(file_path, keyword)


# def search_keyword_in_document(file_path, keyword):
#     try:
#         with open(file_path, 'rb') as file:
#             content = file.read()
#             if keyword in content:
#                 print(f"The keyword '{keyword}' was found in the document.")
#             else:
#                 print(f"The keyword '{keyword}' was not found in the document.")
#     except FileNotFoundError:
#         print("The specified file was not found. Please check the file path.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# file_path = "2nd sem.pdf"
# keyword = "Projects"

# search_keyword_in_document(file_path, keyword)

