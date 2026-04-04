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

PASSED

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
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera połączone dokumenty w naturalnej kolejności.|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test2-alternate-mix-natural/alternate-mix-natural.pdf`
    
PASSED

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
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera połączone dokumenty w odwrotnej kolejności.|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test3-alternate-mix-reversed/alternate-mix-reversed.pdf`

PASSED

4. **Wielokrotne wstawianie strony**: Wstawienie strony z dokumentu A do dokumentu B, powtarzając to po określonej liczbie stron, docelowow B1 A B2 A B3 A...

Summary: Wstawianie strony z dokumentu A (jednostronnego pliku) do dokumentu B (wielostronnego pliku) w określonych odstępach
Priority: Medium

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Wstaw strony wiele razy" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się obszar roboczy z sekcjami: Wybór głównego PDF, "Ustawienia Wstaw i Powtórz" oraz "Plik docelowy". |
| Kliknij przycisk "Wybierz PDF" na górze i wskaż plik główny. | Ścieżka do pliku pojawia się w szarym polu, a poniżej wyświetla się informacja o liczbie stron i wersji PDF. |
|W sekcji "Ustawienia Wstaw i Powtórz" kliknij "Przeglądaj" i wybierz plik, którego strony mają być powtarzane. | Ścieżka do drugiego pliku pojawia się w polu tekstowym. |
| W polu "Powtarzaj te strony" wpisz numery stron (np. "1"), a w polu "Powtarzaj co 'n' stron" wpisz np. "1". | Wartości zostają wprowadzone do pól tekstowych. |
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_alternatemix.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera pzawiera naprzemiennie strony z pliku głównego i pliku powtarzanego (układ 1:1).|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleC.pdf`
Rezultat: `test_artefacts/functionality_test/test4-multi-insert-1/multi-insert-1.pdf`

PASSED

5. **Wielokrotne wstawianie strony**: Wstawienie strony z dokumentu A do dokumentu B, powtarzając to po określonej liczbie stron, docelowow B1 A B2 A B3 A...

Summary: Wstawianie strony z dokumentu A (wielostronnego pliku) do dokumentu B (wielostronnego pliku) w określonych odstępach
Priority: Medium

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Wstaw strony wiele razy" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się obszar roboczy z sekcjami: Wybór głównego PDF, "Ustawienia Wstaw i Powtórz" oraz "Plik docelowy". |
| Kliknij przycisk "Wybierz PDF" na górze i wskaż plik główny. | Ścieżka do pliku pojawia się w szarym polu, a poniżej wyświetla się informacja o liczbie stron i wersji PDF. |
|W sekcji "Ustawienia Wstaw i Powtórz" kliknij "Przeglądaj" i wybierz plik, którego strony mają być powtarzane. | Ścieżka do drugiego pliku pojawia się w polu tekstowym. |
| W polu "Powtarzaj te strony" wpisz numery stron (np. "1"), a w polu "Powtarzaj co 'n' stron" wpisz np. "1". | Wartości zostają wprowadzone do pól tekstowych. |
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_alternatemix.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera pzawiera naprzemiennie strony z pliku głównego i pliku powtarzanego (układ 1:1).|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test5-multi-insert-2/multi-insert-2.pdf`

PASSED

6. **Wielokrotne wstawianie strony**: Wstawienie strony z dokumentu A do dokumentu B, powtarzając to po określonej liczbie stron, docelowow B1 A B2 A B3 A...

