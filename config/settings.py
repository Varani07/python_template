from mysql.connector import Error, connect

class ConexaoBanco:
    @staticmethod
    def get_connection():
        """Retorna uma conexão ativa com o banco ou None em caso de erro."""
        try:
            connection = connect(
                host="localhost",
                user="root",
                password='1234',
                database="teste_modelo"
            )
            return connection
        except Error as e:
            print(f"Erro ao conectar! {e}")
            return None 