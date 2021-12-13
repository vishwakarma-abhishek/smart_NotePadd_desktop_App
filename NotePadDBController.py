import NotePadDbModel


class Db_Controller:

    def __init__(self):
        self.db_model = NotePadDbModel.Db_Model()

    def get_db_status(self):
        return self.db_model.get_db_status()

    def close_notepad(self):
        self.db_model.close_db_connection()

    def get_file_path(self, file_name):
        return self.db_model.get_file_path(file_name)

    def get_file_count(self):
        return self.db_model.file_count()  # check weather this method is exist or not in db_model

    def get_file_owner(self, file_name):
        file_name, file_path, file_owner, file_pwd = self.db_model.file_dict[file_name]
        return file_owner

    def get_file_pwd(self, file_name):
        return self.get_file_pwd(file_name)

    def is_secure_file(self, file_name):
        return self.db_model.is_secure_file(file_name)

    def add_file(self, file_name, file_path, file_owner, file_pwd):
        if file_path == "":
            return ""
        if file_name in self.db_model.file_dict:
            return "File Already Present!"
        self.db_model.add_file(file_name, file_path, file_owner, file_pwd)
        self.db_model.add_file_to_db(file_name, file_path, file_owner, file_pwd)
        return "File added Successfully!"

    def load_files_from_db(self):
        self.db_model.load_files_from_db()
        return self.db_model.file_dict

    def remove_file(self, file_name):
        self.db_model.remove_file_from_db(file_name)