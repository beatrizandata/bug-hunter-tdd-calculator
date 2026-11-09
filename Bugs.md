# Relatório de Bugs: Calculadora Científica


## Resumo

| # | Título | Função / Local | Severidade | Status |
|---|--------|----------------|------------|--------|
| 1 | Adição soma `x` duas vezes | `adicao` | Alta | Não resolvido |
| 2 | Divisão por zero sem tratamento | `divisao` | Média | Não resolvido |
| 3 | Fatorial sempre retorna 0 | `fatorial` | Crítica | Não resolvido |
| 4 | `np.ln` não existe | `logaritmo_natural` | Alta | Não resolvido |
| 5 | Log base 10 usa logaritmo natural | `logaritmo_base10` | Alta | Não resolvido |
| 6 | Log base 10 aceita zero | `logaritmo_base10` | Média | Não resolvido |
| 7 | Seno, cosseno e tangente não implementados | Menu / `calculadora_cientifica` | Alta | Não resolvido |
| 8 | Entradas do usuário não validadas | `calculadora_cientifica` | Média | Não resolvido |
| 9 | Execução automática ao importar o módulo | Última linha do arquivo | Média | Não resolvido |

---

## Bug 1: Adição soma `x` duas vezes

### Identificação
- **Título:** Adição retorna resultado incorreto
- **Localização:** `Calculadora.py`, função `adicao`

### Descrição detalhada
- **Descrição:** A função retorna `x + np.add(x, y)`, ou seja, `x + (x + y)`. O primeiro operando é somado duas vezes. Toda adição realizada pela calculadora produz resultado errado.
- **Contexto:** Python 3.x com NumPy. Ocorre tanto na chamada direta quanto pelo menu (opção 1).

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `1` (Adição).
3. Informar `2` como primeiro número e `3` como segundo.
4. Observar o resultado.

- **Consistência:** Ocorre sempre, exceto quando `x = 0`.

### Resultado esperado vs. obtido
- **Esperado:** `5.0`
- **Obtido:** `7.0`

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  Resultado: 7.0
  ```

### Severidade e impacto
- **Severidade:** Alta
- **Impacto:** A operação mais básica da calculadora retorna valores errados, sem qualquer aviso. O usuário pode usar o resultado sem perceber o erro.

### Sugestão para correção
Retornar `x + y` (ou `np.add(x, y)`), sem somar `x` novamente.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 2: Divisão por zero sem tratamento

### Identificação
- **Título:** Divisão por zero derruba o programa
- **Localização:** `Calculadora.py`, função `divisao`

### Descrição detalhada
- **Descrição:** A função executa `x / y` sem verificar se `y` é zero. Ao dividir por zero, o Python lança `ZeroDivisionError` e o programa é encerrado. As demais funções (raiz quadrada, logaritmos) retornam mensagem de erro amigável, então o comportamento é inconsistente.
- **Contexto:** Pelo menu, os valores são convertidos com `float()`, então o erro é de divisão de float.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `4` (Divisão).
3. Informar `5` como primeiro número e `0` como segundo.
4. Observar o resultado.

- **Consistência:** Ocorre sempre que o divisor é zero.

### Resultado esperado vs. obtido
- **Esperado:** Mensagem como `Erro: Divisão por zero`, mantendo o programa em execução.
- **Obtido:** O programa é interrompido com exceção.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  Traceback (most recent call last):
    ...
  ZeroDivisionError: float division by zero
  ```

### Severidade e impacto
- **Severidade:** Média
- **Impacto:** Um erro comum de uso faz a calculadora fechar abruptamente, e o usuário perde a sessão.

### Sugestão para correção
Verificar `if y == 0` e retornar a mensagem de erro, no mesmo padrão das outras funções.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 3: Fatorial sempre retorna 0

### Identificação
- **Título:** Fatorial retorna 0 para qualquer entrada
- **Localização:** `Calculadora.py`, função `fatorial`

### Descrição detalhada
- **Descrição:** O laço usa `range(x+1)`, que começa em `0`. Na primeira iteração, `fat *= 0` zera o acumulador e todo o produto seguinte continua 0. Além disso, números negativos não são tratados: o laço não executa e a função retorna `1`, o que é matematicamente incorreto (o fatorial não é definido para negativos).
- **Contexto:** Ocorre pelo menu (opção 7) e na chamada direta da função.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `7` (Fatorial).
3. Informar `5`.
4. Observar o resultado.

- **Consistência:** Ocorre sempre, para qualquer `x >= 0`.