Summary: Wstawianie wielu stron z dokumentu A (wielostronnego pliku) do dokumentu B (wielostronnego pliku) w określonych odstępach
Priority: Medium

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Wstaw strony wiele razy" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się obszar roboczy z sekcjami: Wybór głównego PDF, "Ustawienia Wstaw i Powtórz" oraz "Plik docelowy". |
| Kliknij przycisk "Wybierz PDF" na górze i wskaż plik główny. | Ścieżka do pliku pojawia się w szarym polu, a poniżej wyświetla się informacja o liczbie stron i wersji PDF. |
|W sekcji "Ustawienia Wstaw i Powtórz" kliknij "Przeglądaj" i wybierz plik, którego strony mają być powtarzane. | Ścieżka do drugiego pliku pojawia się w polu tekstowym. |
| W polu "Powtarzaj te strony" wpisz numery stron (np. "2-4"), a w polu "Powtarzaj co 'n' stron" wpisz np. "1". | Wartości zostają wprowadzone do pól tekstowych. |
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_alternatemix.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz plik klikając przycisk "Otwórz" | Plik zostaje otwarty w domyślnej aplikacji do obsługi plików PDF. Plik PDF istnieje, posiada poprawną nazwę i zawiera pzawiera naprzemiennie strony z pliku głównego i pliku powtarzanego (układ 1:1).|

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleB.pdf`
Rezultat: `test_artefacts/functionality_test/test6-multi-insert-3/multi-insert-3.pdf`

PASSED

7. **Wielokrotne wstawianie strony**: Wstawienie strony z dokumentu A do dokumentu B, powtarzając to po określonej liczbie stron, docelowow B1 A B2 A B3 A...

Summary: Wstawianie stron z dokumentu A (jednostronnego pliku) do dokumentu B (wielostronnego pliku) w określonych odstępach. Testowanie *negative path* - wprowadzenie niepoprawnych danych do pól tekstowych.
Priority: Medium

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano testowe pliki pdf

|Action|Expected result|
|---|---|
| Kliknij modułu "Wstaw strony wiele razy" na stronie głównej lub wybierz go z listy bocznej| Wyświetla się obszar roboczy z sekcjami: Wybór głównego PDF, "Ustawienia Wstaw i Powtórz" oraz "Plik docelowy". |
| Kliknij przycisk "Wybierz PDF" na górze i wskaż plik główny. | Ścieżka do pliku pojawia się w szarym polu, a poniżej wyświetla się informacja o liczbie stron i wersji PDF. |
|W sekcji "Ustawienia Wstaw i Powtórz" kliknij "Przeglądaj" i wybierz plik jednostronny, którego strony mają być powtarzane. | Ścieżka do drugiego pliku pojawia się w polu tekstowym. |
| W polu "Powtarzaj te strony" wpisz niepoprawne numery stron (np. "1-3"), a w polu "Powtarzaj co 'n' stron" wpisz np. "1". | Wartości zostają wprowadzone do pól tekstowych. |
| W sekcji „Plik docelowy” kliknij przycisk „Przeglądaj” i wskaż miejsce zapisu oraz nazwę pliku wynikowego. | Wybrana ścieżka pliku pojawia się w polu tekstowym (np. C:\Users\...\PDFsam_alternatemix.pdf). |
| Kliknij niebieski przycisk „Wykonaj”. | Program powinien zablokować wykonanie zadania lub wyświetlić czytelny komunikat o błędzie (np. "Zakres stron wykracza poza dokument"). |

Użyte pliki: `sample_pdfs/sampleA.pdf`, `sample_pdfs/sampleC.pdf`

FAILED

BUG REPORT

- Summary: Niejasny komunikat o błędzie przy wprowadzeniu niepoprawnych danych do pól tekstowych w funkcji "Wstaw strony wiele razy".
- Component: UI / UX
- Severity: Minor (nie wpływa na funkcjonalność, ale może powodować frustrację użytkownika)
- Description: W przypadku wprowadzenia zakresu stron, który wykracza poza liczbę stron w dokumencie, program powinien zablokować wykonanie zadania i wyświetlić czytelny komunikat o błędzie (np. "Zakres stron wykracza poza dokument"). Obecnie program pozwala na rozpoczęcie procesu. Po kliknięciu przycisku "Wykonaj" program wyświetla komunikat "Nie udało się". Po kliknięciu przycisku "Pokaż błędy" program wyświetla techniczne logi błędów, które nie są zrozumiałe dla przeciętnego użytkownika. Brak jasnego komunikatu o błędzie.
- Expected behavior: Program powinien zablokować wykonanie zadania i wyświetlić czytelny komunikat o błędzie (np. "Zakres stron wykracza poza dokument") w przypadku wprowadzenia niepoprawnych danych do pól tekstowych.

8. **Podział PDF - Każda strona:**: Rozdzielenie pliku PDF na pojedyncze pliki jednostronicowe.

Summary: Podział dokumentu PDF na pojedyncze strony (Every page)
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano wielostronicowy plik PDF

|Action|Expected result|
|---|---|
| Kliknij moduł "Podział" na stronie głównej lub z listy bocznej. | Wyświetla się obszar roboczy z sekcjami: Wybór PDF, "Ustawienia dzielenia", "Ustawienia wyjściowe" oraz "Ustawienia nazw plików". |
| Kliknij przycisk "Wybierz PDF" i wskaż plik do podziału. | Ścieżka do pliku pojawia się w polu, wyświetla się informacja o ilości stron i wersji PDF. |
| W sekcji "Ustawienia dzielenia" zaznacz opcję "Podziel po" i wybierz z listy "Każda strona". | Opcja zostaje wybrana. Pozostałe pola tekstowe w tej sekcji stają się nieaktywne. |
| W sekcji "Ustawienia wyjściowe" kliknij "Przeglądaj" i wybierz folder docelowy. | Ścieżka folderu pojawia się w polu tekstowym. |
| W sekcji "Ustawienia nazw plików" zostaw domyślny przedrostek `PDFsam_`. | Przedrostek jest widoczny w polu. |
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz folder klikając przycisk "Otwórz" | Folder zostaje otwarty. Pliki PDF istnieją, posiadają poprawne nazwy i zawierają odpowiednie strony.|

Użyte pliki: `sample_pdfs/sampleA.pdf`
Rezultat: `test_artefacts/functionality_test/test8-split-every-page/`

PASSED

9. **Podział PDF - Numery stron**: Rozdzielenie pliku PDF na pliki PDF z według określonych numerów stron.

Summary: Podział dokumentu PDF według określonych numerów stron.
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano plik PDF

|Action|Expected result|
|---|---|
| Kliknij moduł "Podział" na stronie głównej lub z listy bocznej. | Wyświetla się obszar roboczy z sekcjami: Wybór PDF, "Ustawienia dzielenia", "Ustawienia wyjściowe" oraz "Ustawienia nazw plików". |
| Kliknij przycisk "Wybierz PDF" i wskaż plik do podziału. | Ścieżka do pliku pojawia się w polu, wyświetla się informacja o ilości stron i wersji PDF. |
| W sekcji "Ustawienia dzielenia" zaznacz opcję "Podziel po następujących numerach stron" | Opcja zostaje wybrana. Pozostałe pola tekstowe w tej sekcji stają się nieaktywne. |
| Wpisz w pole numery stron: "1,3,8" | Wartości zostają wprowadzone. |
| W sekcji "Ustawienia wyjściowe" kliknij "Przeglądaj" i wybierz folder docelowy. | Ścieżka folderu pojawia się w polu tekstowym. |
| W sekcji "Ustawienia nazw plików" zostaw domyślny przedrostek `PDFsam_`. | Przedrostek jest widoczny w polu. |
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz folder klikając przycisk "Otwórz" | Folder zostaje otwarty. Pliki PDF istnieją, posiadają poprawne nazwy i zawierają odpowiednie strony.|

Użyte pliki: `sample_pdfs/sampleA.pdf`
Rezultat: `test_artefacts/functionality_test/test9-split-page-numbers/`

PASSED

10. **Podział PDF - N stron**: Rozdzielenie pliku PDF na pliki PDF po każdych 'n' stronach.

Summary: Podział dokumentu PDF po każdych 'n' stronach..
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano plik PDF

|Action|Expected result|
|---|---|
| Kliknij moduł "Podział" na stronie głównej lub z listy bocznej. | Wyświetla się obszar roboczy z sekcjami: Wybór PDF, "Ustawienia dzielenia", "Ustawienia wyjściowe" oraz "Ustawienia nazw plików". |
| Kliknij przycisk "Wybierz PDF" i wskaż plik do podziału. | Ścieżka do pliku pojawia się w polu, wyświetla się informacja o ilości stron i wersji PDF. |
| W sekcji "Ustawienia dzielenia" zaznacz opcję "Podziel po każdych 'n' stronach" | Opcja zostaje wybrana. Pozostałe pola tekstowe w tej sekcji stają się nieaktywne. |
| Wpisz w pole ilość stron np. "4" | Wartości zostają wprowadzone. |
| W sekcji "Ustawienia wyjściowe" kliknij "Przeglądaj" i wybierz folder docelowy. | Ścieżka folderu pojawia się w polu tekstowym. |
| W sekcji "Ustawienia nazw plików" zostaw domyślny przedrostek `PDFsam_`. | Przedrostek jest widoczny w polu. |
| Kliknij niebieski przycisk „Wykonaj”. | Proces rozpoczyna się i kończy sukcesem. Widoczny jest komunikat o zakończeniu zadania (np. pełny pasek postępu, dźwięk oraz komunikat "Ukończono"). |
| Otwórz folder klikając przycisk "Otwórz" | Folder zostaje otwarty. Pliki PDF istnieją, posiadają poprawne nazwy i zawierają odpowiednie strony.|

Użyte pliki: `sample_pdfs/sampleA.pdf`
Rezultat: `test_artefacts/functionality_test/test10-split-n-pages/`

PASSED

11. **Podział PDF - Numery stron**: Rozdzielenie pliku PDF na pliki PDF z według określonych numerów stron.

Summary: Podział dokumentu PDF według określonych numerów stron. *Negative path* - wprowadzenie niepoprawnych danych (numer strony większy niż liczba stron w dokumencie).
Priority: High

Setup procedures:
- Zainstalowano PDFsam Basic
- Przygotowano plik PDF

|Action|Expected result|
|---|---|
| Kliknij moduł "Podział" na stronie głównej lub z listy bocznej. | Wyświetla się obszar roboczy z sekcjami: Wybór PDF, "Ustawienia dzielenia", "Ustawienia wyjściowe" oraz "Ustawienia nazw plików". |
| Kliknij przycisk "Wybierz PDF" i wskaż plik do podziału. | Ścieżka do pliku pojawia się w polu, wyświetla się informacja o ilości stron i wersji PDF. |
| W sekcji "Ustawienia dzielenia" zaznacz opcję "Podziel po następujących numerach stron" | Opcja zostaje wybrana. Pozostałe pola tekstowe w tej sekcji stają się nieaktywne. |
| Wpisz w pole numery stron większy niż liczba stron w dokumencie np. "10" dla pliku 7 stronowego | Wartości zostają wprowadzone. |
| W sekcji "Ustawienia wyjściowe" kliknij "Przeglądaj" i wybierz folder docelowy. | Ścieżka folderu pojawia się w polu tekstowym. |
| W sekcji "Ustawienia nazw plików" zostaw domyślny przedrostek `PDFsam_`. | Przedrostek jest widoczny w polu. |
| Kliknij niebieski przycisk „Wykonaj”. | Program powinien zablokować wykonanie zadania lub wyświetlić czytelny komunikat o błędzie (np. "Zakres stron wykracza poza dokument"). |

Użyte pliki: `sample_pdfs/sampleB.pdf`

FAILED

BUG REPORT

- Summary: Niejasny komunikat o błędzie przy wprowadzeniu niepoprawnych danych do pól tekstowych w funkcji "Podział".
- Component: UI / UX
- Severity: Minor (nie wpływa na funkcjonalność, ale może powodować frustrację użytkownika)
- Description: W przypadku wprowadzenia numeru strony, po którym ma być podzielony plik, który wykracza poza liczbę stron w dokumencie, program powinien zablokować wykonanie zadania i wyświetlić czytelny komunikat o błędzie (np. "Zakres stron wykracza poza dokument"). Obecnie program pozwala na rozpoczęcie procesu. Po kliknięciu przycisku "Wykonaj" program wyświetla komunikat "Nie udało się". Po kliknięciu przycisku "Pokaż błędy" program wyświetla techniczne logi błędów, które nie są zrozumiałe dla przeciętnego użytkownika. Brak jasnego komunikatu o błędzie.
- Expected behavior: Program powinien zablokować wykonanie zadania i wyświetlić czytelny komunikat o błędzie (np. "Zakres stron wykracza poza dokument") w przypadku wprowadzenia niepoprawnych danych do pól tekstowych.
