import sqlite3
import chart_builder as cb
connection = sqlite3.connect("ToDo.db")
cursor = connection.cursor()

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
        cb.chart(all_row)
    if designation=='2':
        cursor.execute('''SELECT * FROM taches''')
        all_row = cursor.fetchall()
        cb.chart(all_row)
    if designation=='3':
        cursor.execute('''SELECT * FROM taches''')
        all_row = cursor.fetchall()
        cb.chart(all_row)
    if designation=='4':
        cursor.execute('''SELECT * FROM taches''')
        all_row = cursor.fetchall()
        cb.chart(all_row)


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
