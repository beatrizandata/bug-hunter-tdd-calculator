"""
Reproduz os bugs do Calculadora.py descritos no Bugs.md.

Como o Calculadora.py executa o menu ao ser importado (bug #9), este script
roda o arquivo como um processo separado e envia as entradas do usuário
via stdin. Assim ele funciona antes e depois das correções.

Uso:  python reproduzir_bugs.py
"""
import re
import subprocess
import sys

ARQUIVO = "Calculadora.py"

# (número do bug, título, entradas digitadas, resultado esperado)
CENARIOS = [
    (1, "Adição soma x duas vezes", ["1", "2", "3", "n"], "Resultado: 5.0"),
    (2, "Divisão por zero sem tratamento", ["4", "5", "0", "n"], "mensagem de erro (sem exceção)"),
    (3, "Fatorial sempre retorna 0", ["7", "5", "n"], "Resultado: 120"),
    (4, "np.ln não existe", ["8", "2.718281828", "n"], "Resultado: ~1.0"),
    (5, "Log base 10 usa log natural", ["9", "100", "n"], "Resultado: 2.0"),
    (6, "Log base 10 aceita zero", ["9", "0", "n"], "Erro: Logaritmo de número não positivo"),
    (7, "Seno não implementado (opção 10)", ["10", "30", "n"], "Resultado: 0.5"),
    (7, "Cosseno não implementado (opção 11)", ["11", "60", "n"], "Resultado: 0.5"),
    (7, "Tangente não implementada (opção 12)", ["12", "45", "n"], "Resultado: 1.0"),
    (8, "Entrada inválida (texto)", ["1", "abc", "n"], "mensagem de entrada inválida"),
]


def executar(entradas):
    """Roda Calculadora.py enviando as entradas e devolve (saída, stderr)."""
    proc = subprocess.run(
        [sys.executable, ARQUIVO],
        input="\n".join(entradas) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    return proc.stdout, proc.stderr


def resumir(stdout, stderr):
    """Extrai a linha relevante da saída (resultado ou última linha do erro)."""
    linhas_erro = [l for l in stderr.strip().splitlines() if l.strip()]
    # O prompt do input() não quebra linha, então o resultado vem colado nele:
    # por isso a busca é feita dentro da linha, e não no início dela.
    achado = re.search(r"(Resultado:.*|Erro:.*|Operação inválida.*)", stdout)
    if achado:
        aviso = [l.strip() for l in linhas_erro if "Warning" in l]
        return achado.group(1) + (f"   [{aviso[0]}]" if aviso else "")
    if linhas_erro:
        return linhas_erro[-1]
    return "(sem saída)"


def bug_9():
    """Importar o módulo não deveria abrir o menu nem pedir entrada."""
    proc = subprocess.run(
        [sys.executable, "-c", "import Calculadora"],
        stdin=subprocess.DEVNULL,  # sem entrada disponível
        capture_output=True,
        text=True,
        timeout=10,
    )
    if proc.returncode == 0:
        return "import OK, sem executar o menu"
    erro = [l for l in proc.stderr.strip().splitlines() if l.strip()]
    return erro[-1] if erro else "falhou sem mensagem"


def main():
    print("=" * 70)
    print("REPRODUÇÃO DE BUGS: Calculadora.py")
    print("=" * 70)

    for numero, titulo, entradas, esperado in CENARIOS:
        stdout, stderr = executar(entradas)
        print(f"\n[Bug {numero}] {titulo}")
        print(f"  Entradas : {' -> '.join(entradas[:-1])}")
        print(f"  Esperado : {esperado}")
        print(f"  Obtido   : {resumir(stdout, stderr)}")

    print("\n[Bug 9] Execução automática ao importar o módulo")
    print("  Esperado : import OK, sem executar o menu")
    print(f"  Obtido   : {bug_9()}")

    print("\n" + "=" * 70)
    print("Compare 'Esperado' e 'Obtido' para cada bug.")


if __name__ == "__main__":
    main()
