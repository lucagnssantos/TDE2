# Deadlock
deadlock_reprodução:

<img width="307" height="172" alt="image" src="https://github.com/user-attachments/assets/acc74041-b758-476e-b42e-81663c353edc" />


deadlock_corrigido:

<img width="267" height="169" alt="image" src="https://github.com/user-attachments/assets/aa3397d9-680d-4c9a-9285-c24f5690b76e" />

Por que ocorre o deadlock?
Na versão problemática:

T1 adquire o Lock A.
T2 adquire o Lock B.
T1 espera o Lock B.
T2 espera o Lock A.

Cada thread fica aguardando um recurso que está em posse da outra, formando um ciclo de espera.

Condições de Coffman presentes
Exclusão mútua
Apenas uma thread pode possuir cada lock por vez.
Manter e esperar
Cada thread mantém um lock enquanto aguarda outro.
Não preempção
O lock não pode ser retirado à força da thread que o possui.
Espera circular
T1 espera B enquanto possui A.
T2 espera A enquanto possui B.

Como as quatro condições estão presentes simultaneamente, ocorre deadlock.
