import tkinter as tk


class Crossword:
    def __init__(self, window):
        self.window = window
        self.window.geometry('800x800')
        self.window.title('Mazal Tov!')

        self.grid_size = 16
        self.cell_size = 2
        self.last_et_id = 0
        self.entry_texts = {}

        title_frame = tk.Frame(self.window)
        title_frame.grid(row=0, column=0, sticky='nsew')

        cw_frame = tk.Frame(self.window)
        cw_frame.grid(sticky='nsew')

        for i in range(self.grid_size):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)
            cw_frame.grid_rowconfigure(i, weight=1)
            cw_frame.grid_columnconfigure(i, weight=1)

        # self._fill_grid(title_frame, 1, self.grid_size*self.cell_size, color='#2fff4f')
        label = tk.Label(title_frame, text='תשבץ יום הולדת'[-1::-1])
        label.grid(row=0, column=0, columnspan=10)

        self._fill_grid(cw_frame, self.grid_size)
        self._create_word(cw_frame, 0, 0, 15, 'v')
        self._create_word(cw_frame, 1, 1, 5, 'v')
        self._create_word(cw_frame, 3, 0, 5, 'h')
        self._create_word(cw_frame, 8, 3, 8, 'h')

    def _fill_grid(self, frame, height, width=None, color='#000000'):
        if not width:
            width = height
        for i in range(height):
            for j in range(width):
                label = tk.Label(frame, text=' ' * self.cell_size,
                                 background=color)
                label.grid(row=i, column=j)

    def _create_word(self, frame, start_row, start_col, length, dir='h'):
        for i in range(length):
            self.last_et_id += 1
            sv = tk.StringVar()
            self.entry_texts[self.last_et_id] = sv
            entry = tk.Entry(frame, width=self.cell_size, textvariable=sv)
            sv.trace("w", lambda *args: self._validate(sv))
            if dir == 'h':
                entry.grid(row=start_row, column=start_col+i)
            elif dir == 'v':
                entry.grid(row=start_row+i, column=start_col)

    def _validate(self, entry_text):
        self._character_limit(entry_text)
        self._letter_check(entry_text)

    @staticmethod
    def _character_limit(entry_text):
        input = entry_text.get()
        if len(input) > 0:
            entry_text.set(input[-1])

    @staticmethod
    def _letter_check(entry_text):
        input = entry_text.get()
        if not input.isalpha():
            entry_text.set('')


if __name__ == '__main__':
    window = tk.Tk()
    gui = Crossword(window)
    window.mainloop()
