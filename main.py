#!/usr/bin/env python

import json
import sqlalchemy as db
from sqlalchemy import text


def pretty_print(string: str):
    """Pretty print things"""
    print(json.dumps(string, indent=2, sort_keys=True))


def main():
    "Main function"

    engine = db.create_engine('mysql+pymysql://root:password@localhost:3306/employees')

    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM employees LIMIT 5;"))
        for row in result:
            print(row)



if __name__ == '__main__':
    main()
