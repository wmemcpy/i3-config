import unittest
import os
from System import System
from unittest.mock import patch


class TestSystem(unittest.TestCase):

    def setUp(self) -> None:
        self.log_file = "test_log.log"
        self.system = System(log_file=self.log_file)

    def tearDown(self) -> None:
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("os.remove")
    def test_init(self, mock_remove, mock_open) -> None:
        system = System(log_file=self.log_file)
        mock_remove.assert_called_once_with(self.log_file)
        mock_open.assert_called_once_with(self.log_file, "w")

    @patch("builtins.print")
    def test_log_command(self, mock_print) -> None:
        self.system.__log_command("Test command")
        mock_print.assert_called_once_with("\033[92m[+]\033[0m Test command")

    @patch("subprocess.run")
    def test_command_success(self, mock_run) -> None:
        mock_run.return_value.returncode = 0
        self.system.command("ls", "listing files")

    @patch("subprocess.run")
    def test_command_failure(self, mock_run) -> None:
        mock_run.side_effect = Exception("An error occurred")
        with self.assertRaises(SystemExit) as cm:
            self.system.command("ls", "listing files")
        self.assertEqual(cm.exception.code, 1)

    @patch("shutil.copy")
    def test_copy_file_success(self, mock_copy) -> None:
        self.system.copy_file("src.txt", "dst.txt")
        mock_copy.assert_called_once_with("src.txt", "dst.txt")

    @patch("shutil.copy")
    def test_copy_file_failure(self, mock_copy) -> None:
        mock_copy.side_effect = PermissionError("Permission denied")
        with self.assertRaises(SystemExit) as cm:
            self.system.copy_file("src.txt", "dst.txt")
        self.assertEqual(cm.exception.code, 1)
