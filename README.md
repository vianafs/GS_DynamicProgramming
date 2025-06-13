  <h1>🌍 Global Solution - Dynamic Programming 🐍</h1>
  <h2>Simulador de Resposta a Queimadas</h2>
  <p><strong>Projeto desenvolvido com foco em soluções tecnológicas para combate a queimadas no Brasil e no mundo.</strong></p>

  <h2>👥 Integrantes</h2>
  <ul>
    <li><strong>Rafael Menezes Viana</strong> - RM: 558287</li>
    <li><strong>Kairo da Silva Silvestre de Carvalho</strong> - RM: 558288</li>
  </ul>

  <h2>📋 Requisitos</h2>
  <h3>📜 Requisitos Obrigatórios</h3>
  <ul>
    <li>Python 3.6 ou superior</li>
  </ul>

  <h3>📦 Bibliotecas Utilizadas</h3>
  <ul>
    <li><code>heapq</code> – Fila de prioridade (nativa)</li>
    <li><code>random</code> – Geração aleatória (nativa)</li>
    <li><code>time</code> – Controle de tempo e timestamps (nativa)</li>
  </ul>

  <h2>⚙️ Como Executar</h2>
  <pre><code>git clone https://github.com/vianafs/GS_DynamicProgramming.git
cd simulador
python simulador.py</code></pre>

  <h2>🧠 Explicação do Código</h2>

  <h3>1. Classe <code>Acao</code></h3>
  <p>Representa uma ação realizada (por exemplo, o atendimento de uma ocorrência). Cada objeto é um nó de uma lista ligada.</p>

  <h3>2. Classe <code>HistoricoAcoes</code></h3>
  <p>Gerencia a lista ligada de ações já executadas, permitindo adicionar e listar ações em ordem reversa de inserção (última primeiro).</p>

  <h3>3. Classe <code>SistemaQueimadas</code></h3>
  <p>É o sistema principal, responsável por gerenciar ocorrências e registrar ações:</p>
  <ul>
    <li><strong>iniciar()</strong>: Inicializa as estruturas de dados.</li>
    <li><strong>inserir_ocorrencia()</strong>: Insere uma nova ocorrência na fila de prioridade com base na severidade.</li>
    <li><strong>atender_proxima()</strong>: Remove a ocorrência mais urgente e registra no histórico.</li>
    <li><strong>listar_acoes()</strong>: Exibe todas as ações já realizadas.</li>
    <li><strong>gerar_relatorio()</strong>: Mostra o total de ocorrências atendidas por região.</li>
    <li><strong>simular_chamadas()</strong>: Gera chamadas simuladas com severidade crescente.</li>
  </ul>

  <h3>4. Execução Principal</h3>
  <p>Quando o arquivo <code>simulador.py</code> é executado:</p>
  <ol>
    <li>O sistema é iniciado.</li>
    <li>Ocorrências são simuladas automaticamente.</li>
    <li>Todas são atendidas em ordem de prioridade (maior severidade primeiro).</li>
    <li>Um histórico e um relatório final são exibidos.</li>
  </ol>

  <h2>📈 Benefícios e Aplicações</h2>
  <p>O projeto demonstra como algoritmos simples podem ser aplicados para responder de forma eficiente a situações de emergência. É uma base sólida para sistemas de gerenciamento de crises ambientais com lógica de prioridade.</p>
