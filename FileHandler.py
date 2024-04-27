import pickle
import os

class FileHandler:
    @staticmethod
    def save_data(data, filename):
        """
        Static method to save data to a file using pickle serialization.

        Parameters:
            data (object): The data to be saved.
            filename (str): The name of the file to save the data to.
        """
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist. Creating a new file.")
            with open(filename, 'wb'):
                pass  # Create an empty file
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_data(filename):
        """
        Static method to load data from a file using pickle deserialization.

        Parameters:
            filename (str): The name of the file to load data from.

        Returns:
            object: The loaded data.
        """
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                data = pickle.load(file)
            return data
        else:
            print(f"File '{filename}' does not exist. Returning None.")
            return None
