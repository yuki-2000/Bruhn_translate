
from pathlib import Path
import glob


with open("TableOfContents.md", "w", encoding="utf-8", newline='\n') as f:

    f.writelines("# markdown \n\n")    

    base_path = Path(".")   
    for md_file in base_path.rglob("*.md"):
        md_file_string = str(md_file).replace('\\', '/')
        print(md_file_string)
        f.writelines(f"[{md_file_string}]({md_file_string})\n\n")
    
    f.writelines("\n# html \n\n")
        
        
    base_path = Path(".")      
    for html_file in base_path.rglob("*.html"):
        html_file_string = str(html_file).replace('\\', '/')
        print(html_file_string)
        f.writelines(f"[{html_file_string}]({html_file_string})\n\n")
                
        
    
    f.writelines("\n# pdf \n\n")
        
        
    base_path = Path(".")      
    for html_file in base_path.rglob("*.pdf"):
        html_file_string = str(html_file).replace('\\', '/')
        print(html_file_string)
        f.writelines(f"[{html_file_string}]({html_file_string})\n\n")






