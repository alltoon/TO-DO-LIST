import sqlite3

connection = sqlite3.connect("ToDo.db")
cursor = connection.cursor()


def header(row0: int, row1: int, row2: int):
    head = "╔"
    for i in range(row0 + 2): head += "═"
    head += "╦"
    for _ in range(row1 + 2): head += "═"
    head += "╦"
    for _ in range(row2 + 2): head += "═"
    head += "╗"
    return head


def footer(row0: int, row1: int, row2: int):
    foot = "╚"
    for i in range(row0 + 2): foot += "═"
    foot += "╩"
    for _ in range(row1 + 2): foot += "═"
    foot += "╩"
    for _ in range(row2 + 2): foot += "═"
    foot += "╝"
    return foot


def count_max_row(n, all_row):  # n => row index
    for row in all_row:
        row_max = 0
        if len(str(row[n])) >= row_max:
            row_max = len(str(row[n]))
    return row_max


def new_task():
    print("""
╔═════════════════════════════════════════════╗
║ Ajouter une nouvelle tache à la ToDo Liste: ║
╚═════════════════════════════════════════════╝
    """)

    designation = input("Contenu de votre tache :")
    date_eche = input("Date d'écheance, format AAAA-MM-DD :")
    letat = input("État de la tâche, 0 pour non fait, X pour fait :")
    cursor.execute(
        '''INSERT INTO "taches" (id, designation, echeance, etat) VALUES (1,  designation, date_eche, letat);''')
    pass


def see_task():
    print("""
╔════════════════════════════════════════╗
║ Consulter les taches de la ToDo Liste: ║
╚════════════════════════════════════════╝
Quelle action souhaitez vous effectuez ? Répondre par 1,2 ou 3:
    1 - Consulter toutes les taches
    2 - Consulter les taches non terminées 
    3 - Consulter les taches terminées
    4 - Consulter les taches urgentes
    """)
    designation = str(input("Effectuer l'action : "))

    if designation=='1':
        cursor.execute('''SELECT * FROM taches''')
        all_row = cursor.fetchall()
        print(header(count_max_row(0, all_row), count_max_row(1, all_row), count_max_row(2, all_row)))
        for row in all_row:
            print('║ {0} ║ {1} ║ {2} ║ '.format(row[0], row[1], row[2]))


def edit_task():
    print("""
╔═══════════════════════════════════════════════╗
║ Modifier l'état d'une tache de la ToDo Liste: ║
╚═══════════════════════════════════════════════╝
    """)
    pass


def del_task():
    print("""
╔═══════════════════════════════════════╗
║ Supprimer une tache de la ToDo Liste: ║
╚═══════════════════════════════════════╝
    """)
    pass