### Resultado esperado vs. obtido
- **Esperado:** `fatorial(5) = 120`, `fatorial(0) = 1`, `fatorial(-3)` com mensagem de erro.
- **Obtido:** `fatorial(5) = 0`, `fatorial(0) = 0`, `fatorial(-3) = 1`.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  Resultado: 0
  ```

### Severidade e impacto
- **Severidade:** Crítica
- **Impacto:** A operação nunca funciona corretamente. Qualquer cálculo que dependa do fatorial está errado.

### Sugestão para correção
Iniciar o laço em 1 (`range(1, x + 1)`) ou usar `math.factorial`. Tratar `x < 0` com mensagem de erro.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido _(bug escolhido para correção via TDD)_

---

## Bug 4: `np.ln` não existe

### Identificação
- **Título:** Logaritmo natural lança `AttributeError`
- **Localização:** `Calculadora.py`, função `logaritmo_natural`

### Descrição detalhada
- **Descrição:** A função chama `np.ln(x)`, mas o NumPy não possui essa função. O logaritmo natural no NumPy é `np.log`. Com isso, a operação falha para qualquer entrada válida.
- **Contexto:** Ocorre pelo menu (opção 8) e na chamada direta.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `8` (Logaritmo Natural).
3. Informar `2.718281828`.
4. Observar o resultado.

- **Consistência:** Ocorre sempre para `x > 0`.

### Resultado esperado vs. obtido
- **Esperado:** Aproximadamente `1.0`.
- **Obtido:** O programa é interrompido com exceção.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  AttributeError: module 'numpy' has no attribute 'ln'
  ```

### Severidade e impacto
- **Severidade:** Alta
- **Impacto:** A funcionalidade está totalmente inoperante e o programa fecha com erro.

### Sugestão para correção
Trocar `np.ln(x)` por `np.log(x)`.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 5: Logaritmo base 10 usa o logaritmo natural

### Identificação
- **Título:** `logaritmo_base10` calcula ln em vez de log10
- **Localização:** `Calculadora.py`, função `logaritmo_base10`

### Descrição detalhada
- **Descrição:** A função retorna `np.log(x)`, que é o logaritmo natural. Para base 10, o correto é `np.log10(x)`. O resultado é sempre diferente do esperado (exceto para `x = 1`).
- **Contexto:** Ocorre pelo menu (opção 9) e na chamada direta.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `9` (Logaritmo Base 10).
3. Informar `100`.
4. Observar o resultado.

- **Consistência:** Ocorre sempre, para `x > 1` ou `0 < x < 1`.

### Resultado esperado vs. obtido
- **Esperado:** `2.0`
- **Obtido:** `4.605170185988092`

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  Resultado: 4.605170185988092
  ```

### Severidade e impacto
- **Severidade:** Alta
- **Impacto:** Resultado incorreto sem nenhum aviso, o que pode induzir o usuário a erro.

### Sugestão para correção
Trocar `np.log(x)` por `np.log10(x)`.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 6: Logaritmo base 10 aceita zero

### Identificação
- **Título:** Validação incorreta em `logaritmo_base10`
- **Localização:** `Calculadora.py`, função `logaritmo_base10`

### Descrição detalhada
- **Descrição:** A condição é `x < 0`, então `x = 0` passa pela validação, embora o logaritmo de zero não seja definido. A mensagem de erro diz "não positivo", o que indica que a intenção era `x <= 0` (como em `logaritmo_natural`).
- **Contexto:** Ocorre pelo menu (opção 9) e na chamada direta.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `9` (Logaritmo Base 10).
3. Informar `0`.
4. Observar o resultado.

- **Consistência:** Ocorre sempre com `x = 0`.

### Resultado esperado vs. obtido
- **Esperado:** `Erro: Logaritmo de número não positivo`
- **Obtido:** `-inf`, acompanhado de aviso do NumPy.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  RuntimeWarning: divide by zero encountered in log
  Resultado: -inf
  ```

### Severidade e impacto
- **Severidade:** Média
- **Impacto:** Um valor inválido é devolvido como se fosse resultado, e o comportamento difere do logaritmo natural.

### Sugestão para correção
Alterar a condição para `x <= 0`.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 7: Seno, cosseno e tangente não implementados

### Identificação
- **Título:** Operações trigonométricas ausentes ou quebradas
- **Localização:** `Calculadora.py`, função `menu` e `calculadora_cientifica` (opções 10, 11 e 12)

### Descrição detalhada
- **Descrição:** O menu anuncia seno (10), cosseno (11) e tangente (12), mas:
  - a opção 10 não tem ramo no `if/elif` e cai em "Operação inválida";
  - as funções `cosseno` e `tangente` (opções 11 e 12) são chamadas mas nunca foram definidas;
  - a chamada `tangente(x, radianos=False)` usa um parâmetro que também não existe.
