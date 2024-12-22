from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document.")

    def scan_document(self):
        print("Scanning document.")


class BasicPrinter(Printer):
    def print_document(self):
        print("Printing document.")


printer = BasicPrinter()
printer.print_document()

mfp = MultiFunctionPrinter()
mfp.print_document()
mfp.scan_document()
