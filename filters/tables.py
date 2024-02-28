import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Table):
        # Convert the table to a LaTeX tabular environment wrapped in a table environment
        # This is a simplistic conversion; customization may be required based on your needs
        content = pf.convert_text(pf.stringify(elem), input_format='markdown', output_format='latex')
        latex_table = '\\begin{table}[ht]\n\\centering\n' + content + '\n\\end{table}'
        return pf.RawBlock(latex_table, format='latex')

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()
