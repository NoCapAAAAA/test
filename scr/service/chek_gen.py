from django.conf import settings
from fpdf import FPDF
import os
import uuid


def generate_pdf_check(order):
    # Генерация уникального имени файла
    filename = f"check_{order.pk}.pdf"
    pdf = FPDF()
    pdf.add_page()
    line_spacing = 1
    pdf.set_auto_page_break(auto=True, margin=5)
    pdf.add_font('DejaVu', '', 'C:\\Users\\user\\Desktop\\pass\\DejaVuSansCondensed.ttf', uni=True)

    pdf.set_font('DejaVu', size=8)
    pdf.cell(200, 10, txt='Общество с ограниченной ответственностью "Сервис по хранению шин"', ln=1, align='C')
    pdf.set_y(pdf.get_y() + line_spacing)
    pdf.cell(200, 10, txt='Бакунинская ул., 81, Москва, 105082', ln=1, align='C')
    pdf.set_y(pdf.get_y() + line_spacing)
    pdf.cell(200, 10, txt='ИНН: 7777777777', ln=1, align='C')
    pdf.set_y(pdf.get_y() + line_spacing)
    pdf.cell(200, 10, txt='Место расчётов: https://Tire-Storage.ru/', ln=1, align='C')
    pdf.set_font('DejaVu', size=25)
    pdf.cell(200, 10, txt='Кассовый чек', ln=1, align='C')
    pdf.set_font('DejaVu', size=8)
    pdf.cell(200, 10, txt='Приход               18 мая 2023 г. 20:43', ln=1, align='C')
    pdf.cell(200, 10, txt='Общество с ограниченной ответственностью "Сервис по хранению шин"', ln=1, align='C')

    filename = "order_{}.pdf".format(order.id)

    # Путь к папке media
    media_root = settings.MEDIA_ROOT

    # Полный путь к файлу PDF
    file_path = os.path.join(media_root, filename)

    # Сохранение PDF-файла
    pdf.output(file_path)

    return filename
