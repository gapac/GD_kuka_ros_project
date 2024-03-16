import tkinter.ttk as ttk
import tkinter as tk


__all__ = ("HintedEntry",)

class HintedEntry(ttk.Entry):
    """
    A hinted tkinter.ttk.Entry.
    The entry accepts the parameter ``hint`` (The hinting text which will be displayed in gray)
    and the original tkinter.ttk.Entry parameters.
    """
    def __init__(self, hint: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hint = hint
        self._set_hint()
        self.bind("<FocusIn>", self._focus_in)
        self.bind("<FocusOut>", self._focus_out)

    def get(self) -> str:
        if str(self["foreground"]) == "gray":
            return ''

        return super().get()

    def insert(self, *args, **kwargs) -> None:
        state = self.cget("state")
        self.config(state="enabled")
        if str(self["foreground"]) == "gray":
            self.delete('0', tk.END)

        _ret = super().insert(*args, **kwargs)
        self["foreground"] = "black"
        self.config(state=state)
        return _ret

    def _set_hint(self):
        self.insert('0', self.hint)
        self["foreground"] = "gray"

    def _focus_in(self, event: tk.Event):
        if str(self["foreground"]) == "gray":
            self["foreground"] = 'black'
            self.delete('0', tk.END)

    def _focus_out(self, event: tk.Event):
        if not super().get():
            self._set_hint()
