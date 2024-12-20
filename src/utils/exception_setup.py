"""
exception_setup.py

Dieses Skript enthält eine benutzerdefinierte Ausnahmeklasse `CustomException` und eine Hilfsfunktion `error_message_detail`, 
die zusammen eine erweiterte Fehlerbehandlung in Python-Projekten ermöglichen.

Funktionen:
- **error_message_detail**: Erstellt eine detaillierte Fehlermeldung, die den Ursprung eines Fehlers mit Dateinamen und Zeilennummer
  angibt. Dies erleichtert das Debugging und die Fehlerdiagnose.

Klassen:
- **CustomException**: Erweitert die Standard-Ausnahmebehandlung in Python und fügt detaillierte Informationen zu einem Fehler hinzu, 
  einschließlich des Ortes, an dem der Fehler auftrat, und der vollständigen Fehlermeldung.

Typische Verwendung:
- Dieses Modul wird importiert und in Projekten verwendet, bei denen Fehler präzise dokumentiert und analysiert werden müssen.
- Die `CustomException`-Klasse ersetzt die Standard-Ausnahmen und ermöglicht eine erweiterte Protokollierung und Fehlerverfolgung.

Beispiel:
    try:
        x = 1 / 0  # Löst eine ZeroDivisionError aus
    except Exception as e:
        raise CustomException(e, sys)

Erzeugt folgende Fehlermeldung:
    Error occurred in python script name [example.py] line number [12] error message [division by zero]
"""
# Import
import sys


# error_message_detail
def error_message_detail(error, error_detail: sys):
    """
    Erstellt eine detaillierte Fehlermeldung mit Informationen über den Ursprung des Fehlers.

    Args:
        error (Exception): Das aufgetretene Fehlerobjekt.
        error_detail (sys): Das sys-Modul, um auf die Ausnahmeinformationen zuzugreifen.

    Returns:
        str: Eine formatierte Fehlermeldung mit dem Dateinamen, der fehlerhaften Zeilennummer und der Fehlermeldung.
    """
    # Extrahiere die traceback-Informationen
    _, _, exc_tb = error_detail.exc_info()
    
    # Hole den Namen der Datei, in der der Fehler auftrat
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Formatiere die detaillierte Fehlermeldung
    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] error message [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))
    
    return error_message


# Klasse CostumException
class CustomException(Exception):
    """
    Eine benutzerdefinierte Ausnahmeklasse, die zusätzliche Kontextinformationen über Fehler liefert.

    Attribute:
        error_message (str): Die detaillierte Fehlermeldung, die den Fehler beschreibt.

    Methods:
        __str__: Gibt die detaillierte Fehlermeldung als Zeichenkette zurück.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Initialisiert die CustomException mit einer detaillierten Fehlermeldung.

        Args:
            error_message (Exception): Das aufgetretene Fehlerobjekt.
            error_detail (sys): Das sys-Modul, um auf die Ausnahmeinformationen zuzugreifen.
        """
        super().__init__(error_message)
        
        # Generiere eine detaillierte Fehlermeldung
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        """
        Gibt die detaillierte Fehlermeldung als Zeichenkette zurück.

        Returns:
            str: Die detaillierte Fehlermeldung.
        """
        return self.error_message
