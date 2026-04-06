import PyPDF2

def generate_expected_content():
    # File performance_test_9999.pdf page 2 / 10
    expected=[]
    for i in range(0, 10000):
        for j in range(0, 10):
            expected.append( f"File performance_test_{i}.pdf page {j+1} / 10")
    return expected

def read_pdf_content(_filepath):
    actual = []
    with open(_filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text().strip()
            actual.append(text)

    return actual


def compare_content(_expected, _actual):
    if len(_expected) != len(_actual):
        print(f"Różna liczba stron: Oczekiwano {len(_expected)}, Rzeczywiście {len(_actual)}")
        return False

    mismatches = []
    for i, (exp, act) in enumerate(zip(_expected, _actual)):
        if exp != act:
            mismatches.append((i, exp, act))

    if mismatches:
        print(f"Znaleziono {len(mismatches)} niezgodności. Oto pierwsze 10:")
        for page_num, exp, act in mismatches[:10]:  # Wyświetl pierwszych 10
            print(f"  Strona {page_num + 1}: Oczekiwana: '{exp}' | Rzeczywista: '{act}'")
        return False

    return True


if __name__ == "__main__":
    filepath = "/mnt/c/Users/kocis/Desktop/SEM_6/Jakosc_oprogramowania/Projekt/SEM_6-JO-PROJ1/test_artefacts/performance_tests/test1/test1-merge.pdf"
    expected_content = generate_expected_content()
    actual_content = read_pdf_content(filepath)
    if compare_content(expected_content, actual_content):
        print("Zawartość PDF zgodna z oczekiwaną.")
    else:
        print("Zawartość PDF NIE jest zgodna z oczekiwaną.")