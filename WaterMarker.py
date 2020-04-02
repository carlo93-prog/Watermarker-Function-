# -*- coding: utf-8 -*-

"""
Created on Thu Apr  2 12:11:58 2020

@author: carlo
"""

import PyPDF2


def watermark_pages(input_pdf,watermark,output_pdf):
        
    pdf = PyPDF2.PdfFileReader(input_pdf)
    watermark = PyPDF2.PdfFileReader(watermark)
    output = PyPDF2.PdfFileWriter()
        
    
    for page_number in range( pdf.getNumPages()):
        pages = pdf.getPage(page_number)
        pages.mergePage(watermark.getPage(0))
        output.addPage(pages)
                 
        
    with open(output_pdf, "wb") as final_pdf:
       output.write(final_pdf)
    
    return 'all done'






