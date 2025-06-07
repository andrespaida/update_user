def update_user(conn, user_id, fields):
    set_clause = ', '.join(f"{key} = %s" for key in fields)
    values = list(fields.values()) + [user_id]

    with conn.cursor() as cur:
        cur.execute(
            f"UPDATE users SET {set_clause} WHERE id = %s",
            values
        )
        conn.commit()
