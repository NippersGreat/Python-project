import tkinter as tk
from tkinter import ttk

# Функция расчета

def calculate_parameters(diameter, length, explosive_type, plotnost, nedozaryad_perc,nedozaryadmm,massa_boevika):

    # Здесь будут использоваться реальные формулы для расчета
    # Тип боевика Украинит П-СА
    # Маса боевика Украинит П-СА 1 кг
    # Плотность ЭВВ после 20мин, кг/м3 для Украинит П-СА Равна = 1
    # Величина недозаряда после 20мин, % = 11.2 процента

    ukrainit_pp2 = explosive_type = plotnost * 1
    nedozaryadm = nedozaryadmm * 1000
    nedozaryad = length * (nedozaryad_perc / 100)  # используем процент недозаряда
    charge_length_after_20_min = length - nedozaryad  # Вычисление длины заряда после 20 минут
    charge_length_before_gas_generation = charge_length_after_20_min / (1400/ukrainit_pp2) # Пример расчета длины заряда до газогенерации
    total_mass_of_explosive = ((((3.14 * (diameter / 10) * (diameter / 10)) / 4) * 100) / 1000) * 1.4 * (charge_length_before_gas_generation / 1000) - massa_boevika # Пример общей массы заряда
    mass_of_explosive_per_meter = total_mass_of_explosive / (charge_length_after_20_min / 1000)  # Пример расчета массы заряда на 1 п.м.
    mark_on_the_charging_sleeve = length - charge_length_before_gas_generation  # Пример метки на зарядном рукаве
    growth = charge_length_after_20_min - charge_length_before_gas_generation

    return {
        "Общая масса заряда ЭВВ на скважину (кг)": total_mass_of_explosive,
        "Рост скважины (мм)": growth,
        "Недозаряд скважины":  nedozaryad,
        "Величина недозаряда (мм)": nedozaryadm,
        "Длина заряда скважины (мм)": charge_length_after_20_min,
        "Масса заряда на 1 п.м.": mass_of_explosive_per_meter,
        "Длина заряда до газогенерации (мм)": charge_length_before_gas_generation,
        "Метка на зарядном рукаве (мм)": mark_on_the_charging_sleeve
    }

 # ...

from tkinter import messagebox

def display_results(results):

    # Очищаем текстовое поле от прошлых результатов
    results_text.delete('1.0', tk.END)

    # Вставляем новые результаты
    for key, value in results.items():
        results_text.insert(tk.END, f"{key}: {value:.2f}\n")

