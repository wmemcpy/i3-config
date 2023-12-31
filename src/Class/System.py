from subprocess import run, PIPE, CalledProcessError, Popen
from os import remove, system, path
from datetime import datetime


class System:
    def __init__(self, log_file: str = "log.log", log: bool = True) -> None:
        self.log_file = log_file
        self.log = log

        if log and log_file:
            if path.exists(log_file):
                remove(log_file)
            with open(log_file, "w") as f:
                f.write(
                    f"[{datetime.now().strftime('%H:%M:%S')}]: Log file created.\n")

    def __log_command(self, cmd: str, error: bool = False) -> None:
        if error:
            print(f"\033[91m[-] {cmd}\033[0m")
        if self.log and self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().strftime('%H:%M:%S')}]: {cmd}\n")

    def command(self, cmd: str, tiny_cmd: str):
        print(f"\033[92m[+]\033[0m {tiny_cmd}")
        self.__log_command(cmd)

        try:
            if "sudo" in cmd:
                system(f"{cmd} >> {self.log_file} 2>&1")
            else:
                run(cmd, shell=True, check=True,
                    text=True, stdout=PIPE, stderr=PIPE)
        except CalledProcessError as e:
            self.__log_command(
                f"Failed to execute {cmd}: {e.stderr}", error=True)
        except Exception as e:
            self.__log_command(
                f"Failed to execute {cmd}: {str(e)}", error=True)

    def copy_file(self, src: str, dst: str, sudo: bool = False, log_msg: str = "") -> None:
        sudo_cmd = "sudo " if sudo else ""
        try:
            dst_dir = path.dirname(dst)
            if not path.exists(dst_dir):
                self.command(f"{sudo_cmd}mkdir -p {dst_dir}",
                             f"Creating directory {dst_dir}")

            if path.exists(dst):
                self.command(f"{sudo_cmd}cp {dst} {dst}.bak",
                             f"Backing up {dst}")
            self.command(f"{sudo_cmd}cp -r {src} {dst}", log_msg)
        except FileNotFoundError:
            self.__log_command(f"File {src} does not exist", error=True)
        except PermissionError:
            self.__log_command(
                f"Permission denied: Cannot copy {src} to {dst}", error=True)
        except Exception as e:
            self.__log_command(
                f"Failed to copy {src} to {dst}: {str(e)}", error=True)

    def command_with_enter(self, cmd: str):
        print(
            f"\033[92m[+]\033[0m Executing {cmd} and simulating Enter key press")
        self.__log_command(cmd)

        process = Popen(
            cmd,
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
            text=True
        )

        process.stdin.write('\n')
        process.stdin.flush()

        stdout, stderr = process.communicate()

        if process.returncode != 0:
            self.__log_command(
                f"Failed to execute {cmd} with enter: {stderr}", error=True)
            return None

        return stdout
