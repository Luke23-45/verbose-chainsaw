import os
import re

def process_file(md_path, tex_path, chapter_num, chapter_title):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    out.append(f'\\chapter{{{chapter_title}}}\\label{{ch:chap_{chapter_num}}}\n\n')
    
    in_code_block = False
    in_table = False
    table_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip main chapter heading as we already added \chapter
        if stripped.startswith('# CHAPTER'):
            i += 1
            continue
            
        # Code blocks (often used for figure references in our drafts)
        if stripped.startswith('```'):
            if not in_code_block:
                in_code_block = True
                block_content = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    block_content.append(lines[i].strip())
                    i += 1
                i += 1 # skip closing ```
                in_code_block = False
                
                # Check if block describes a figure
                content_str = " ".join(block_content)
                fig_match = re.search(r'Figure\s+(\d+\.\d+):\s*(.*?)(?:\[Refer to:\s*(.*?)\]|$)', content_str)
                if fig_match:
                    fnum = fig_match.group(1)
                    ftitle = fig_match.group(2).strip()
                    fpath = fig_match.group(3).strip() if fig_match.group(3) else ""
                    # Normalize figure path
                    fname = os.path.basename(fpath)
                    
                    # Next lines might have note
                    note_line = ""
                    if i < len(lines) and lines[i].strip().startswith('*Note.*'):
                        note_line = lines[i].strip()[7:].strip()
                        i += 1
                    elif i < len(lines) and lines[i].strip().startswith('*Note:'):
                        note_line = lines[i].strip()[6:].strip()
                        i += 1
                        
                    tex_fig = f"""
\\begin{{figure}}[!htbp]
\\centering
\\includegraphics[width=0.88\\textwidth]{{figures/{fname}}}
\\caption{{{ftitle}}}
\\label{{fig:{fname.split('.')[0]}}}
\\end{{figure}}
"""
                    if note_line:
                        tex_fig += f"""
\\vspace{{-10pt}}
\\begin{{center}}
\\begin{{minipage}}{{0.88\\textwidth}}
\\footnotesize \\textit{{Note.}} {note_line}
\\end{{minipage}}
\\end{{center}}
\\vspace{{6pt}}
"""
                    out.append(tex_fig)
                continue
                
        # Markdown section headings
        if stripped.startswith('#### '):
            title = stripped[5:].strip()
            # remove numbering if present like 4.2.1.1
            title_clean = re.sub(r'^\d+(\.\d+)*\s*', '', title)
            out.append(f'\\subsubsection{{{title_clean}}}\n\n')
            i += 1
            continue
        elif stripped.startswith('### '):
            title = stripped[4:].strip()
            title_clean = re.sub(r'^\d+(\.\d+)*\s*', '', title)
            out.append(f'\\subsection{{{title_clean}}}\n\n')
            i += 1
            continue
        elif stripped.startswith('## '):
            title = stripped[3:].strip()
            title_clean = re.sub(r'^\d+(\.\d+)*\s*', '', title)
            out.append(f'\\section{{{title_clean}}}\n\n')
            i += 1
            continue
            
        # Horizontal rules
        if stripped in ['---', '***', '___']:
            out.append('\n')
            i += 1
            continue
            
        out.append(line)
        i += 1

    content = "".join(out)
    
    # Write initial pass
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {md_path} -> {tex_path}")

print("Converter loaded.")

