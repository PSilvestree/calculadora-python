"""
Calculadora em Python
Refatorada com POO, dicionário de operações e boas práticas.
"""

import math
import logging

# Configuração do logging
logging.basicConfig(
    filename="calculadora.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Calculadora:
    """Classe principal da calculadora com histórico de operações."""

    def __init__(self):
        self.historico: list[str] = []
        self.acoes: dict = {
            "1": (self.somar,        "+"),
            "2": (self.subtrair,     "-"),
            "3": (self.multiplicar,  "×"),
            "4": (self.dividir,      "÷"),
            "5": (self.potencia,     "^"),
            "6": (self.divisao_inteira, "//"),
            "7": (self.modulo,       "%"),
        }

    # ------------------------------------------------------------------ #
    #  Operações                                                           #
    # ------------------------------------------------------------------ #

    @staticmethod
    def somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def dividir(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b

    @staticmethod
    def divisao_inteira(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a // b

    @staticmethod
    def potencia(a: float, b: float) -> float:
        return a ** b

    @staticmethod
    def modulo(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a % b

    @staticmethod
    def raiz_quadrada(a: float) -> float:
        if a < 0:
            raise ValueError("Raiz quadrada de número negativo não é definida.")
        return math.sqrt(a)

    # ------------------------------------------------------------------ #
    #  Utilitários                                                         #
    # ------------------------------------------------------------------ #

    @staticmethod
    def formatar_resultado(valor: float) -> str:
        """Exibe inteiro se não houver casas decimais."""
        if valor == int(valor):
            return str(int(valor))
        return f"{valor:.6g}"

    def registrar_historico(self, operacao: str, resultado: float) -> None:
        entrada = f"{operacao} = {self.formatar_resultado(resultado)}"
        self.historico.append(entrada)

    def exibir_historico(self) -> None:
        if not self.historico:
            return
        print("\n  📋 Histórico desta sessão:")
        for i, item in enumerate(self.historico[-5:], 1):
            print(f"     {i}. {item}")

    # ------------------------------------------------------------------ #
    #  Interface de usuário                                                #
    # ------------------------------------------------------------------ #

    @staticmethod
    def exibir_menu() -> None:
        print("\n" + "=" * 40)
        print("          CALCULADORA PYTHON")
        print("=" * 40)
        print("  1. Somar              (+)")
        print("  2. Subtrair           (-)")
        print("  3. Multiplicar        (×)")
        print("  4. Dividir            (÷)")
        print("  5. Potência           (^)")
        print("  6. Divisão Inteira    (//)")
        print("  7. Módulo / Resto     (%)")
        print("  8. Raiz Quadrada      (√)")
        print("  0. Sair")
        print("=" * 40)

    @staticmethod
    def ler_numero(mensagem: str) -> float:
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("  ⚠ Por favor, insira um número válido.")

    def executar(self) -> None:
        """Loop principal da calculadora."""
        print("\nBem-vindo à Calculadora Python!")

        while True:
            self.exibir_menu()
            opcao = input("  Escolha uma opção: ").strip()

            if opcao == "0":
                print("\nEncerrando a calculadora. Até mais! 👋\n")
                break

            try:
                if opcao in self.acoes:
                    func, simbolo = self.acoes[opcao]
                    a = self.ler_numero("  Primeiro número: ")
                    b = self.ler_numero("  Segundo número:  ")
                    resultado = func(a, b)
                    operacao = f"{self.formatar_resultado(a)} {simbolo} {self.formatar_resultado(b)}"

                elif opcao == "8":
                    a = self.ler_numero("  Número: ")
                    resultado = self.raiz_quadrada(a)
                    operacao = f"√{self.formatar_resultado(a)}"

                else:
                    print("\n  ⚠ Opção inválida. Tente novamente.")
                    continue

                print(f"\n  ✅ Resultado: {operacao} = {self.formatar_resultado(resultado)}")
                self.registrar_historico(operacao, resultado)

            except (ZeroDivisionError, ValueError) as e:
                logging.error("Erro na operação: %s", e)
                print(f"\n  ❌ Erro: {e}")

            self.exibir_historico()


if __name__ == "__main__":
    calc = Calculadora()
    calc.executar()