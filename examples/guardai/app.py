"""Consulta local usada para validar a separação entre SQL e dados."""

import sqlite3


def find_user(connection: sqlite3.Connection, username: str) -> tuple | None:
    return connection.execute(
        "SELECT username FROM users WHERE username = ?", (username,)
    ).fetchone()


if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE users (username TEXT PRIMARY KEY)")
        connection.executemany(
            "INSERT INTO users VALUES (?)", [("Ana",), ("D'Ávila",)]
        )
        assert find_user(connection, "Ana") == ("Ana",)
        assert find_user(connection, "D'Ávila") == ("D'Ávila",)
        assert find_user(connection, "Ausente") is None
        print("Consultas parametrizadas verificadas em três casos.")
    finally:
        connection.close()
