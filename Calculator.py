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
        # ตัวเลข
        if label in "0123456789.":
            color = ft.Colors.BLUE_GREY_100
            text_color = ft.Colors.BLACK
        # เครื่องหมาย
        elif label in "+-*/":
            color = ft.Colors.AMBER_300
            text_color = ft.Colors.BLACK
        # =
        elif label == "=":
            color = ft.Colors.GREEN_400
            text_color = ft.Colors.WHITE
        # C
        elif label == "C":
            color = ft.Colors.RED_400
            text_color = ft.Colors.WHITE
        else:
            color = ft.Colors.GREY_300
            text_color = ft.Colors.BLACK

        return ft.ElevatedButton(
            text=label,
            width=60,
            height=60,
            data=label,
            on_click=button_click,
            style=ft.ButtonStyle(
                bgcolor=color,
                color=text_color
            )
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