def on_calculate():

    if not diameter_entry.get():
        messagebox.showerror("Ошибка", "Введите диаметр скважины.")
        return
    if not length_entry.get():
        messagebox.showerror("Ошибка", "Введите длину скважины.")
        return
    if not explosive_type_combobox.get():
        messagebox.showerror("Ошибка", "Выберите тип боевика.")
        return
    if not massa_boevika_entry.get():
        messagebox.showerror("Ошибка", "Введите массу боевика.")
        return
    if not plotnost_entry.get():
        messagebox.showerror("Ошибка", "Выберите плотность.")
        return
    if not nedozaryadmm_entry.get():
        messagebox.showerror("Ошибка", "Введите величину недозаряда.")
        return

    diameter = float(diameter_entry.get())
    length = float(length_entry.get())
    plotnost = float(plotnost_entry.get())
    explosive_type = explosive_type_combobox.get()
    massa_boevika = float(massa_boevika_entry.get())
    nedozaryad_perc = float(nedozaryadmm_entry.get())
    nedozaryadmm = float(nedozaryadmm_entry.get())

    # Выполнение расчетов
    results = calculate_parameters(diameter, length, explosive_type, plotnost, nedozaryad_perc, nedozaryadmm, massa_boevika)
    results = calculate_parameters(diameter, length, explosive_type, plotnost, nedozaryad_perc, nedozaryadmm, massa_boevika)
    results = calculate_parameters(diameter, length, explosive_type, plotnost, nedozaryad_perc, nedozaryadmm, massa_boevika)

    # Вывод результатов в интерфейс
    for key, value in results.items():
        results_text.insert(tk.END, f"{key}: {value:.2f}\n")

    # Обновляем метку с общей массой заряда
    well_length_value_label.config(text=f"{length:.2f} (мм)")  # Длина скважины
    total_mass = calculate_parameters(diameter, length, explosive_type, plotnost, nedozaryad_perc,nedozaryadmm, massa_boevika)
    total_mass_label.config(text=f"Масса заряда ЭВВ на скважину: {results['Общая масса заряда ЭВВ на скважину (кг)']:.2f} (кг)")

    # Получаем результат для недозаряда
    charge_length_before_gas_generation = results.get("Длина заряда до газогенерации (мм)", 0)

    # Обновляем метку для недозаряда с новым значением
    charge_length_before_gas_generation_value_label.config(text=f"{charge_length_before_gas_generation:.2f} (мм)")

    # Получаем результаты для недозаряда и метки на зарядном рукаве
    charge_length_before_gas_generation = results.get("Длина заряда до газогенерации (мм)", 0)
    mark_value_label.config(text=f"{results['Метка на зарядном рукаве (мм)']:.2f} (мм)")
    nedozaryad = results.get("Величина недозаряда (мм)", 0)

    charge_length_before_gas_generation_value_label.config(text=f"{results['Длина заряда до газогенерации (мм)']:.2f} (мм)")
    nedozaryad_value_label.config(text=f"{results['Величина недозаряда (мм)']:.2f} (мм)")

    # Выполняем расчёты и получаем результаты в виде словаря
    results = calculate_parameters(diameter, length, explosive_type, plotnost,nedozaryad_perc,nedozaryadmm,massa_boevika)

    # Отображаем результаты в текстовом поле
    display_results(results)

    # Обновляйте метки соответствующим образом
    plotnost_value_label.config(text=f"{plotnost:.2f} (кг/м^3)")

  #...

# Создаем главное окно
root = tk.Tk()
root.title("Расчет восходящих скважин количества ЭВВ")

# Создаем виджеты для ввода данных
tk.Label(root, text="Выберите тип боевика:").pack()
explosive_type_combobox = ttk.Combobox(root, values=["Украинит П-СА"])
explosive_type_combobox.pack()

tk.Label(root, text="Масса боевика, кг:").pack()
massa_boevika_entry = tk.Entry(root)
massa_boevika_entry.pack()

tk.Label(root, text="Плотность ЭВВ, кг/м^3:").pack() # Метка для плотности
plotnost_entry = tk.Entry(root) # Поле ввода для плотности
plotnost_entry.pack()

tk.Label(root, text="Величина недозаряда, м:").pack()
nedozaryadmm_entry = tk.Entry(root)
nedozaryadmm_entry.pack()

tk.Label(root, text="Диаметр скважины, мм:").pack()
diameter_entry = tk.Entry(root)
diameter_entry.pack()

