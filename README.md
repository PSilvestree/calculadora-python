# 🧮 Calculadora Python

Calculadora de console desenvolvida em Python com boas práticas de desenvolvimento, incluindo Programação Orientada a Objetos, tratamento de erros, logging e testes unitários.

---

## 📋 Funcionalidades

| Opção | Operação          | Símbolo |
|-------|-------------------|---------|
| 1     | Somar             | +       |
| 2     | Subtrair          | -       |
| 3     | Multiplicar       | ×       |
| 4     | Dividir           | ÷       |
| 5     | Potência          | ^       |
| 6     | Divisão Inteira   | //      |
| 7     | Módulo / Resto    | %       |
| 8     | Raiz Quadrada     | √       |

- ✅ Histórico das últimas 5 operações da sessão
- ✅ Validação de entradas inválidas
- ✅ Registro de erros em arquivo `.log`

---

## 📁 Estrutura do Projeto

```
calculadora-python/
├── calculadora.py        # Código principal
├── test_calculadora.py   # Testes unitários com pytest
├── calculadora.log       # Gerado automaticamente ao ocorrer erros
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior

### Rodando a calculadora

```bash
python calculadora.py
```

### Rodando os testes

Instale o pytest caso ainda não tenha:

```bash
pip install pytest
```

Execute os testes:

```bash
pytest test_calculadora.py -v
```

Resultado esperado:

```
35 passed in 0.17s
```

---

## 🏗️ Decisões Técnicas

### Orientação a Objetos
Toda a lógica foi encapsulada na classe `Calculadora`. O histórico de operações e o dicionário de ações são atributos da instância, tornando o estado coeso e fácil de gerenciar.

### Dicionário de operações
Em vez de um bloco extenso de `if/elif`, as operações são mapeadas em um dicionário:

```python
self.acoes = {
    "1": (self.somar,     "+"),
    "2": (self.subtrair,  "-"),
    ...
}
```

Isso torna a adição de novas operações trivial — basta inserir uma nova entrada no dicionário.

### Métodos estáticos
As operações matemáticas são declaradas com `@staticmethod` por não dependerem do estado da instância, deixando clara a separação entre lógica pura e estado da aplicação.

### Tratamento de erros
- `ZeroDivisionError` — usado nativamente para divisões por zero
- `ValueError` — para entradas inválidas como raiz de número negativo
- Todos os erros são registrados automaticamente em `calculadora.log` via módulo `logging`

---

## 🧪 Cobertura de Testes

Os testes estão organizados por classe de operação:

| Classe de Teste          | O que cobre                                      |
|--------------------------|--------------------------------------------------|
| `TestSomar`              | Positivos, negativos, zero e floats              |
| `TestSubtrair`           | Resultado positivo, negativo e zero              |
| `TestMultiplicar`        | Casos com zero, negativos e sinais opostos       |
| `TestDividir`            | Divisão exata, float, negativo e por zero        |
| `TestDivisaoInteira`     | Arredondamento e divisão por zero                |
| `TestPotencia`           | Expoente positivo, zero, negativo e fracionário  |
| `TestRaizQuadrada`       | Raiz perfeita, zero, float e número negativo     |
| `TestModulo`             | Resto básico, divisão exata e por zero           |
| `TestHistorico`          | Estado inicial, registro e acúmulo               |
| `TestFormatarResultado`  | Inteiros, floats e negativos                     |

---

## 💡 Possíveis Melhorias Futuras

- [ ] Interface gráfica com Tkinter
- [ ] Exportar histórico para arquivo `.txt` ou `.csv`
- [ ] Suporte a expressões livres como `3 + 5 * 2`
- [ ] Medição de cobertura de testes com `pytest-cov`

---

## 👨‍💻 Autor

Desenvolvido como projeto de estudo em Python — aplicando POO, boas práticas e testes unitários.