- **Contexto:** Ocorre pelo menu. O arquivo não define nenhuma função trigonométrica.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `10`, depois repetir escolhendo `11` e informando `60`, e depois `12` com `45`.
3. Observar os resultados.

- **Consistência:** Ocorre sempre.

### Resultado esperado vs. obtido
- **Esperado:** Opção 10 com 30° retorna `0.5`. Opção 11 com 60° retorna `0.5`. Opção 12 com 45° retorna `1.0`.
- **Obtido:** Opção 10 exibe "Operação inválida. Tente novamente." As opções 11 e 12 encerram o programa com exceção.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  NameError: name 'cosseno' is not defined
  NameError: name 'tangente' is not defined
  ```

### Severidade e impacto
- **Severidade:** Alta
- **Impacto:** Três funcionalidades anunciadas no menu estão indisponíveis, e duas delas derrubam o programa.

### Sugestão para correção
Implementar `seno`, `cosseno` e `tangente` (com conversão de graus para radianos via `np.radians`), adicionar o ramo da opção 10 e tratar a tangente de 90° (valor indefinido).

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 8: Entradas do usuário não validadas

### Identificação
- **Título:** Entrada inválida causa `ValueError`
- **Localização:** `Calculadora.py`, função `calculadora_cientifica` (chamadas a `float()` e `int()`)

### Descrição detalhada
- **Descrição:** As entradas numéricas são convertidas diretamente com `float(input())` e `int(input())`, sem `try/except`. Texto ou campo vazio causa `ValueError`. Na opção 7 (fatorial), digitar um decimal como `3.5` também causa erro, pois a conversão usa `int()`.
- **Contexto:** Ocorre em todas as operações que pedem números.

### Passos para reproduzir
1. Executar `python Calculadora.py`.
2. Escolher a opção `1`.
3. No primeiro número, digitar `abc`.
4. Observar o resultado.

- **Consistência:** Ocorre sempre com entrada não numérica.

### Resultado esperado vs. obtido
- **Esperado:** Mensagem como "Entrada inválida" e nova solicitação do valor.
- **Obtido:** O programa é interrompido com exceção.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  ValueError: could not convert string to float: 'abc'
  ```

### Severidade e impacto
- **Severidade:** Média
- **Impacto:** Um erro de digitação encerra a calculadora e prejudica a usabilidade.

### Sugestão para correção
Envolver as leituras em `try/except ValueError` (ou criar uma função auxiliar de leitura) e pedir o valor novamente.

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Bug 9: Execução automática ao importar o módulo

### Identificação
- **Título:** `calculadora_cientifica()` é executada na importação
- **Localização:** `Calculadora.py`, última linha

### Descrição detalhada
- **Descrição:** A chamada `calculadora_cientifica()` está no nível do módulo, sem `if __name__ == "__main__":`. Ao importar o arquivo (por exemplo, em um teste com pytest), o menu é exibido e o programa fica esperando `input()`. Isso impossibilita testes automatizados.
- **Contexto:** Afeta qualquer `import Calculadora` ou `from Calculadora import ...`.

### Passos para reproduzir
1. Criar um arquivo `test_calculadora.py` com `from Calculadora import fatorial`.
2. Executar `pytest`.
3. Observar o resultado.

- **Consistência:** Ocorre sempre.

### Resultado esperado vs. obtido
- **Esperado:** A importação apenas carrega as funções, e o menu só roda ao executar `python Calculadora.py`.
- **Obtido:** O menu é exibido na importação e o pytest falha ao tentar ler a entrada padrão.

### Evidências
- **Screenshot:** _inserir print do terminal_
- **Log:**
  ```
  OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
  ```

### Severidade e impacto
- **Severidade:** Média
- **Impacto:** Impede testes automatizados e o reaproveitamento das funções em outros módulos. É pré-requisito para aplicar TDD.

### Sugestão para correção
Substituir a última linha por:
```python
if __name__ == "__main__":
    calculadora_cientifica()
```

### Registro e acompanhamento
- **Data de identificação:** 09/11/2026
- **Status:** Não resolvido

---

## Observações de design (baixa severidade)

- Funções como `raiz_quadrada` devolvem **strings de erro** em vez de lançar exceções, o que mistura tipos de retorno (número e texto).
- A repetição do menu usa **recursão** (`calculadora_cientifica()` chama a si mesma), então muitas repetições podem estourar o limite de recursão. Um laço `while` seria mais adequado.

---

## Correção aplicada (preencher após o TDD)

- **Bug corrigido:** #3, Fatorial sempre retorna 0
- **O que foi alterado:** _descrever_
- **Por que foi alterado:** _descrever_
- **Como resolve o bug:** _descrever_
- **Testes:** _listar os testes e o resultado do `pytest`_
- **Commit:** _hash ou mensagem do commit_
