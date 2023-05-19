from django.conf import settings
from django.utils import timezone
from fpdf import FPDF
import os
import uuid


def generate_pdf_check(order):
    # Генерация уникального имени файла
    filename = f"check_{order.pk}.pdf"
    pdf = FPDF()
    pdf.add_page()
    ###
    line_spacing = 0.1
    pdf.set_auto_page_break(auto=True, margin=0.1)
    pdf.add_font('DejaVu', '', 'C:\\Users\\user\\Desktop\\pass\\DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', size=8)
    pdf.cell(200, 10, txt='Общество с ограниченной ответственностью "Сервис по хранению шин"', ln=(0.00000000001), align='C')
    pdf.set_y(pdf.get_y() + line_spacing)
    pdf.cell(200, 10, txt='Бакунинская ул., 81, Москва, 105082', ln=0.00000000001, align='C')
    pdf.set_y(pdf.get_y() + line_spacing)
    pdf.cell(200, 10, txt='ИНН: 7777777777', ln=0.00000000001, align='C')
    # pdf.set_y(pdf.get_y() + line_spacing)
    pdf.cell(200, 10, txt='Место расчётов: https://Tire-Storage.ru/', ln=0.00000000001, align='C')
    pdf.set_font('DejaVu', size=25)
    pdf.cell(200, 10, txt='Кассовый чек', ln=1, align='C')
    pdf.set_font('DejaVu', size=8)
    pdf.cell(200, 10, txt=f'Приход                                                                                                                        {timezone.now().strftime ("%Y - %m - %d, %H:%M")}', ln=1, align='C')
    pdf.cell(200, 10, txt='применяемая система налогообложения                                                                                           ОСН', ln=1, align='C')
    pdf.cell(200, 10, txt=f'Телефон или электронный адрес покупателя                                                                  {order.user.email or order.user.phone_number}', ln=1, align='C')
    pdf.cell(200, 10, txt='признак расчетов в сети Интернет                                                                                                        да', ln=1, align='C')
    pdf.cell(200, 10, txt='сайт ФНС                                                                                                      https://www.nalog.gov.ru/rn77/', ln=1, align='C')
    pdf.cell(200, 10, txt=f'Адрес отправителя                                                                                                    {settings.EMAIL_HOST_USER}',ln=1,align='C')
    pdf.cell(200, 10, txt=f'___________________________________________________________________________________________________________',ln=1,align='C')
    pdf.cell(200, 10, txt=f'Услуга хранения шин на срок - {order.period} мес., размер шин {order.size}, количество шин {order.quantity}                                   1 х { order.price }',ln=1, align='C')
    pdf.cell(200, 10, txt=f'Общая стоимость позиции с учётом скидок и наценок                                                                       {order.price}', ln=1, align='C')
    pdf.cell(200, 10, txt=f'Ставка НДС                                                                                                                                             20%', ln=1, align='C')
    pdf.cell(200, 10, txt=f'Сумма НДС                                                                                                                                              {order.get_nds()}', ln=1,align='C')
    pdf.cell(200, 10, txt=f'___________________________________________________________________________________________________________', ln=1,align='C')
    pdf.cell(200, 10, txt=f'Итог                                                                                                                                                        {order.price}', ln=1, align='C')
    pdf.cell(200, 10, txt='Наличными                                                                                                                                             0.00', ln=1, align='C')
    pdf.cell(200, 10, txt=f'Электронными                                                                                                                                       {order.price}',ln=1, align='C')
    pdf.cell(200, 10, txt='АВАНС                                                                                                                                                      0.00', ln=1, align='C')
    pdf.cell(200, 10, txt='Сумма по чеку в кредит                                                                                                                        0.00', ln=1, align='C')
    pdf.cell(200, 10, txt='Сумма по чеку встроенным представлением                                                                                      0.00', ln=1, align='C')
    pdf.cell(200, 10, txt=f'НДС 20%                                                                                                                                                 {order.get_nds()}', ln=1, align='C')
    pdf.cell(200, 10,txt=f'___________________________________________________________________________________________________________',ln=1, align='C')
    pdf.set_font('DejaVu', size=20)
    pdf.cell(200, 10, txt='СПАСИБО ЗА ПОКУПКУ!', ln=1, align='C')
    filename = "order_{}.pdf".format(order.id)
    # Путь к папке media
    media_root = settings.MEDIA_ROOT
    # Полный путь к файлу PDF
    file_path = os.path.join(media_root, filename)
    # Сохранение PDF-файла
    pdf.output(file_path)
    return filename
