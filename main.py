import sqlite3
import action as ac


def menu():
    print("""
╔═══════════════════════════════════════════╗
║ Bienvenu sur l'interface NSI Todo Liste : ║
╚═══════════════════════════════════════════╝
Quelle action souhaitez vous effectuez ? Répondre par 1,2,3,4 ou 5:
    1 - C - Créer une nouvelle tache
    2 - R - Consulter la liste des taches non terminée, terminée, urgentes
    3 - U - Modifier l'état d'une tache.
    4 - D - Supprimer une tache.
    5 - E - Quitter l'application
    """)
    return str(input("Effectuer l'action : "))


v = True
while v:
    main_menu = menu()
    if main_menu=='1' or main_menu=='C':
        ac.new_task()
        v = False
    if main_menu=='2' or main_menu=='R':
        ac.see_task()
        v = False
    if main_menu=='3' or main_menu=='U':
        ac.edit_task()
        v = False
    if main_menu=='4' or main_menu=='D':
        ac.del_task()
        v = False
    if main_menu=='5' or main_menu=='E':
        exit()
    if int(main_menu) > 5 or str(main_menu)!='C' or 'R' or 'U' or 'D' or 'E':
        print("\nVotre entrée est invalide !\n")
