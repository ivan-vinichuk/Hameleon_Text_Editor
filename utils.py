import tkinter as tk

imgs={}
imgs_2 = {}

class Icons:
    @staticmethod
    def new_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['new'] = tk.PhotoImage(file='icons2/new.png')
        return ims['new']

    @staticmethod
    def open_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['open'] = tk.PhotoImage(file='icons2/open.png')
        return ims['open']

    @staticmethod
    def save_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['save'] = tk.PhotoImage(file='icons2/save.png')
        return ims['save']

    @staticmethod
    def save_as_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['save_as'] = tk.PhotoImage(file='icons2/save_as.png')
        return ims['save_as']

    @staticmethod
    def exit_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['exit'] = tk.PhotoImage(file='icons2/exit.png')
        return ims['exit']

    @staticmethod
    def copy_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['copy'] = tk.PhotoImage(file='icons2/copy.png')
        return ims['copy']

    @staticmethod
    def paste_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['paste'] = tk.PhotoImage(file='icons2/paste.png')
        return ims['paste']

    @staticmethod
    def cut_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['cut'] = tk.PhotoImage(file='icons2/cut.png')
        return ims['cut']

    @staticmethod
    def clear_all_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['clear_all'] = tk.PhotoImage(file='icons2/clear_all.png')
        return ims['clear_all']

    @staticmethod
    def find_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['find'] = tk.PhotoImage(file='icons2/find.png')
        return ims['find']

    @staticmethod
    def tool_bar_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['tool_bar'] = tk.PhotoImage(file='icons2/tool_bar.png')
        return ims['tool_bar']

    @staticmethod
    def status_bar_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['status_bar'] = tk.PhotoImage(file='icons2/status_bar.png')
        return ims['status_bar']

    @staticmethod
    def light_default_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['light_default'] = tk.PhotoImage(file='icons2/light_default.png')
        return ims['light_default']

    @staticmethod
    def light_plus_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['light_plus'] = tk.PhotoImage(file='icons2/light_plus.png')
        return ims['light_plus']

    @staticmethod
    def dark_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['dark'] = tk.PhotoImage(file='icons2/dark.png')
        return ims['dark']

    @staticmethod
    def red_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['red'] = tk.PhotoImage(file='icons2/red.png')
        return ims['red']

    @staticmethod
    def monokai_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['monokai'] = tk.PhotoImage(file='icons2/monokai.png')
        return ims['monokai']

    @staticmethod
    def night_blue_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['night_blue'] = tk.PhotoImage(file='icons2/night_blue.png')
        return ims['night_blue']

    @staticmethod
    def bold_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['bold'] = tk.PhotoImage(file='icons2/bold.png')
        return ims['bold']

    @staticmethod
    def italic_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['italic'] = tk.PhotoImage(file='icons2/italic.png')
        return ims['italic']

    @staticmethod
    def underline_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['underline'] = tk.PhotoImage(file='icons2/underline.png')
        return ims['underline']

    @staticmethod
    def font_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['font_color'] = tk.PhotoImage(file='icons2/font_color.png')
        return ims['font_color']

    @staticmethod
    def align_left_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['align_left'] = tk.PhotoImage(file='icons2/align_left.png')
        return ims['align_left']

    @staticmethod
    def align_center_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['align_center'] = tk.PhotoImage(file='icons2/align_center.png')
        return ims['align_center']

    @staticmethod
    def align_right_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['align_right'] = tk.PhotoImage(file='icons2/align_right.png')
        return ims['align_right']

    @staticmethod
    def select_icon(popup=False):
        ims = imgs
        if popup:
            ims = imgs_2
        ims['select'] = tk.PhotoImage(file='icons2/select_all.png')
        return ims['select']

    @staticmethod
    def get_color_icons(popup=False):
        return (
            Icons.light_default_icon(popup=False),
            Icons.light_plus_icon(popup=False),
            Icons.dark_icon(popup=False),
            Icons.red_icon(popup=False),
            Icons.monokai_icon(popup=False),
            Icons.night_blue_icon(popup=False)
        )

    @staticmethod
    def about_icon():
        imgs['about'] = tk.PhotoImage(file='icons2/about.png')
        return imgs['about']

    @staticmethod
    def developer_icon():
        imgs['developer'] = tk.PhotoImage(file='icons2/developer.png')
        return imgs['developer']