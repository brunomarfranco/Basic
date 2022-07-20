P: Quando usar métodos na mesma linha e quando criar uma nova variável para isso?
R: Fazer o que for mais fácil se entender quando outro dev for ler; desenvolver o feeling, a sensibilidade.

P: É melhor usar com função ou sem? Quando usar cada um, pensando em legibilidade pro dev e processamento de HW?
R: Em geral, usar função traz mais legibilidade, pois o código fica dividido em porções bem desenhadas do que está executando.
Tentar manter a função entre 10-20 linhas de código (algo opinativo)

P: Quais recursos gastam mais memória?
R: For e While Loops alinhados (ou seja, um "dentro" do outro) aumentam exponencialmente o peso do programa (n, n², n³);
.insert e .remove têm um for loop dentro deles, pois movem todos os números. Priorizar o uso do .append!

O(log n) ("Ó de log n"): Análise/Complexidade do algoritmo. Estudar p/ entrevistas.
Log n subentende-se que é de 2 (na matemática é de 10)

Quando passar do limite horizontal da página, dar enter. Nunca deve-se precisar rolar à direita para ler o código.

Não abreviar demais a ponto de perder legibilidade. Isso era uma prática antes do auto-complete


P: Como remover um arquivo 'x' já comittado do Git?
R: git rm --cached x.py

