import os
import json


class ConfigManager:

    @staticmethod
    def load_config_file_in_current_dir():
        # Get the directory of the current script
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the JSON file
        return os.path.join(current_directory, 'config.json')

    @staticmethod
    def get_config_dict():
        config_path = ConfigManager.load_config_file_in_current_dir()
        config_dict = {}
        try:
            with open(config_path) as config_file:
                config_dict = json.load(config_file)
        except Exception as e:
            print(e)
        return config_dict

    @staticmethod
    def get_config(name: str):
        try:
            return ConfigManager.get_config_dict()[name]
        except Exception as e:
            print(str(e))
            return {}

    @staticmethod
    def set_config(namespace: str, name: str, value):
        config_path = ConfigManager.load_config_file_in_current_dir()
        try:
            # Load the existing config
            with open(config_path, 'r') as config_file:
                config_dict = json.load(config_file)

            # Update the config with the new value
            config_dict[namespace][name] = value

            # Write the updated config back to the file
            with open(config_path, 'w') as config_file:
                json.dump(config_dict, config_file, indent=4)

        except Exception as e:
            print(str(e))
