import base64
import json
import os
import tkinter as tk
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import simpledialog as sd, messagebox as mb
from tkinter import ttk
from tkinter.messagebox import showinfo
import utils

# ------------------------------------------------------------
# ------------------------- Globals --------------------------
# ------------------------------------------------------------

color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}

url = ''
text_changed = False
current_font_family = 'Arial'
current_font_size = 14

password = ''


# ------------------------------------------------------------
# ------------------------- Methods --------------------------
# ------------------------------------------------------------

def c_font(text_edt):
    global current_font_family
    current_font_family = font_family.get()
    text_edt.config(font=(current_font_family, current_font_size))


def c_size(text_edt):
    global current_font_size
    current_font_size = size_var.get()
    text_edt.config(font=(current_font_family, current_font_size))


def c_bold(text_edt):
    text_property = tk.font.Font(font=text_edt['font'])

    if text_property.actual()['weight'] == 'normal':
        text_edt.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_edt.configure(font=(current_font_family, current_font_size, 'normal'))


def c_italic(text_edt):
    text_property = tk.font.Font(font=text_edt['font'])
    if text_property.actual()['slant'] == 'roman':
        text_edt.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_edt.configure(font=(current_font_family, current_font_size, 'normal'))


def u_line(text_edt):
    text_property = tk.font.Font(font=text_edt['font'])

    if text_property.actual()['underline'] == 0:
        text_edt.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_edt.configure(font=(current_font_family, current_font_size, 'normal'))

def ask_save(*args, **kwargs):
    mbox = messagebox.askyesnocancel('Попередження', 'Ви хочете зберегти файл?')
    if mbox:
        save()

    return mbox

def new_file(event=None):
    global url
    global text_changed
    if text_changed:
        asked = ask_save()
        if asked is not None:
            url = ''
            text_editor.delete(1.0, tk.END)
            text_changed = False
    else:
        url = ''
        text_editor.delete(1.0, tk.END)
        text_changed = False


# Функція, яка зберігає заданий текст із заданим паролем по заданому шляху
def save_with_password(text, password, path):
    obj = {'text': text, 'password': password}
    to_save = open(path, 'w')
    data = json.dumps(obj)
    encoded_data = base64.b64encode(data.encode()).decode()
    to_save.write(encoded_data)
    to_save.close()


# Функція, що відкриває запаролений файл
def open_passworded_file(path):
    f = open(path, 'r')
    encoded_data = f.read()
    f.close()

    json_text = base64.b64decode(encoded_data.encode()).decode()
    data = json.loads(json_text)
    password = sd.askstring(title="Ввід даних", prompt="Введіть пароль")
    if password == data['password']:
        return data['text']
    else:
        mb.showerror('Помилка', 'Невірний пароль')


def open_any_file(*args, **kwargs):
    asked = True

    global text_changed

    if text_changed:
        asked = ask_save()

    if asked is not None:
        name = filedialog.askopenfilename(initialdir=os.getcwd(), title='Виберіть Файл',
                                      filetypes=(
                                          ('Текстові файли', '*.txt'), ('Захищений файл', '*.ptxt'),
                                          ('Всі файли', '*.*')))
        if name != '':
         try:
            text_content = open_passworded_file(name)
            if text_content is not None:
                global url
                url = name
                text_editor.delete(1.0, tk.END)
                text_editor.insert(1.0, text_content)
         except:
            f = open(name, 'r')
            text_content = f.read()
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, text_content)


def _save(text, f, new_pass=False):
    content = text
    if f != '':
        p = f
        if p[-5:] == '.ptxt':
            global password
            psword = password
            if (new_pass):
                psword = sd.askstring(title="Ввід даних", prompt="Задайте новий пароль")
            if (psword is not None) & (psword != ''):
                password = psword
                url = p
                save_with_password(content, password, p)
            else:
                mb.showerror()
        else:
            file = open(f, 'w')
            file.write(content)
            file.close()
            url = f


def m_save(text_edt):
    global url
    if url == '':
        m_save_as(text_edt)
    else:
        content = text_edt.get(1.0, tk.END)
        _save(content, url)


def m_save_as(text_edt):
    global url

    content = text_edt.get(1.0, tk.END)
    f = filedialog.asksaveasfilename(defaultextension='.txt',
                                     filetypes=(
                                         ('Текстові файли', '*.txt'), ('Захищений файл', '*.ptxt'),
                                         ('Всі файли', '*.*')))
    _save(content, f, new_pass=True)


def save_as(*args, **kwargs):
    m_save_as(text_editor)


def save(*args, **kwargs):
    m_save(text_editor)


