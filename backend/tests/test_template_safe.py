from backend.ingestion.docx_reader import extract_text_from_docx
import os


def run():
    print("=== TEST TEMPLATE SAFE ===")

    file_path = "backend/tests/test_files/ejemplo.docx"

    if not os.path.exists(file_path):
        print("❌ File not found:", file_path)
        return

    text = extract_text_from_docx(file_path)

    print("\n📄 Extracted Text:\n")
    print(text)


if __name__ == "__main__":
    run()
