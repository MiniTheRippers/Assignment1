import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลขด้วย Flet"
    page.window_width = 300
    page.window_height = 450

    result = ft.TextField(value="0", text_align="right", width=280, read_only=True)

    current = {"value": ""}

    def button_click(e):
        data = e.control.data

        if data == "C":
            current["value"] = ""
        elif data == "=":
            try:
                current["value"] = str(eval(current["value"]))
            except:
                current["value"] = "ข้อผิดพลาด"
        else:
            current["value"] += data

        result.value = current["value"] if current["value"] else "0"
        page.update()

    def create_button(label):
        return ft.ElevatedButton(
            text=label,
            width=60,
            height=60,
            data=label,
            on_click=button_click
        )
    
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"]
    ]

    rows = []
    for row in buttons:
        rows.append(ft.Row([create_button(lbl) for lbl in row], alignment="center"))

    page.add(
        ft.Row([result], alignment="center"),
        *rows
    )

ft.app(target=main)