def exit_func(*args, **kwargs):
    global text_changed
    try:
        if text_changed:

            asked = ask_save()

            if asked is not None:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


def change_font(*args, **kwargs):
    c_font(text_editor)


def change_size(*args, **kwargs):
    c_size(text_editor)


def change_bold(*args, **kwargs):
    c_bold(text_editor)


def change_italic(*args, **kwargs):
    c_italic(text_editor)


def underline(*args, **kwargs):
    u_line(text_editor)


def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


def align_left(*args, **kwargs):
    align(text_editor, 'left')


def align_center(*args, **kwargs):
    align(text_editor, 'center')


def align_right(*args, **kwargs):
    align(text_editor, 'right')


def align(text_edt, dir):
    text_content = text_edt.get(1.0, 'end')
    text_edt.tag_config(dir, justify=dir)
    text_edt.delete(1.0, tk.END)
    text_edt.insert(tk.INSERT, text_content, dir)


def _hide_tool_bar(bar, text_edt, s_bar):
    global show_toolbar
    if show_toolbar:
        bar.pack_forget()
        show_toolbar = False

    else:
        text_edt.pack_forget()
        s_bar.pack_forget()
        bar.pack(side=tk.TOP, fill=tk.X)
        text_edt.pack(fill=tk.BOTH, expand=False)
        s_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_toolbar(*args, **kwargs):
    _hide_tool_bar(tool_bar, text_editor, status_bar)


def _hide_status_bar(s_bar):
    global show_statusbar
    if show_statusbar:
        s_bar.pack_forget()
        show_statusbar = False
    else:
        s_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


def hide_statusbar(*args, **kwargs):
    _hide_status_bar(status_bar)


def changed(t_edt, bar):
    global text_changed
    if t_edt.edit_modified():
        text_changed = True
        words = len(
            t_edt.get(1.0, 'end-1c').split())
        characters = len(t_edt.get(1.0, 'end-1c'))
        bar.config(text=f' Рядків: {words} Символів : {characters}')
    t_edt.edit_modified(False)


def add_status_bar(app, text_edt):
    s_bar = ttk.Label(app, text='Статус бар')
    s_bar.pack(side=tk.BOTTOM)

    def on_change(*args, **kwargs):
        changed(text_edt, s_bar)

    text_edt.bind('<<Modified>>', on_change)
    return s_bar


def add_text_edit(app):
    text_edt = tk.Text(app)
    text_edt.config(wrap='word', relief=tk.FLAT)

    scroll_bar = tk.Scrollbar(app)
    text_edt.focus_set()
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_bar.config(command=text_edt.yview)
    text_edt.config(yscrollcommand=scroll_bar.set)

    text_edt.configure(font=('Arial', 14))

    edt = tk.Menu(text_edt, tearoff=False)
    add_edit_options(edt, popup=True)
    edt.add_separator()
    add_view_options(edt, popup=True)

    def show_popup(event):
        try:
            edt.tk_popup(event.x_root, event.y_root, 0)
        finally:
            edt.grab_release()

    text_edt.bind('<ButtonRelease-3>', show_popup)
    text_edt.event_add('<<Paste>>','<Control-igrave>')
    return text_edt


def add_toolbar_options(bar):
    bold_btn = ttk.Button(bar, image=utils.Icons.bold_icon())
    bold_btn.grid(row=0, column=2, padx=5)
    bold_btn.configure(command=change_bold)

    italic_btn = ttk.Button(bar, image=utils.Icons.italic_icon())
    italic_btn.grid(row=0, column=3, padx=5)
    italic_btn.configure(command=change_italic)

    underline_btn = ttk.Button(bar, image=utils.Icons.underline_icon())
    underline_btn.grid(row=0, column=4, padx=5)
    underline_btn.configure(command=underline)

    font_color_btn = ttk.Button(bar, image=utils.Icons.font_icon())
    font_color_btn.grid(row=0, column=5, padx=5)
    font_color_btn.configure(command=change_font_color)

    align_left_btn = ttk.Button(bar, image=utils.Icons.align_left_icon())
    align_left_btn.grid(row=0, column=6, padx=5)
    align_left_btn.configure(command=align_left)

    align_center_btn = ttk.Button(bar, image=utils.Icons.align_center_icon())
    align_center_btn.grid(row=0, column=7, padx=5)
    align_center_btn.configure(command=align_center)

    align_right_btn = ttk.Button(bar, image=utils.Icons.align_right_icon())
    align_right_btn.grid(row=0, column=8, padx=5)
    align_right_btn.configure(command=align_right)


