**Classe Livraria de Planos**
Classe que gerencia os planos disponíveis para o agente.

    *Iniciar*:
        planos = dicionário vazio

    *Método Define Livraria de Planos(planos)*:
        Define os planos iniciais para a livraria de planos.

    *Método Adiciona Plano(meta, precondição, plano)*:
        Adiciona um plano à livraria de planos com metas, precondições e planos correspondentes.

    *Método Obter Plano(meta, base de crenças)*:
        Obtém um plano da livraria de planos com base nas metas e na base de crenças.

**Classe Ação**
Classe que representa uma ação que o agente pode executar no ambiente.

    *Método Ação()*:
        Imprime "###> ação no ambiente<###".

**Classe Agente**
Classe que representa o agente inteligente que toma decisões com base em suas crenças, desejos e intenções.

    *Iniciar*:
        crenças = dicionário vazio
        desejos = lista vazia
        intenções = lista vazia
        livraria de planos = nova instância de livraria de planos

    *Método Obter Desejos()*:
        Remove e retorna o último elemento da lista de desejos.

    *Método Adicionar Desejos(desejo)*:
        Adiciona um desejo à lista de desejos do agente.

    *Método Adicionar Crenças(crença)*:
        Atualiza o dicionário de crenças do agente com uma nova crença.

    *Método Definir Livraria de Planos(plano)*:
        Define a livraria de planos para o agente.

    *Método Atualiza Intenção(meta)*:
        Atualiza as intenções do agente com base nas metas e crenças atuais.
        Se um plano relevante é encontrado na livraria de planos, ele é adicionado à lista de intenções.

    *Método Execute Intenção()*:
        Executa as intenções do agente, tomando ações com base em seus planos e crenças.
        Enquanto houver intenções na lista, o agente executa a próxima ação ou atualiza suas intenções.
