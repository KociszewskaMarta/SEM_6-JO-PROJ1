## Manual test cases

### Template
- **Summary**: [Nazwa testu]
- Priority: [Highest/High/Medium/Low/Lowest]

Setup procedures: [...]

Actions:

|Action|Expected result|
|---|---|
| [...] | [...] |

### Testy funkcjonalne (>=10 test case)

1. **Łączenie plików PDF**: Sprawdzenie, czy aplikacja poprawnie scala dwa lub więcej plików PDF w jeden dokument, zachowując kolejność stron - podstawowy scenariusz.

Summary: Łączenie plików PDF
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Łączenie" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się moduł "Łączenie" - okna dialogowe "Przeciągnij i upuść tu pliki PDF" oraz "Ustawienia łączenia" i "Plik docelowy"|
| Przeciągnij i upuść pliki PDF w oknie dialogowym| Wybrane pliki PDF są dodawane do listy wraz z ich metadanymi|
|Ustawienie plików w pożądanej kolejności za pomocą przycisków  "W górę" i "Przesuń w dół" lub ręcznie| Pliki są ustawiane w odpowiedniej kolejności w liście|
| Sprawdź sekcję „Ustawienia łączenia” bez dokonywania w niej żadnych zmian. | Sekcja jest widoczna. Opcje pozostają w stanach domyślnych (np. „Normalizacja stron: Brak”, „Spis treści: Nie twórz”) |
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_merge.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Proces scalania rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera połączone dokumenty.|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test1-merging/test1-merging.pdf`

2. **Łączenie przemienne plików PDF**: Sprawdzenie, czy aplikacja poprawnie scala dwa lub więcej plików PDF w jeden dokument, przyjmując kolejność naturalną.

Summary: Łączenie przemienne plików PDF w naturalnej kolejności
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Łączenie przemienne" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się moduł "Łączenie" - okna dialogowe "Przeciągnij i upuść tu pliki PDF" i "Plik docelowy"|
| Przeciągnij i upuść pliki PDF w oknie dialogowym| Wybrane pliki PDF są dodawane do listy wraz z ich metadanymi|
|Ustawienie plików w pożądanej kolejności za pomocą przycisków  "W górę" i "Przesuń w dół" lub ręcznie| Pliki są ustawiane w odpowiedniej kolejności w liście|
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_alternatemix.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Proces scalania rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera połączone dokumenty w naturalnej kolejności.|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test2-alternate-mix-natural/alternate-mix-natural.pdf`

3. **Łączenie przemienne plików PDF**: Sprawdzenie, czy aplikacja poprawnie scala dwa lub więcej plików PDF w jeden dokument, przyjmując kolejność odwrotną.

Summary: Łączenie przemienne plików PDF w odwrotnej kolejności dla jednego z plików
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Łączenie przemienne" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się moduł "Łączenie" - okna dialogowe "Przeciągnij i upuść tu pliki PDF" i "Plik docelowy"|
| Przeciągnij i upuść pliki PDF w oknie dialogowym| Wybrane pliki PDF są dodawane do listy wraz z ich metadanymi|
|Ustawienie plików w pożądanej kolejności za pomocą przycisków  "W górę" i "Przesuń w dół" lub ręcznie| Pliki są ustawiane w odpowiedniej kolejności w liście|
| W oknie dialogowym zaznacz checkbox "Odwracanie" przy jednym z plików | Checkbox jest zaznaczony na kolor niebieski, podczas gdy inne pliki pozostają bez zmian. Podczas zamiany kolejności plików, checkbox pozostaje zaznaczony przy odpowiednim pliku.|
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_alternatemix.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Proces scalania rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera połączone dokumenty w odwrotnej kolejności.|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test3-alternate-mix-reversed/alternate-mix-reversed.pdf`