def add_tool_bar(app):
    toolbar = ttk.Label(app)
    toolbar.pack(side=tk.TOP, fill=tk.X)

    font_tuple = tk.font.families()

    font_box = ttk.Combobox(toolbar, width=30, textvariable=font_family, state='readonly')
    font_family.set(current_font_family)
    font_box['values'] = font_tuple

    font_box.grid(row=0, column=0, padx=5)

    font_box.bind("<<ComboboxSelected>>", change_font)

    font_size = ttk.Combobox(toolbar, width=14, textvariable=size_var, state='readonly')
    font_size['values'] = tuple(range(8, 80, 2))
    size_var.set(current_font_size)
    font_size.grid(row=0, column=1, padx=5)
    font_size.bind("<<ComboboxSelected>>", change_size)

    add_toolbar_options(toolbar)
    return toolbar


def create_find_dialog(on_find, on_replace):
    dialogue = tk.Toplevel()
    dialogue.geometry('450x250+500+200')
    dialogue.resizable(0, 0)

    find_frame = ttk.LabelFrame(dialogue, text='Знайти/Замінити')
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame, text='Знайти:')
    text_replace_label = ttk.Label(find_frame, text='Замінити:')

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    def find(*args, **kwargs):
        on_find(find_input)

    def replace(*args, **kwargs):
        on_replace(find_input, replace_input)

    find_button = ttk.Button(find_frame, text='Пошук', command=find)
    replace_button = ttk.Button(find_frame, text='Заміна', command=replace)

    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)


