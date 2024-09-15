from flet import *
import sqlite3

conn=sqlite3.connect('db/database.db', check_same_thread=False)

# caula = turma 5 horas

tb_atleta=DataTable(
    columns=[
        DataColumn(Text('Ação')),
        DataColumn(Text('ID')),
        DataColumn(Text('Nome')),
        DataColumn(Text('Idade')),
        DataColumn(Text('Modalidade')),
    ],
    rows=[]
)

tb_aula5=DataTable(
    columns=[
        DataColumn(Text('Ação')),
        DataColumn(Text('ID')),
        DataColumn(Text('Nome')),
   ],
    rows=[]
)

tb_aula6=DataTable(
    columns=[
        DataColumn(Text('Ação')),
        DataColumn(Text('ID')),
        DataColumn(Text('Nome')),
   ],
    rows=[]
)

def showdelete(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("DELETE FROM atleta WHERE id=?",(myid,))
        conn.commit()
        tb_atleta.rows.clear()
        totalatleta()
        tb_atleta.update()

    except Exception as erro:
        print(erro)

def showdelete2(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("UPDATE atleta SET id_usuario = 0 WHERE id=?",(myid,))
        conn.commit()
  
        tb_aula5.rows.clear()
        totalaula5()
        tb_aula5.update()
        
    except Exception as erro:
        print(erro)

    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("UPDATE atleta SET id_usuario = 0 WHERE id=?",(myid,))
        conn.commit()
  
        tb_aula6.rows.clear()
        totalaula6()
        tb_aula6.update()

    except Exception as erro:
        print(erro)


id_edit = Text()
nome_edit = TextField(label='Nome')
idade_edit = TextField(label='Idade')
modalidade_edit = TextField(label='Modalidade')

def hidedlg(e):
    dlg.visible=False
    dlg.update()

def updateandsave(e):
    try:
        myid = id_edit.value
        c=conn.cursor()
        c.execute(
            """UPDATE atleta SET nome=?, idade=?,
            modalidade=?
            WHERE id=?""", (nome_edit.value, idade_edit.value, 
            modalidade_edit.value, myid)
        )
        conn.commit()
        print('Editados com sucesso')
        tb_atleta.rows.clear()
        totalatleta()
        dlg.visible=False
        dlg.update()
        tb_atleta.update()

    except Exception as erro:
        print('o erro está aqui', erro)

dlg = Container(
    bgcolor='green200',
    padding=10,
    content=Column([
        Row([
            Text(
                'Editar dados',
                size=20,
                weight='bold'
            ),
            IconButton(
                icon='close', 
                on_click=hidedlg
            )], alignment='spaceBetween'),
        nome_edit,
        idade_edit,
        modalidade_edit,
        ElevatedButton(
            'Atualizar',
            on_click=updateandsave
        ),
    ])
)

def showedit(e):
    data_edit = e.control.data
    id_edit.value = data_edit['id']
    nome_edit.value = data_edit['nome']
    idade_edit.value = data_edit['idade']
    modalidade_edit.value = data_edit['modalidade']
    
    dlg.visible=True
    dlg.update()

def totalatleta():
    c = conn.cursor()
    c.execute('SELECT * FROM atleta')
    atleta = c.fetchall()
    print(atleta)

    if not atleta == '':
        keys= ['id', 'nome','idade', 'modalidade']
        result = [dict(zip(keys, values)) for values in atleta]
        for x in result:
            tb_atleta.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                IconButton(
                                    icon='create',
                                    icon_color='blue',
                                    data=x,
                                    on_click=showedit
                                ),
                                IconButton(
                                    icon='delete',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete
                                ),
                            ])
                        ),
                        DataCell(Text(x['id'])),
                        DataCell(Text(x['nome'])),
                        DataCell(Text(x['idade'])),
                        DataCell(Text(x['modalidade'])),
  
                    ],
                ),
            )

totalatleta()
dlg.visible=False


def totalaula5():
    c = conn.cursor()
    c.execute('SELECT * FROM atleta WHERE id_usuario=1')
    checkin= c.fetchall()
    print(checkin)

    if not checkin == '':
        keys= ['id', 'nome']
        result = [dict(zip(keys, values)) for values in checkin]
        for x in result:
            tb_aula5.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                
                                IconButton(
                                    icon='delete',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete2
                                ),
                            ])
                        ),
                        DataCell(Text(x['id'])),
                        DataCell(Text(x['nome'])),
                          
                    ],
                ),
            )

    
totalaula5()

def totalaula6():
    c = conn.cursor()
    c.execute('SELECT * FROM atleta WHERE id_usuario=2')
    checkin= c.fetchall()
    print(checkin)

    if not checkin == '':
        keys= ['id', 'nome']
        result = [dict(zip(keys, values)) for values in checkin]
        for x in result:
            tb_aula6.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                
                                IconButton(
                                    icon='delete',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete2
                                ),
                            ])
                        ),
                        DataCell(Text(x['id'])),
                        DataCell(Text(x['nome'])),
                          
                    ],
                ),
            )

    
totalaula6()



myatletas = Column([
        dlg,
        Row([tb_atleta],scroll='always')
])

myaula5 = Column([
    dlg,
    Row([tb_aula5],scroll='always')
])

myaula6 = Column([
    dlg,
    Row([tb_aula6],scroll='always')
])

