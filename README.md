# 🧮 Calculadora Python

Calculadora de linha de comando implementada com **Programação Orientada a Objetos (POO)**, oferecendo operações matemáticas básicas e avançadas com histórico de operações e logging robusto.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Code Quality](https://img.shields.io/badge/Code%20Quality-Professional-success)

---

## 🎯 Funcionalidades

- ✅ **7 Operações Básicas** - Soma, subtração, multiplicação, divisão, potência, divisão inteira, módulo
- ✅ **Raiz Quadrada** - Operação especial com validação
- ✅ **Histórico de Operações** - Acompanhe as últimas 5 operações da sessão
- ✅ **Logging de Erros** - Registro automático de erros em arquivo
- ✅ **Validação Robusta** - Tratamento de divisão por zero, números negativos, etc
- ✅ **Interface CLI Intuitiva** - Menu navegável e mensagens claras
- ✅ **POO Profissional** - Código modular e reutilizável
- ✅ **Sem Dependências Externas** - Usa apenas `math` e `logging` (stdlib)

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Descrição |
|---|---|---|
| **Python** | 3.8+ | Linguagem principal |
| **math** | Built-in | Operações matemáticas avançadas |
| **logging** | Built-in | Sistema de logs |

**Nenhuma dependência externa!** Usa apenas a biblioteca padrão do Python.

---

## 📦 Instalação

### Pré-requisitos

```bash
# Verifique se Python 3.8+ está instalado
python3 --version

# Se não estiver, instale:
# Ubuntu/Debian
sudo apt-get install python3

# Fedora
sudo dnf install python3

# macOS
brew install python3
```

### Setup Rápido

```bash
# Clone o repositório
git clone https://github.com/PSilvestree/calculadora-python.git
cd calculadora-python

# Execute a calculadora
python3 calculadora.py
```

✅ **Pronto!** A calculadora iniciará no seu terminal.

---

## 🚀 Como Usar

### Executar a Calculadora

```bash
python3 calculadora.py
```

### Interface

```
========================================
          CALCULADORA PYTHON
========================================
  1. Somar              (+)
  2. Subtrair           (-)
  3. Multiplicar        (×)
  4. Dividir            (÷)
  5. Potência           (^)
  6. Divisão Inteira    (//)
  7. Módulo / Resto     (%)
  8. Raiz Quadrada      (√)
  0. Sair
========================================
  Escolha uma opção: 
```

---

## 📋 Exemplos de Uso

### Exemplo 1: Soma Simples

```
Escolha uma opção: 1
  Primeiro número: 10
  Segundo número: 5

✅ Resultado: 10 + 5 = 15

📋 Histórico desta sessão:
   1. 10 + 5 = 15
```

### Exemplo 2: Divisão com Tratamento de Erro

```
Escolha uma opção: 4
  Primeiro número: 100
  Segundo número: 0

❌ Erro: Divisão por zero não é permitida.
```

### Exemplo 3: Raiz Quadrada

```
Escolha uma opção: 8
  Número: 144

✅ Resultado: √144 = 12
```

### Exemplo 4: Operações Avançadas

```
Escolha uma opção: 5
  Primeiro número: 2
  Segundo número: 10

✅ Resultado: 2 ^ 10 = 1024

---

Escolha uma opção: 7
  Primeiro número: 17
  Segundo número: 5

✅ Resultado: 17 % 5 = 2
```

---

## 📂 Estrutura do Projeto

```
calculadora-python/
├── calculadora.py         # Arquivo principal
├── calculadora.log        # Logs de erros (gerado automaticamente)
├── requirements.txt       # Dependências (vazio - só stdlib)
├── tests/
│   └── test_calculadora.py # Testes unitários (opcional)
└── README.md             # Esta documentação
```

---

## 🔍 Análise de Código

### Arquitetura

A calculadora segue o padrão **POO** com separação clara de responsabilidades:

```python
class Calculadora:
    ├── Operações (métodos estáticos)
    │   ├── somar()
    │   ├── subtrair()
    │   ├── multiplicar()
    │   ├── dividir()
    │   ├── potencia()
    │   ├── divisao_inteira()
    │   ├── modulo()
    │   └── raiz_quadrada()
    │
    ├── Utilitários
    │   ├── formatar_resultado()
    │   ├── registrar_historico()
    │   └── exibir_historico()
    │
    └── Interface
        ├── exibir_menu()
        ├── ler_numero()
        └── executar() [loop principal]
```

### Dicionário de Operações

Padrão profissional que torna o código extensível:

```python
self.acoes: dict = {
    "1": (self.somar,        "+"),
    "2": (self.subtrair,     "-"),
    "3": (self.multiplicar,  "×"),
    "4": (self.dividir,      "÷"),
    "5": (self.potencia,     "^"),
    "6": (self.divisao_inteira, "//"),
    "7": (self.modulo,       "%"),
}
```

**Vantagem:** Adicionar nova operação é trivial!

### Tratamento de Erros

```python
try:
    resultado = func(a, b)
except (ZeroDivisionError, ValueError) as e:
    logging.error("Erro na operação: %s", e)
    print(f"❌ Erro: {e}")
```

---

## 💡 Usando como Módulo

Você pode importar a `Calculadora` em outros projetos:

```python
from calculadora import Calculadora

# Criar instância
calc = Calculadora()

# Operações diretas
resultado = calc.somar(10, 5)
print(resultado)  # 15

resultado = calc.multiplicar(7, 8)
print(resultado)  # 56

resultado = calc.raiz_quadrada(144)
print(resultado)  # 12.0

# Usar em cálculos em cadeia
total = calc.somar(
    calc.multiplicar(10, 5),
    calc.dividir(100, 2)
)
print(total)  # 100
```

---

## 📊 Operações Detalhadas

| Operação | Símbolo | Exemplo | Resultado |
|----------|---------|---------|-----------|
| Soma | + | 10 + 5 | 15 |
| Subtração | - | 10 - 3 | 7 |
| Multiplicação | × | 4 × 7 | 28 |
| Divisão | ÷ | 20 ÷ 4 | 5 |
| Potência | ^ | 2 ^ 8 | 256 |
| Divisão Inteira | // | 17 // 5 | 3 |
| Módulo | % | 17 % 5 | 2 |
| Raiz Quadrada | √ | √144 | 12 |

---

## 📝 Sistema de Logging

Erros são registrados automaticamente em `calculadora.log`:

```
2026-04-25 10:30:45,123 - ERROR - Erro na operação: Divisão por zero não é permitida.
2026-04-25 10:31:12,456 - ERROR - Erro na operação: Raiz quadrada de número negativo não é definida.
```

**Verificar logs:**
```bash
cat calculadora.log

# Ou monitorar em tempo real
tail -f calculadora.log
```

---

## 🧪 Testes

### Teste Manual (Rápido)

```bash
python3 calculadora.py
# Digite operações e verifique os resultados
```

### Teste Programático

```python
from calculadora import Calculadora

calc = Calculadora()

# Testes básicos
assert calc.somar(2, 3) == 5
assert calc.subtrair(10, 4) == 6
assert calc.multiplicar(3, 4) == 12
assert calc.dividir(20, 4) == 5.0
assert calc.potencia(2, 3) == 8
assert calc.divisao_inteira(17, 5) == 3
assert calc.modulo(17, 5) == 2
assert calc.raiz_quadrada(144) == 12.0

print("✅ Todos os testes passaram!")
```

### Teste com pytest (Recomendado)

```bash
# Instale pytest
pip install pytest

# Execute testes
pytest tests/test_calculadora.py -v
```

**Arquivo `tests/test_calculadora.py`:**

```python
import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_somar(calc):
    assert calc.somar(10, 5) == 15

def test_subtrair(calc):
    assert calc.subtrair(10, 3) == 7

def test_multiplicar(calc):
    assert calc.multiplicar(4, 7) == 28

def test_dividir(calc):
    assert calc.dividir(20, 4) == 5.0

def test_dividir_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)

def test_raiz_quadrada(calc):
    assert calc.raiz_quadrada(144) == 12.0

def test_raiz_quadrada_negativa(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-1)
```

---

## 🔧 Personalização

### Adicionar Nova Operação

1. **Adicione o método:**

```python
@staticmethod
def logaritmo(a: float, b: float = 10) -> float:
    """Logaritmo de a na base b (padrão: base 10)"""
    if a <= 0:
        raise ValueError("Logaritmo de números não-positivos não é definido.")
    return math.log(a, b)
```

2. **Registre no dicionário:**

```python
self.acoes["9"] = (self.logaritmo, "log")
```

3. **Atualize o menu:**

```python
print("  9. Logaritmo         (log)")
```

### Mudar Tema de Cores

Adicione emojis ou símbolos personalizados nas mensagens:

```python
print("✨ Bem-vindo à Calculadora Python!")  # Altere os emojis
```

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'math'"

- **Solução:** `math` é built-in, não precisa instalar. Verifique sua instalação Python.

### Problema: Resultado com muitas casas decimais

- **Solução:** Veja a função `formatar_resultado()` que limita a 6 dígitos significativos.

### Problema: Histórico não aparece

- **Solução:** Execute pelo menos uma operação antes de sair, ou altere:

```python
# Aumentar número de operações no histórico
for i, item in enumerate(self.historico[-10:], 1):  # Aumentar de 5 para 10
    print(f"     {i}. {item}")
```

---

## 📈 Roadmap (Futuras Melhorias)

- [ ] **GUI com Tkinter** - Interface gráfica
- [ ] **Modo científico** - Trigonometria, logaritmo, etc
- [ ] **Modo complexo** - Números complexos
- [ ] **Testes unitários** - pytest completo
- [ ] **Suporte a frações** - Operações com frações
- [ ] **Histórico persistente** - Salvar em arquivo
- [ ] **Avaliador de expressões** - `3 + 4 * 2` → 11
- [ ] **Conversão de unidades** - Metros para pés, etc
- [ ] **Gráfico de funções** - matplotlib integration
- [ ] **Export de histórico** - CSV, JSON, PDF

---

## 🤝 Contribuições

Melhorias são bem-vindas! Como contribuir:

1. **Fork** o repositório
2. **Crie uma branch:** `git checkout -b feature/nova-operacao`
3. **Implemente a feature** com testes
4. **Commit:** `git commit -m 'Adiciona logaritmo'`
5. **Push:** `git push origin feature/nova-operacao`
6. **Pull Request:** Descreva sua mudança

---

## 📄 Licença

MIT - Libre para uso pessoal e comercial. Veja [LICENSE](LICENSE).

---

## 👨‍💻 Autor

**Paulo Silvestre**  
*Mestrando em História • Universidade Estadual de Maringá (UEM)*  
Apaixonado por algoritmos e história! 📚🧮

- 🔗 **LinkedIn:** [paulosilvestree](https://www.linkedin.com/in/paulosilvestree)
- 🐙 **GitHub:** [@PSilvestree](https://github.com/PSilvestree)

---

## 📚 Referências

- [Python Documentation - math](https://docs.python.org/3/library/math.html)
- [Python OOP Guide](https://docs.python.org/3/tutorial/classes.html)
- [Logging in Python](https://docs.python.org/3/library/logging.html)
- [PEP 8 - Style Guide](https://pep8.org/)

---

**Versão:** 1.0.0  
**Última atualização:** 2026-04-25  
**Status:** Desenvolvimento ativo ✨
