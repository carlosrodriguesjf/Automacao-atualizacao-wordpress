# PROJETO AUTOMAÇÃO DA ATUALIZAÇÃO DO WORDPRESS

import pyautogui
import pyperclip
import webbrowser
import schedule
from time import sleep


def escreverCodigo(codigo):
    pyperclip.copy(codigo)
    pyautogui.hotkey('ctrl','v')
    

def atualizaSiga():

    webbrowser.open('https://siga.ufjf.br')

    # leitura dos arquivos com login e senha
    lista = []
    with open('login_siga.txt','r',newline='',encoding='utf-8') as arquivo:
        for linha in arquivo:
            lista.append(linha)

    # acesso ao siga
    sleep(2)
    pyautogui.click(381,467,duration=2)
    pyautogui.write(lista[0])
    sleep(1)
    pyautogui.click(560,565,duration=1)
    pyautogui.write(lista[1])
    pyautogui.click(643,673, duration=1)
    sleep(2)

    # clicar em sites
    pyautogui.click(1350,307, duration=2)
    sleep(2)

    # clicar em meus sites
    pyautogui.click(81,300, duration=2)
    sleep(2)

    # clicar no site central de atendimento JF
    pyautogui.click(90,357, duration=2)
    sleep(2)

    # mover para paginas
    pyautogui.moveTo(90,437, duration=1)
    sleep(2)

    # clicar em todas as paginas
    pyautogui.click(293,437, duration=1)
    sleep(2)

    # clicar duas vezes na página de rolagem
    pyautogui.doubleClick(1906,950, duration=2)
    sleep(2)

    # clicar em Formularios
    pyautogui.click(325,635, duration=2)
    sleep(2)

    # clicar na area de codigo
    pyautogui.click(308,790, duration=1)
    sleep(2)

    # apertar control + A
    pyautogui.hotkey('ctrl','a')
    sleep(0.5)

    # apertar delete
    pyautogui.hotkey('del')
    sleep(0.5)

    # clicar na area de codigo
    pyautogui.click(308,790, duration=1)
    sleep(1)

    # ler arquivo com atualização
    codigo ="""Nessa página serão listados os formulários eletrônicos e em PDF para quando é necessário assinatura do requerente. Consulte nossa página <a href="https://www2.ufjf.br/cat/servicos/">Serviços</a> para conhecer os atendimentos realizados.

    Para o preenchimento, deverá inicialmente ser realizado o login com uma conta Google, preferencialmente usando o e-mail institucional do respondente, sendo permitidos os domínios @ufjf.br, @estudante.ufjf.br e @visitante.ufjf.br.
    <ul style="margin-left: 0">
        <li><a href="https://www2.ufjf.br/cat/formularios/requerimento-aproveitamento-de-estudos/aproveitamento-de-estudos/" target="_blank" rel="noopener">Aproveitamento de Estudos</a></li>
        <li><a href="https://forms.gle/pbRXL9PNyK9K7jMT6">Atestado, Declaração ou Certidão</a></li>
        <li><a href="https://forms.gle/gtddvJwC9f9NKoiH6" target="_blank" rel="noopener">Correção ou Alteração de Dados Cadastrais</a></li>
        <li><a href="https://forms.gle/c8Nq46M78ufDoK5H8" target="_blank" rel="noopener">Data Especial de Colação de Grau (Antecipação de Colação)</a></li>
        <li><a href="https://forms.gle/9MmJRV3WmAKRmHSV6" target="_blank" rel="noopener">Diploma de Graduação – Segunda Via</a></li>
        <li><a href="https://forms.gle/hHsKg1b8K9ULEb5fA" target="_blank" rel="noopener">Diploma/Certificado de Pós-graduação – Segunda Via</a></li>
        <li><a href="https://forms.gle/93GHeu18jvQEBXeo6" target="_blank" rel="noopener">Histórico Escolar</a></li>
            <li><a href="https://forms.gle/F5yqh6LEcH5j8aCYA"><span class="material-icons">read_more</span> Ingresso de Refugiados Políticos</a></li>
        <li><a href="https://www2.ufjf.br/cat/ceua/" target="_blank" rel="noopener">Submissão de Protocolo CEUA</a></li>
        <li><a href="https://forms.gle/a8K8h6LSnNdpK1Ez6" target="_blank" rel="noopener">Transferência de Aceitação Obrigatória (ex-officio)</a></li>
    </ul>
    &nbsp;

    <span class="material-icons">info </span>Os seguintes documentos estão disponibilizados com <a href="https://www2.ufjf.br/cat/servicos/graduacao/documentos/autenticacao-eletronica/"><span class="material-icons">open_in_new</span> autenticação eletrônica</a>:  Atestado de Vínculo (sem prazos); Atestado de Previsão de Colação de Grau (para discente inscrito na Colação de Grau), Plano de Ensino de Disciplinas (Ementas), Atestado de vínculo com IRA, Atestado de reconhecimento de curso e históricos escolares de disciplina isolada da graduação, convênio exterior e convênio outras IFES.

    &nbsp;
    <h2>Formulários em PDF</h2>
    Confira as orientações de cada pedido na página <a href="https://www2.ufjf.br/cat/servicos/" target="_blank" rel="noopener">Serviços</a>
    <ul style="margin-left: -3rem">
        <li><a href="https://www2.ufjf.br/cat/formularios/requerimento-aproveitamento-de-estudos/aproveitamento-de-estudos/" target="_blank" rel="noopener">Aproveitamento de Estudos</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2023/05/Atestado-Declaração-ou-Certidão-v260423.pdf" target="_blank" rel="noopener">Atestado, Declaração ou Certidão</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/03/2-Cadastro-de-E-mail-no-Siga_v070322-2.pdf">Cadastro de E-mail no Siga</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2023/04/Cancelamento-de-Matrícula-em-Curso-de-Graduação-v260423.pdf">Cancelamento de Matrícula em Curso de Graduação</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/06/Correcao-Alteracao-Dados-Cadastrais-v200522.pdf" target="_blank" rel="noopener">Correção ou Alteração de Dados Cadastrais</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2023/03/Data-Especial-de-Colação-de-Grau_v020323.pdf" target="_blank" rel="noopener">Data Especial de Colação de Grau (Antecipação de Colação)</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2018/12/13.2-Dilatação-ou-Prorrogação-de-Prazo.pdf" target="_blank" rel="noopener">Dilatação de curso</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/11/Segunda-Via-de-Diploma-de-Graduação-v091122.pdf" target="_blank" rel="noopener">Diploma de Graduação – Segunda Via</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/11/Segunda-Via-de-Diploma-de-Pos-Graduação-v091122.pdf" target="_blank" rel="noopener">Diploma/Certificado de Pós-graduação – Segunda Via</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2021/12/Historico-Escolar-v190722.pdf" target="_blank" rel="noopener">Histórico Escolar</a></li>
            <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2023/05/Inscricao-Ingresso-Refugiados-Politicos-v280423.pdf"><span class="material-icons">read_more</span> Ingresso de Refugiados Políticos</a></li>
            <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2023/01/Reintegração-ao-Curso-v260123.pdf">Reintegração ao Curso</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/03/Formulário-Nome-Social_v080322.pdf" target="_blank" rel="noopener">Requerimento de Uso de Nome Social</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2023/03/Requerimento-Para-envio-de-Documento-pelo-Correios_v260123.pdf">Requerimento Para envio de Documento pelo Correios</a>
    <a href="https://www2.ufjf.br/cat/servicos/geral/envio-de-documentos-pelos-correios/"><span class="material-icons">read_more</span> Mais detalhes sobre envio de documentos</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/03/3-Restituição-de-Taxa-E-mail_v210322.pdf">Restituição de Taxa</a></li>
        <li><a href="https://www2.ufjf.br/cat/formularios/termo-de-concordancia-e-veracidade-para-liberacao-de-usuario-externo-sei-ufjf/">Termo de Concordância e Veracidade para Liberação de Usuario Externo SEI UFJF</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/11/Trancamento-Excepcional-de-Curso-não-saúde-v011122.pdf">Trancamento Excepcional de Curso (não saúde)</a></li>
        <li><a href="https://www2.ufjf.br/cat/wp-content/uploads/sites/19/2022/11/Transferencia-Obrigatoria-v011122.pdf" target="_blank" rel="noopener">Transferência de Aceitação Obrigatória (ex-officio)</a></li>
    </ul>"""

    escreverCodigo(codigo)

    # clicar duas vezes na página de rolagem para subir
    pyautogui.doubleClick(1906,174, duration=2)
    sleep(1)

     # clicar em atualizar
    pyautogui.click(1811,759, duration=2)
    sleep(3)

    # mover até "olá Carlos"
    pyautogui.moveTo(1648,149, duration=1)
    sleep(1)
    
    # clicar botão sair
    pyautogui.click(1649,299, duration=2)
 

# agendamento da automação
schedule.every().tuesday.at('00:00').do(atualizaSiga)

while True:
    schedule.run_pending()
    sleep(1)