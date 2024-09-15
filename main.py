from flet import *
import flet as ft
import sqlite3 
from tabela import criar_tabela, aulas
from dados_tabela import myatletas,myaula5,myaula6,tb_atleta,tb_aula6,tb_aula5,totalatleta,totalaula5,totalaula6

criar_tabela()
aulas()

conn=sqlite3.connect('db/database.db', check_same_thread=False)

nome = ft.TextField(label="Nome")
idade = ft.TextField(label="Idade")
modalidade=ft.TextField(label="Modalidade")
id_usuario = ft.TextField(label="ID",keyboard_type="number") 


def main(page:Page):
    page.window_width = 350
    page.window_height = 450
    page.window_resizable=False
    page.window_always_on_top = True
    page.scroll = 'auto'
    page.title ='Gestão de Atleta'
        

    def formulario(e):    
        if not nome.value:
            dlg = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text("Nome obrigatório"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            return

        if not idade.value:
            dlg = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text("Idade obrigatória"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            return

        if not modalidade.value:
            dlg = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text("Modalidade obrigatória"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            return
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Atleta Registrado"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            try:
                c=conn.cursor()
                c.execute('''INSERT INTO atleta (nome, idade, modalidade) VALUES (?,?,?)''',(
                nome.value,
                idade.value, 
                modalidade.value))
                
                nome.value=""
                idade.value=""
                modalidade.value=""
                conn.commit()
                page.update
                tb_atleta.rows.clear()
                totalatleta()
                tb_atleta.update()
                page.update()
            
            except Exception as e:
                print('entrou no def savedata(e): mas não saiu', e)
            page.update()

    def envio5hr(e):
        # Validação de entrada
        if not id_usuario.value:
            dlg = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text("ID obrigatorio"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            
        else:
            try:
                entrada = id_usuario.value
            # Converte a entrada para inteiro
                numero = int(entrada)
                # Tenta converter o ID para um inteiro
                id_to_check = numero
                
                # Conecta ao banco de dados e verifica o registro
                conn = sqlite3.connect('db/database.db')
                cursor = conn.cursor()
                
                cursor.execute("SELECT 1 FROM atleta WHERE id = ?", (id_to_check,))
                record = cursor.fetchone()
                conn.commit
                     
                # Exibe o resultado
                if record:
                    dlg = ft.AlertDialog(
                    title=ft.Text("Confirmado!"),
                    content=ft.Text("Aluno Presente "))
                    page.dialog = dlg
                    dlg.open = True
                    page.update()
                    c=conn.cursor()
                    c.execute("UPDATE atleta SET id_usuario = 1 WHERE id=?", (id_to_check,))
                    

                    id_usuario.value=""
                    conn.commit()
                    page.update()
                    tb_aula5.rows.clear()
                    totalaula5()
                    tb_aula5.update()
                    page.update()
            
                else:
                    dlg = ft.AlertDialog(
                    title=ft.Text("Erro!"),
                    content=ft.Text("Aluno Nao Existe "))
                    page.dialog = dlg
                    dlg.open = True
                    page.update()                    
                
              
                conn.close()
            except ValueError:
                # Exibe mensagem de erro se o ID não for um inteiro válido
                dlg = ft.AlertDialog(
                title=ft.Text("Erro!"),
                content=ft.Text("ID incorreto "))
                page.dialog = dlg
                dlg.open = True
            except sqlite3.Error as e:
                # Exibe mensagem de erro em caso de falha no banco de dados
                print(f"An error occurred: {e}")
        
                page.update()
    def envio6hr(e):
        # Validação de entrada
        if not id_usuario.value:
            dlg = ft.AlertDialog(
                title=ft.Text("Aviso"),
                content=ft.Text("ID obrigatorio"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            
        else:
            try:
                entrada = id_usuario.value
            # Converte a entrada para inteiro
                numero = int(entrada)
                # Tenta converter o ID para um inteiro
                id_to_check = numero
                
                # Conecta ao banco de dados e verifica o registro
                conn = sqlite3.connect('db/database.db')
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM atleta WHERE id = ?", (id_to_check,))
                record = cursor.fetchone()
                
                # Exibe o resultado
                if record:
                    dlg = ft.AlertDialog(
                    title=ft.Text("Confirmado!"),
                    content=ft.Text("Aluno Presente "))
                    page.dialog = dlg
                    dlg.open = True
                    page.update()
                    c=conn.cursor()
                    c.execute("UPDATE atleta SET id_usuario = 2 WHERE id=?", (id_to_check,))
                    
                    id_usuario.value=""
                    conn.commit()
                    page.update()
                    tb_aula6.rows.clear()
                    totalaula6()
                    tb_aula6.update()
                    page.update()
         
                else:
                    dlg = ft.AlertDialog(
                    title=ft.Text("Erro!"),
                    content=ft.Text("Aluno Nao Existe "))
                    page.dialog = dlg
                    dlg.open = True
                    page.update()                    
            
                conn.close()
            except ValueError:
                # Exibe mensagem de erro se o ID não for um inteiro válido
                dlg = ft.AlertDialog(
                title=ft.Text("Erro!"),
                content=ft.Text("ID incorreto "))
                page.dialog = dlg
                dlg.open = True
            except sqlite3.Error as e:
                # Exibe mensagem de erro em caso de falha no banco de dados
                print(f"An error occurred: {e}")
        
                page.update()

    def mundanca_rota(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
        
                [
                ft.AppBar(title=Text("Imua Setiba VAA"), bgcolor=colors.SURFACE_VARIANT),
                ft.Row([
                ft.Container(
                    content=ft.Text("Turma 5"),
                    margin=3,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda _: page.go("/turmacinco"),
                ),
                ft.Container(
                    content=ft.Text("Turma 6"),
                    margin=3,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda _: page.go("/turmaseis"),
                ),
                ])
                ],
                ft.Row([
                  ft.Container(
                    content=ft.Text("Adicionar Alteta"),
                    margin=3,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda _: page.go("/novoatleta"),
                ),
                  ft.Container(
                    content=ft.Text("Todos Atleta"),
                    margin=3,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda _: page.go("/todosatletas"),
               
                  )
                ])        
        )
        )
        if page.route == "/novoatleta":
            page.views.append(
                View(
                    "/novoatleta",
                    [
                    AppBar(title=Text("Cadastrar novo atleta"), bgcolor=colors.SURFACE_VARIANT),                    
                    nome,
                    idade,
                    modalidade,
                    ft.ElevatedButton("enviar",on_click=formulario),
                    
                    ],
        
         )  
                                                 
            )

        elif page.route == "/todosatletas":
            page.views.append(
                View(
                    "/todosatletas",
                    [
                        AppBar(title=Text("Todos Atletas"), bgcolor=colors.SURFACE_VARIANT),
                        myatletas    
                    ],
                )
            )
        elif page.route == "/turmacinco":
            page.views.append(
                View(
                    "/turmacinco",
                    [
                        AppBar(title=Text("Turma 5 a.m"), bgcolor=colors.SURFACE_VARIANT),
                        id_usuario,
                        ft.ElevatedButton(text="Confimar",on_click=envio5hr),
                        myaula5
                    ],
                 )                
                )  
        
        elif page.route == "/turmaseis":
            page.views.append(
                View(
                    "/turmaseis",
                    [
                        AppBar(title=Text("Turma 6 a.m"), bgcolor=colors.SURFACE_VARIANT),
                        id_usuario,
                        ft.ElevatedButton(text="Confimar",on_click=envio6hr),
                        myaula6
                    ],
                 )                
                )  
        page.update()

    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
 
    page.on_route_change = mundanca_rota
    page.on_view_pop = view_pop
    
    page.go(page.route)


ft.app(target=main)    
