import sqlite3
from contextlib import closing
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("notes.db")


def connect_database():
    return closing(sqlite3.connect(DATABASE_PATH))


def initialize_database():
    with connect_database() as connection:
        with connection:
            # TODO: Crie a tabela notes com id, title e content.
            pass


def add_note(title, content):
    with connect_database() as connection:
        with connection:
            # TODO: Insira a nota usando parâmetros ? e retorne o id gerado.
            pass


def list_notes():
    with connect_database() as connection:
        # TODO: Retorne id, title e content de todas as notas, ordenadas por id.
        pass


def update_note(note_id, title, content):
    with connect_database() as connection:
        with connection:
            # TODO: Atualize a nota e retorne True se uma linha foi alterada.
            pass


def delete_note(note_id):
    with connect_database() as connection:
        with connection:
            # TODO: Exclua a nota e retorne True se uma linha foi removida.
            pass
