import flet as ft

def main(page: ft.Page):
    '''es para ponerle titulo a la ventana''' 
    page.title="¿Me perdonas?"  
    '''se hace una aliniacion para decir que este en el centro orizontal y vertical'''
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    '''funcion para poner el color de fondo de la ventana'''
    page.bgcolor="purple"
    '''es una variable para poner el texto en letras negras y su tamaño'''
    lbl1=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="bold"))
    '''bariable para poner la imagen1(la imagen triste xd) lo que esta en parentecis es el tamaño que va ser de la imagen'''
    Img1=ft.Image(src="triste.png",width=200,height=200)
    '''se hace el primer boton opcion si dentro del parentesis dice que va ir de color verde el boton y va tener un tamaño de 100 y 50 '''
    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50)
    '''se hace el segundo boton y es lo mismo que el primero solo que el color es rojo'''
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50)
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        page.update()
    def si(e):
        Img1.src="Feliz.png"
        page.update()
        
    btnSi.on_click=si
    btnNo.on_click=no
    page.add(
        ft.Column(
            [
                lbl1,
                Img1,
                ft.Row([btnSi,btnNo],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
            
        )
    )

ft.app(main)
