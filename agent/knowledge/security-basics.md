# Fundamentos de segurança

- **Vulnerabilidade** é uma fraqueza em código, configuração ou processo.
- **Ameaça** é uma circunstância ou agente capaz de causar dano ao explorar uma fraqueza.
- **Risco** combina as consequências possíveis e a probabilidade nas condições observadas.
- **Confidencialidade** limita o acesso aos dados a pessoas e sistemas autorizados.
- **Integridade** protege dados e processos contra alterações indevidas.
- **Disponibilidade** mantém os serviços acessíveis quando necessário.

## Controles defensivos

Use consultas parametrizadas para separar instruções SQL dos valores fornecidos pelo usuário. Conceda apenas as permissões necessárias. Mantenha segredos fora do código e dos logs. Preserve as evidências de diagnóstico sem registrar dados sensíveis. Valide cada correção em ambiente local ou de homologação com dados de teste.
