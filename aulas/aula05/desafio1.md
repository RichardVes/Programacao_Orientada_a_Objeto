## Exercício 1: Sistema de Processamento de Pagamentos para E-commerce

### **Contexto**

Você foi contratado para desenvolver um módulo de pagamentos de um e-commerce que deve integrar múltiplos gateways (PayPal, Stripe, Mercado Pago). Cada gateway tem regras distintas:

- O PayPal cobra uma taxa fixa de 2% por transação.
- O Stripe permite estorno total apenas em até 7 dias.
- O Mercado Pago exige um token de segurança e limita transações a R$ 10.000.

---

### **Tarefa**

1. Projete classes para cada gateway usando herança e polimorfismo, garantindo que novos gateways sejam adicionados sem modificar o código existente.
2. Implemente um método abstrato `processar_pagamento(valor)` que retorne o ID da transação, custo de processamento e status.
3. Adicione exceções personalizadas para:
   - Valores excedentes (transações acima de R$ 10.000 no Mercado Pago).
   - Tokens inválidos (Mercado Pago).
   - Estornos fora do prazo (Stripe).
