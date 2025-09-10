import os
import mysql.connector

from django.core.management.base import BaseCommand, CommandError, CommandParser

# Write your command here


class Command(BaseCommand):
    help = "Creates a database"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-n",
            "--name",
            type=str,
            help="Name of the database to be created.",
        )

    def handle(self, *args, **kwargs):
        default = os.getenv("DB_NAME")
        given = kwargs.get("name")
        db_name = default if given is None else given

        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
        )
        mycursor = mydb.cursor()

        query = "CREATE DATABASE {}".format(db_name)

        mycursor.execute(query)

        print("Database created successfully.")
