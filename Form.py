import flet as ft
import csv
import os

def main(page: ft.Page):
    page.title = "ฟอร์มรับสมัคร"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    name_field = ft.TextField(label="ชื่อ-สกุล", width=300)
    phone_field = ft.TextField(label="เบอร์โทรศัพท์", width=300, keyboard_type=ft.KeyboardType.PHONE)
    team_field = ft.TextField(label="ชื่อทีม", width=300)

    def save_data(e):
        name = name_field.value.strip()
        phone = phone_field.value.strip()
        team = team_field.value.strip()

        if not name or not phone or not team:
            page.snack_bar = ft.SnackBar(ft.Text("กรุณากรอกข้อมูลให้ครบถ้วน", color="white"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        file_name = "สมัคร.csv"
        file_exists = os.path.isfile(file_name)

        with open(file_name, mode="a", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["ชื่อ-สกุล", "เบอร์โทรศัพท์", "ชื่อทีม"])  # เขียนหัวตารางถ้ายังไม่มี
            writer.writerow([name, phone, team])

        name_field.value = ""
        phone_field.value = ""
        team_field.value = ""
        page.snack_bar = ft.SnackBar(ft.Text("บันทึกข้อมูลเรียบร้อยแล้ว", color="white"), bgcolor="green")
        page.snack_bar.open = True
        page.update()

    
    save_button = ft.ElevatedButton("บันทึก", on_click=save_data)


    page.add(
        ft.Column([
            name_field,
            phone_field,
            team_field,
            save_button,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