tk.Label(root, text="Длина скважины, мм:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=on_calculate)
calculate_button.pack(pady=(11, 11))

well_image_label = tk.Label(root, text="Общее изображение скважины",  font=('Arial', 12, 'bold'),fg='black', bg='lightgrey', pady=7)
well_image_label.pack()  # по умолчанию будет расположена по центру под кнопкой

# Рамка и метка для "Длина скважины"
well_length_frame = tk.Frame(root, bg='#fef2ca')  # Цвет фона - светло-желтый
well_length_frame.pack(fill=tk.X, padx=5, pady=0)

well_length_label = tk.Label(well_length_frame, text="Длина скважины", font=('Arial', 10), bg='#fef2ca', fg='black')
well_length_label.pack(side=tk.TOP, fill=tk.X)

well_length_value_label = tk.Label(well_length_frame, text="0", font=('Arial', 18, 'bold'), bg='#fef2ca', fg='black')
well_length_value_label.pack(side=tk.TOP, fill=tk.X)

# Жёлтая рамка для "Длину заряда до газогенерации"
charge_length_before_gas_generation_frame = tk.Frame(root, bg='#F4B084')  # Жёлтый фон
charge_length_before_gas_generation_frame.pack(fill=tk.X, padx=5, pady=0)

charge_length_before_gas_generation_label = tk.Label(charge_length_before_gas_generation_frame, text="Длина заряда до газогенерации", font=('Arial', 10), bg='#F4B084', fg='black')
charge_length_before_gas_generation_label.pack(side=tk.TOP, fill=tk.X)

charge_length_before_gas_generation_value_label = tk.Label(charge_length_before_gas_generation_frame, text="0", font=('Arial', 18, 'bold'), bg='#F4B084', fg='black')
charge_length_before_gas_generation_value_label.pack(side=tk.TOP, fill=tk.X)

# Оранжевая рамка для "Массы заряда ЭВВ на скважину"
total_mass_frame = tk.Frame(root, bg='#F4B084')  # Оранжевый фон
total_mass_frame.pack(fill=tk.X, padx=5, pady=0)

total_mass_label = tk.Label(total_mass_frame, text="0 кг", font=('Arial', 19, 'bold'), bg='#F4B084', fg='black')
total_mass_label.pack(side=tk.TOP, fill=tk.X, expand=True)

# Серая рамка для "Недозаряда"
nedozaryad_frame = tk.Frame(root, bg='#D9D9D9')  # Серый фон
nedozaryad_frame.pack(fill=tk.X, padx=5, pady=0)

nedozaryad_label = tk.Label(nedozaryad_frame, text=" Величина недозаряда", font=('Arial', 10), bg='#D9D9D9', fg='black')
nedozaryad_label.pack(side=tk.TOP, fill=tk.X)

nedozaryad_value_label = tk.Label(nedozaryad_frame, text="0", font=('Arial', 18, 'bold'), bg='#D9D9D9', fg='black')
nedozaryad_value_label.pack(side=tk.TOP, fill=tk.X)

# Жёлтая рамка для "Метки на зарядном рукаве"
mark_frame = tk.Frame(root, bg='#FFD966')  # Жёлтый фон
mark_frame.pack(fill=tk.X, padx=5, pady=0)

mark_label = tk.Label(mark_frame, text="Метка на зарядном рукаве", font=('Arial', 10), bg='#FFD966', fg='black')
mark_label.pack(side=tk.TOP, fill=tk.X)

mark_value_label = tk.Label(mark_frame, text="0", font=('Arial', 18, 'bold'), bg='#FFD966', fg='black')
mark_value_label.pack(side=tk.TOP, fill=tk.X)

# Зеленая рамка для "ЭВВ"
plotnost_frame = tk.Frame(root, bg='#C3FDB8')  # Зеленый фон
plotnost_frame.pack(fill=tk.X, padx=5, pady=0)

plotnost_label = tk.Label(plotnost_frame, text="Плотность ЭВВ", font=('Arial', 10), bg='#C3FDB8', fg='black')
plotnost_label.pack(side=tk.TOP, fill=tk.X)

plotnost_value_label = tk.Label(plotnost_frame, text="0", font=('Arial', 18, 'bold'), bg='#C3FDB8', fg='black')
plotnost_value_label.pack(side=tk.TOP, fill=tk.X)

evv_calculations_label = tk.Label(root, text="Результаты расчетов ЭВВ", font=('Arial', 12, 'bold'), fg='black', bg='#ddd', pady=5)
evv_calculations_label.pack(fill=tk.X, padx=10)

# Вместо прямого размещения results_text используем Frame как контейнер
results_frame = tk.Frame(root)
results_frame.pack(fill=tk.BOTH, expand=True)  # Разрешаем расширение по обоим направлениям

# Создаем Scrollbar внутри Frame
scrollbar = tk.Scrollbar(results_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Место для вывода результатов, теперь с привязкой к Scrollbar
results_text = tk.Text(results_frame, height=10, width=50, yscrollcommand=scrollbar.set)
results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Настраиваем Scrollbar для работы с results_text
scrollbar.config(command=results_text.yview)

# Запуск главного цикла
root.mainloop()
