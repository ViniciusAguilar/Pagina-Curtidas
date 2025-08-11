import flet as ft
from flet import Control, Colors, Icons

class PostComCurtidas:
    def __init__(self, titulo, descricao, url_imagem, page):
        self.titulo = titulo
        self.page = page
        self.descricao = descricao
        self.url_imagem = url_imagem

        # Variáveis de estado do post (não privadas)
        self.__curtidas_contagem = 0
        self.curtido = False

        # Componentes do Flet
        self.curtidas_texto = ft.Text(f"{self.__curtidas_contagem}", size=20)
        self.icone_curtida = ft.IconButton(
            icon=ft.Icons.FAVORITE_BORDER,
            icon_color=ft.Colors.GREY,
            on_click=self.curtir_post
        )
        
        self.layout = ft.Container( 
            content = ft.Column(
            [
                ft.Text(self.titulo, size=30, weight=ft.FontWeight.BOLD),
                ft.Text(self.descricao, size=20),
                ft.Row([   
                    ft.Image(
                    src=self.url_imagem,
                    width=400,
                    height=400,
                    border_radius=ft.border_radius.all(10),
                )],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
             
                ft.Divider(),
                ft.Row(
                    [self.icone_curtida, self.curtidas_texto],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
            bgcolor="#1e1e1e",
            border_radius=15,
            padding=20,
            margin=10,
            shadow=ft.BoxShadow(blur_radius=10, 
                                color=ft.Colors.BLACK26, 
                                offset=ft.Offset(0, 2)),
            border=ft.border.all(1, Colors.BLACK),
            width=800,
            )
    
    def curtir_post(self, _):
        self.curtido = not self.curtido
        if self.curtido:
            self.__curtidas_contagem += 1
            self.icone_curtida.color = ft.Colors.RED
            self.icone_curtida.icon = ft.Icons.FAVORITE
        else:
            
            self.icone_curtida.color = ft.Colors.GREY
            self.icone_curtida.icon = ft.Icons.FAVORITE_BORDER
        self.curtidas_texto.value = f"{self.__curtidas_contagem}"
        self.page.update()
    
    def get_layout(self):
        return self.layout
    
def main(page: ft.Page):
    page.title = "Sistema de curtidas com classes"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    post1 = PostComCurtidas("Minha viagem", "Céu azul e paisagens de tirar o fôlego!", 
        "https://picsum.photos/400/300?random=1", page)

    post2 = PostComCurtidas("Aventura na montanha", "Explorando trilhas e conquistando picos!",
        "https://picsum.photos/400/300?random=2", page)
        
    page.add(ft.Column([post1.get_layout(), ft.Divider(height=20), post2.get_layout()], 
                       scroll="auto", expand=True, alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER))
    
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)