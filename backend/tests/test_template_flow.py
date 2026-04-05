from backend.ingestion.docx_reader import extract_text_from_docx


def run():
    print("=== TEST TEMPLATE FLOW ===")

    file_path = "backend/tests/test_files/ejemplo.docx"

    try:
        text = extract_text_from_docx(file_path)

        print("\n✅ TEMPLATE FLOW WORKING\n")
        print(text[:500])  # preview

    except Exception as e:
        print("\n❌ ERROR")
        print(str(e))


if __name__ == "__main__":
    run()
