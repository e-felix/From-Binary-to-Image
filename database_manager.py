import psycopg2
from psycopg2 import OperationalError
import logging
from load_env import read_env_vars


class DatabaseManager:
    """
    This class is used to connect to the database

    Attributes:
        db_name (string): the database name
        db_user (string): the database username
        db_password (string): the database password
        db_host (string): the database host IP
        db_port (int): the database name
    """
    CONNECTION_MESSAGE = "Connection to PostgreSQL DB successful"
    SUCCESS_MESSAGE = "Query was executed correctly"
    ERROR_MESSAGE = "A error occured:"

    def __init__(self):
        """
        Returns a database connection

        Parameters:
            db_name (string): the database name
            db_user (string): the database username
            db_password (string): the database password
            db_host (string): the database host IP
            db_port (int): the database name

        Returns:
            connection (object): the database connection
        """
        db_vars = read_env_vars()

        self.db_host = db_vars["DATABASE_HOST"]
        self.db_port = db_vars["DATABASE_PORT"]
        self.db_name = db_vars["DATABASE_NAME"]
        self.db_user = db_vars["DATABASE_USER"]
        self.db_password = db_vars["DATABASE_PASSWORD"]
        self.connection = None
        self.cursor = None

        self.create_connection()

    def create_connection(self):
        """
        Creates and returns a database connection

        Returns:
            connection (object): the database connection
        """
        if self.cursor is not None:
            self.cursor = self.connection.cursor()
            return self.connection

        try:
            self.connection = psycopg2.connect(
                host=self.db_host,
                port=self.db_port,
                database=self.db_name,
                user=self.db_user,
                password=self.db_password
            )
            logging.info(self.CONNECTION_MESSAGE)
        except OperationalError as e:
            logging.error(f"Create Connection: {self.ERROR_MESSAGE} {e}")

        self.cursor = self.connection.cursor()
        return self.connection

    def find_signals_images(self):
        """
        Returns the list of images

        Returns:
            result (tuple): the list of images
        """
        query = f"""
            SELECT *
            FROM image
            WHERE signal_id IS NOT NULL
        """

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            logging.info(f"Query find_users: {self.SUCCESS_MESSAGE}")
            return result
        except OperationalError as e:
            logging.error(f"Query find_users: {self.ERROR_MESSAGE} {e}")

    def delete_signal_documents_of_inactive_users_from_database(self, signalsId):
        """
        Delete the documents of inactive users

        Parameters:
            signalsId (string): the list of signal Ids
        """
        query = f"""
            DELETE FROM document
            WHERE signal_id IN ({signalsId})
        """

        try:
            self.cursor.execute(query)
            self.connection.commit()
            logging.info(f"Query delete_signal_documents_of_inactive_users_from_database: {self.SUCCESS_MESSAGE}")
        except OperationalError as e:
            logging.error(f"Query delete_signal_documents_of_inactive_users_from_database: {self.ERROR_MESSAGE} {e}")
