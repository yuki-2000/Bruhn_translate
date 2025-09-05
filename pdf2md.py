# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 21:12:58 2025

@author: yuki
"""

import sys
import pypdfium2 as pdfium

#pdf = pdfium.PdfDocument('73 Bruhn analysis and design of flight vehicles.pdf')

#for page in pdf:
#    textpage = page.get_textpage()
#    text = textpage.get_text_range()
#    print(text)
    


#https://qiita.com/ryosuke_ohori/items/a21637537dfdd6d209a9
    
import pymupdf4llm

# PDFからMarkdownを抽出
md_text = pymupdf4llm.to_markdown('73 Bruhn analysis and design of flight vehicles.pdf',
                                  write_images=True,
                                  image_path="images",
                                  )
with open("output.md", "w", encoding="utf-8") as f:
    f.write(md_text)

