import os
import datetime
import locale
import shutil

# Устанавливаем локаль для русского языка
locale.setlocale(locale.LC_TIME, 'ru_RU')

# Задайте путь к папке с файлами-шаблонами
templates_directory = "D:\programming\scriptGinecologiya\Templates"  # Замените на путь к вашей папке с шаблонами

# Устанавливаем начальную дату как сегодня
current_date = datetime.date.today()

# Устанавливаем конечную дату на год вперед
end_date = current_date + datetime.timedelta(days=365)

# Задайте путь к директории, в которой есть папки для месяцев
base_month_directory = "D:\programming\scriptGinecologiya\Month"  # Замените на путь к вашей базовой папке месяцев

# Перебираем месяцы
while current_date <= end_date:
    # Получаем номер месяца (от 1 до 12)
    month_number = current_date.month

    # Получаем название месяца
    month_name = current_date.strftime('%B')
    month_year = current_date.year

    # Формируем путь к папке месяца
    month_directory = os.path.join(base_month_directory, f"{month_year}_{month_number}_{month_name}")

    # Проверяем, существует ли папка месяца, и создаем ее, если она отсутствует
    if not os.path.exists(month_directory):
        os.makedirs(month_directory)

    # Копируем файлы-шаблоны из папки templates и переименовываем их
    for day_number in range(1, 5):
        if current_date.weekday() <= 4:
            day_name = current_date.strftime('%A')
            day_date = current_date.strftime('%d.%m.%Y')
            source_file = os.path.join(templates_directory, f"{current_date.weekday()}.xlsx")
            target_file = os.path.join(month_directory, f"{day_date}-{day_name}.xlsx")
            shutil.copy(source_file, target_file)

    # Переходим к следующему дню
    current_date += datetime.timedelta(days=1)
