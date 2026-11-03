import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

CLIENT_DIR = Path(__file__).parents[1] / "src" / "win-arena-container" / "client"
sys.path.insert(0, str(CLIENT_DIR))

from result_utils import parse_result_value
from show_result import get_result


class TestParseResultValue(unittest.TestCase):
    def test_boolean_and_numeric_values(self):
        cases = {
            "True\n": 1.0,
            "false\n": 0.0,
            "0.75\n": 0.75,
            "1\n": 1.0,
        }
        for result, expected in cases.items():
            with self.subTest(result=result):
                self.assertEqual(parse_result_value(result, "results/vlc/task/result.txt"), expected)

    def test_invalid_and_non_finite_values_fail_closed_and_log_path(self):
        for result in ("not-a-score", "", "nan", "inf"):
            with self.subTest(result=result):
                with self.assertLogs("result_utils", level="WARNING") as captured:
                    value = parse_result_value(result, "results/vlc/task/result.txt")
                self.assertEqual(value, 0.0)
                self.assertIn("results/vlc/task/result.txt", captured.output[0])

    def test_show_result_aggregates_boolean_values_consistently(self):
        with tempfile.TemporaryDirectory() as target_dir:
            for domain, task, value in (
                ("libreoffice_calc", "passed", "True\n"),
                ("vlc", "failed", "False\n"),
            ):
                task_dir = Path(target_dir) / domain / task
                task_dir.mkdir(parents=True)
                (task_dir / "result.txt").write_text(value, encoding="utf-8")

            with redirect_stdout(io.StringIO()):
                results = get_result(target_dir)

            self.assertCountEqual(results, [1.0, 0.0])
            analysis = json.loads((Path(target_dir) / "all_result.json").read_text(encoding="utf-8"))
            self.assertEqual(analysis["vlc"]["failed"], 0.0)


if __name__ == "__main__":
    unittest.main()
