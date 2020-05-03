import tkinter as tk


def main():

    window = tk.Tk()

    window.geometry('800x800')

    window.title('Mazal Tov!')

    label = tk.Label(text='Test')

    entry_text = tk.StringVar()
    entry = tk.Entry(width=2, textvariable=entry_text)

    entry_text.trace("w", lambda *args: validate(entry_text))

    label.pack()
    entry.pack()

    window.mainloop()


def validate(entry_text):
    character_limit(entry_text)
    letter_check(entry_text)


def character_limit(entry_text):
    input = entry_text.get()
    if len(input) > 0:
        entry_text.set(input[-1])


def letter_check(entry_text):
    input = entry_text.get()
    if not input.isalpha():
        entry_text.set('')


if __name__ == '__main__':
    main()