def _find_func(text_edt):
    def find(input):
        word = input.get()
        text_edt.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_edt.search(word, start_pos, stopindex=tk.END)
                if (not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_edt.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_edt.tag_config('match', foreground='red', background='')

    def replace(input1, input2):
        word = input1.get()
        replace_text = input2.get()
        content = text_edt.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_edt.delete(1.0, tk.END)
        text_edt.insert(1.0, new_content)

    find_dialogue = create_find_dialog(find, replace)
    find_dialogue.mainloop()


def find_func(*args, **kwargs):
    _find_func(text_editor)


def _change_theme(text_edt):
    choose_theme = theme_choice.get()
    color_tuple = color_dict.get(choose_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_edt.config(background=bg_color, fg=fg_color)


def change_theme(*args, **kwargs):
    _change_theme(text_editor)


def add_file_options(file_menu):
    file_menu.add_command(label='новий', image=utils.Icons.new_icon(), compound=tk.LEFT, accelerator='Ctrl+N',
                          command=new_file)

    file_menu.add_separator()

    file_menu.add_command(label='Відкрити', image=utils.Icons.open_icon(), compound=tk.LEFT, accelerator='Ctrl+O',
                          command=open_any_file)

    file_menu.add_separator()

    file_menu.add_command(label='Зберегти', image=utils.Icons.save_icon(), compound=tk.LEFT, accelerator='Ctrl+S',
                          command=save)
    file_menu.add_command(label='Зберегти Як', image=utils.Icons.save_as_icon(), compound=tk.LEFT,
                          accelerator='Ctrl+Alt+S', command=save_as)

    file_menu.add_separator()

    file_menu.add_command(label='Вийти', image=utils.Icons.exit_icon(), compound=tk.LEFT, accelerator='Ctrl+Q',
                          command=exit_func)


def add_edit_options(edit_menu, popup=False):
    edit_menu.add_command(label='Копіювати', image=utils.Icons.copy_icon(popup=popup), compound=tk.LEFT, accelerator='Ctrl+C',
                          command=lambda: text_editor.event_generate("<<Copy>>"))
    edit_menu.add_command(label='Вставити', image=utils.Icons.paste_icon(popup=popup), compound=tk.LEFT, accelerator='Ctrl+V',
                          command=lambda: text_editor.event_generate("<<Paste>>"))
    edit_menu.add_command(label='Вирізати', image=utils.Icons.cut_icon(popup=popup), compound=tk.LEFT, accelerator='Ctrl+X',
                          command=lambda: text_editor.event_generate("<<Cut>>"))
    edit_menu.add_command(label='Виділити все', image=utils.Icons.select_icon(popup=popup), compound=tk.LEFT, accelerator='Ctrl+A',
                          command=lambda: text_editor.event_generate("<<SelectAll>>"))

    edit_menu.add_command(label='Видалити Все', image=utils.Icons.clear_all_icon(popup=popup), compound=tk.LEFT,
                          accelerator='Ctrl+ALt+X',
                          command=lambda: text_editor.delete(1.0, tk.END))

    edit_menu.add_command(label='Знайти', image=utils.Icons.find_icon(popup=popup), compound=tk.LEFT, accelerator='Ctrl+F',
                          command=find_func)


def add_view_options(view_menu, popup=False):
    view_menu.add_checkbutton(label='Панель інструментів', onvalue=True, offvalue=0, variable=show_toolbar,
                              image=utils.Icons.tool_bar_icon(popup=popup), compound=tk.LEFT, command=hide_toolbar)
    view_menu.add_checkbutton(label='Рядок стану', onvalue=1, offvalue=False, variable=show_statusbar,
                              image=utils.Icons.status_bar_icon(popup=popup),
                              compound=tk.LEFT, command=hide_statusbar)


def about():
    showinfo("Інформація",
             "Хамелеон\n"
             "Версія 1.1.0\n"
             "Розробка текстового редактора під Windows\n"
             "Вінічук Іван Васильович\n"
             "Група: КІ-406\n"
             "ТК ТНТУ\n"
             "2020"
             )

def developer():
    showinfo("Інформація",
             "З нами можна зв'язатися через\n"
             "Telegram: @ivan_vinichuk\n"
             "Instagram: @ivan_vinichuk")

def add_help_options(help_menu):
    help_menu.add_command(label="Про програму", image=utils.Icons.about_icon(), compound=tk.LEFT,
                          command=about)
    help_menu.add_command(label="Зв'язок з розробником", image=utils.Icons.developer_icon(), compound=tk.LEFT,
                          command=developer)

def create_menu():
    menu = tk.Menu()

    file = tk.Menu(menu, tearoff=False)
    add_file_options(file)

    edit = tk.Menu(menu, tearoff=False)
    add_edit_options(edit)

    view = tk.Menu(menu, tearoff=False)
    add_view_options(view)

    help = tk.Menu(menu, tearoff=False)
    add_help_options(help)

    color_theme = tk.Menu(menu, tearoff=False)

    count = 0
    for i in color_dict:
        color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,
                                    command=change_theme)
        count += 1

    menu.add_cascade(label='Файл', menu=file)
    menu.add_cascade(label='Редагувати', menu=edit)
    menu.add_cascade(label='Відобразити', menu=view)
    menu.add_cascade(label='Колірна тема', menu=color_theme)
    menu.add_cascade(label='Допомога', menu=help)

    return menu

def on_key_press(event=None):
    if (event.char == '\x0e') & (event.keysym != 'n'):
        new_file()
    elif (event.char == '\x0f') & (event.keysym != 'o'):
        open_any_file()
    elif (event.char == '\x13') & (event.keysym != 's'):
        save()
    elif (event.keycode == 83 ) & (event.keysym != 's') & (event.state==131084):
        save_as()
    elif (event.char == '\x11') & (event.keysym != 'q'):
        exit_func()    
    elif (event.char == '\x03') & (event.keysym != 'c'):
        text_editor.event_generate('<<Copy>>')
    elif (event.char == '\x16') & (event.keysym != 'v'):
        text_editor.event_generate('<<Paste>>')
    elif (event.char == '\x18') & (event.keysym != 'x'):
        text_editor.event_generate('<<Cut>>')
    elif (event.keycode == 65 ) & (event.keysym != 'a') & (event.state==12):
        text_editor.tag_add(tk.SEL, "1.0", tk.END)
    elif (event.keycode == 88 ) & (event.keysym != 'x') & (event.state==131084):
        text_editor.delete(1.0, tk.END)
    elif (event.char == '\x06') & (event.keysym != 'f'):
        find_func()

    

def create_notepad_main_window():
    app = tk.Tk()
    app.geometry('1200x800')
    app.title('Хамелеон')
    
    app.bind('<KeyPress>', on_key_press)
    app.bind("<Control-n>", new_file)
    app.bind("<Control-o>", open_any_file)
    app.bind("<Control-s>", save)
    app.bind("<Control-Alt-s>", save_as)
    app.bind("<Control-q>", exit_func)
    app.bind("<Control-f>", find_func)

    app.protocol("WM_DELETE_WINDOW", exit_func)
    return app


# ------------------------------------------------------------
# -------------------------- Main ----------------------------
# ------------------------------------------------------------

main_application = create_notepad_main_window()

font_family = tk.StringVar()
theme_choice = tk.StringVar()
size_var = tk.IntVar()

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

color_icons = utils.Icons.get_color_icons()

main_menu = create_menu()

tool_bar = add_tool_bar(main_application)

text_editor = add_text_edit(main_application)
status_bar = add_status_bar(main_application, text_editor)
text_editor.pack(fill=tk.BOTH, expand=True)

main_application.config(menu=main_menu)
main_application.mainloop()
