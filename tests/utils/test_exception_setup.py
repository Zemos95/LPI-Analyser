"""
test_exception_setup.py

Dieses Skript enthält Tests für das Modul `exception_setup.py`, das eine benutzerdefinierte Ausnahmeklasse `CustomException` 
und die Hilfsfunktion `error_message_detail` bereitstellt. 

Ziel dieser Tests ist es, die Korrektheit und Robustheit der Fehlerbehandlungslogik zu gewährleisten.

Funktionen:
- **test_error_message_detail**:
    Testet die Funktion `error_message_detail` aus dem Modul `exception_setup.py`. 
    Es wird überprüft, ob die generierte Fehlermeldung den Dateinamen, die Zeilennummer und die Fehlermeldung korrekt enthält.

- **test_custom_exception**:
    Testet die benutzerdefinierte Ausnahme `CustomException`. Es wird sichergestellt, dass die erzeugte Fehlermeldung 
    die erwarteten Informationen über den Fehler (z. B. Dateiname, Zeilennummer, Fehlermeldung) enthält.

Typische Verwendung:
- Dieses Testskript wird mit `pytest` ausgeführt, um sicherzustellen, dass die Funktionen und Klassen des Moduls `exception_setup.py`
  wie erwartet funktionieren.
- Die Tests sind isoliert und haben keine Auswirkungen auf andere Teile des Projekts.

Beispiel zur Testausführung:
    pytest tests/utils/test_exception_setup.py

Erwartetes Ergebnis:
- Alle Tests sollten erfolgreich sein, wenn die Implementierung in `exception_setup.py` korrekt ist.
"""
# Import
import pytest
import sys
import os

# Füge das Verzeichnis mit exception_setup.py zum Python-Pfad hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/utils")))

from src.utils.exception_setup import CustomException, error_message_detail

def test_error_message_detail():
    """Testet, ob error_message_detail eine korrekt formatierte Fehlermeldung zurückgibt."""
    try:
        # Erzeuge absichtlich einen Fehler
        1 / 0
    except ZeroDivisionError as e:
        # Übergebe die Ausnahmeinformationen direkt an die Funktion
        error_message = error_message_detail(e, sys)
        assert "division by zero" in error_message, "Die Fehlermeldung enthält nicht den erwarteten Text."
        assert "test_exception_setup.py" in error_message, "Die Fehlermeldung enthält nicht den Dateinamen."
        assert "line number" in error_message, "Die Fehlermeldung enthält keine Zeilennummer."

def test_custom_exception():
    """Testet, ob CustomException korrekt initialisiert wird."""
    with pytest.raises(CustomException) as excinfo:
        try:
            1 / 0  # Löst einen ZeroDivisionError aus
        except ZeroDivisionError as e:
            raise CustomException(e, sys)

    # Überprüfe die Fehlermeldung der CustomException
    error_message = str(excinfo.value)
    assert "division by zero" in error_message, "Die CustomException enthält nicht die erwartete Fehlermeldung."
    assert "test_exception_setup.py" in error_message, "Die CustomException enthält nicht den Dateinamen."
    assert "line number" in error_message, "Die CustomException enthält keine Zeilennummer."
