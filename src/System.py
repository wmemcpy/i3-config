from subprocess import run, PIPE, CalledProcessError
from datetime import datetime
from os import remove, path, makedirs
from shutil import copy, SameFileError


class System:
    def __init__(self, log_file: str = "log.log", log: bool = True) -> None:
        self.log_file = log_file
        self.log = log

        if log and log_file:
            try:
                remove(log_file)
            except FileNotFoundError:
                self.__log_command(f"Log file {log_file} does not exist.")
            with open(log_file, "w") as f:
                f.write(f"[{datetime.now()}]: Log file created.\n")

    def __log_command(self, cmd: str, error: bool=False) -> None:
        if error:
            print(f"\033[91m{cmd}\033[0m")
        if self.log and self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now()}]: {cmd}\n")

    def command(self, cmd: str, tiny_cmd: str) -> str:
        print(f"\033[92m[+]\033[0m {tiny_cmd}")
        self.__log_command(cmd)

        try:
            result = run(cmd, shell=True, check=True, text=True, stdout=PIPE, stderr=PIPE)
            return result.stdout
        except CalledProcessError as e:
            self.__log_command(f"An error occurred: {str(e)}", error=True)
            return e.stderr

    def copy_file(self, src: str, dst: str) -> None:
        try:
            copy(src, dst)
            self.__log_command(f"Copying {src} to {dst}")
        except SameFileError:
            self.__log_command("Source and destination represents the same file.")
        except PermissionError:
            self.__log_command(f"Permission denied: Cannot copy {src} to {dst}", error=True)
            exit(1)            
        except Exception as e:
            self.__log_command(f"Failed to copy {src} to {dst}: {str(e)}", error=True)
            exit(1)