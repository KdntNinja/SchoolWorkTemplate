import os
import shutil
from datetime import datetime


class DocsTemplateInterface:
    class DocsTemplate:
        def __init__(self, subject_dir: str) -> None:
            self.subject_dir: str = f"Classwork/{subject_dir}/"
            self.inv_date: str = datetime.today().strftime("%y.%m.%d")
            self.new_template_name: str = f"{self.inv_date}.docx"
            self.template_dir: str = f"{os.getcwd()}/{self.subject_dir}"
            self.template_copy_path: str = os.path.join(
                self.template_dir, self.new_template_name
            )
            os.makedirs(os.path.dirname(self.template_copy_path), exist_ok=True)
            shutil.copy2("template.docx", self.template_copy_path)

    def __init__(self):
        self.subjects: list = ["English", "Biology", "Chemistry", "Physics"]
        self.subject: int = 0
        self.subject_menu = (
            "\n".join(f"({i}) {self.subjects[i]}" for i in range(len(self.subjects)))
            + "\n"
        )

        self.user_select_subject()
        self.run_docs_template()

    def user_select_subject(self) -> None:
        while True:
            try:
                choice = int(input(self.subject_menu))
                if 0 <= choice < len(self.subjects):
                    self.subject = self.subjects[choice]
                    break
                else:
                    print("Invalid selection. Please enter a valid number.")
                    continue
            except (ValueError, IndexError):
                print("Please enter a valid number.")
                continue

    def run_docs_template(self) -> None:
        self.DocsTemplate(str(self.subject))


if __name__ == "__main__":
    DocsTemplateInterface()
