from docx import Document


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Utente
    user = 'BENFATTO DANIELE'
    fiscal_code = '3yr24793dgq9ei08'
    contact = '0909504877'

    #libro
    title = 'Il silmarillion'
    author = 'J.R.R. Tolkien'
    numInv = '874983749728'
    rack = 'X'
    shelf = 'A'
    position = 3
    coll = f"{rack} | {shelf} | {position}"
    dateIn = '20/20/2020'
    dateEnd = '50/50/2050'



    doc = Document()

    #TITOLO REPORT
    doc.add_heading('                                                     MODULO DI PRESTITO', 1)
    core_properties = doc.core_properties




    par = doc.add_paragraph('\nBIBLIOTECA COMUNALE RECANATI\nCORSO PERSIANI 52 6100 RECANATI\n0719740021 biblioteca@comune.recanati.mc.it')
    #par.add_run('e un pò di grassetto').bold = True

    par = doc.add_paragraph(f"Il lettore  {user}\nCodice:     {fiscal_code}\nRecapiti:  {contact}")

    par = doc.add_paragraph('ottiene in prestito il documento con i seguenti dati di collocazione:')

    par = doc.add_paragraph(f"Titolo:    {title}\nAutore:  {author}\nN. inv:    {numInv}\nColloc:   {coll}\n")
    par.add_run(f"In prestito dal {dateIn} Scade il {dateEnd}").bold = True


    #doc.add_heading('Altro titolo', 1)
    #doc.add_paragraph('Quotazione', 'Intense Quote')

    #par = doc.add_paragraph('E infine una tabella')
    records = (
        ('ORARI DI APERTURA','',''),
        ('', 'Mattina', 'Pomeriggio'),
        ('Lun-Ven', '9:00 - 13:00', '15:30 - 18:30'),
        ('Sabato', '9:00 - 12:00', 'Chiuso')
    )


    table = doc.add_table(1, 3)
    #hdr_cells = table.rows[0].cells
    #[0].text = ''
    #hdr_cells[1].text = 'Mattina'
    #hdr_cells[2].text = 'Pomeriggio'

    for day, hours_M, hours_P in records:
        row_cells = table.add_row().cells
        row_cells[0].text = day
        row_cells[1].text = hours_M
        row_cells[2].text = hours_P

    par = doc.add_paragraph('\n\n\n\n\n                                                                             Firma\n\n\n\n'
                            '                                                    _______________________________________')


    doc.add_page_break()

    doc.save('test.docx')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
