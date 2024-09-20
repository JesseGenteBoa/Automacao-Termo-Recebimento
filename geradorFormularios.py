import os
import re
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib import colors
from io import BytesIO


def gerarFormularios(caminho_arq, data):
    arquivos = []
    nomes_arquivos = []

    df = pd.read_excel(caminho_arq, sheet_name='Planilha1', dtype={3:str})

    lista_de_nomes = df.iloc[:, 0].tolist()

    lista_de_cpf = df.iloc[:, 1].tolist()

    def formatar_cpf(cpf):
        cpf = cpf.zfill(11)
        return re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)

    cpfs_formatados = [formatar_cpf(str(cpf)) for cpf in lista_de_cpf]

    lista_de_matricula = df.iloc[:, 3].tolist()


    string = """
    TERMO DE RECEBIMENTO E RESPONSABILIDADE

    EQS ENGENHARIA S/A portadora do CNPJ 80.464.753/0001-97 declara para os devidos fins administrativos, civis e criminais, que estamos disponibilizando o CARTÃO CORPORATIVO FLASH vinculado ao CPF 000.000.000-00 e que, a partir desta data 22/08/2024, é de sua responsabilidade pelo uso adequado e preservação do mesmo.
    O mal uso do cartão ou apropriação indébita do saldo disponibilizado, é passivo de desconto podendo até, acarretar em demissão por justa causa conforme política vigente da empresa e Termo e Condições gerais de uso do cartão, a seguir especificadas.


























    TERMO E CONDIÇÕES GERAIS DE USO

    1.	SOBRE O CARTÃO:

    1.1.	O cartão é vinculado aos dados do portador no momento da ativação, como nome completo, CPF, data de nascimento, nome da mãe e nome do pai;
    1.2.	O portador é responsável pelas informações cadastrais fornecidas sendo, portanto, responsável pelo envio atualizado de seus dados sempre que necessário. Para atualizá-los, o portador deverá entrar em contato com a EQS ENGENHARIA S/A;
    1.3.	O cartão é de uso exclusivo e intransferível do Portador;
    1.4.	A responsabilidade pela criação e sigilo da senha do cartão é exclusiva do Portador, ficando desde já a EQS ENGENHARIA S/A e a FLASH isentos de quaisquer obrigações decorrentes de sua má utilização ou divulgação a terceiros, devendo nesses casos ser observado o procedimento de comunicação ao banco, conforme item 5 (cinco);
    1.5.	A senha do cartão poderá ser alterada acessando o Aplicativo Móvel Flash para smartphones e tablet, ficando o Portador impossibilitado de fazê-lo diretamente nos caixas eletrônicos;
    1.6.	Ao receber o cartão, o Portador está ciente que utilizará o cartão para pagamento de despesas devidamente autorizadas pela empresa;
    1.7.	As cargas serão disponibilizadas nos dias 11 e 25 de cada mês e, caso seja um feriado ou final de semana, será feito no próximo dia útil subsequente.
    1.8.	Caso haja saldo no cartão ou valor pendente de prestação de contas de meses anteriores, será descontado do valor programado da carga;
    1.9.	Caso haja a necessidade de realizar transferências entre os cartões, a solicitação deve ser exclusivamente para o e-mail da GESTÃO DE CAIXA (caixa@eqsengenharia.com.br) onde é realizada duas vezes ao dia, ao término da manhã e ao final do dia;
    1.10.	De acordo com a modalidade de cartão empresarial, poderá haver um custo de mensalidade para o cartão, o qual não é de responsabilidade do portador e não interfere na prestação de contas do mesmo. Caso haja alguma dúvida, deve ser verificado com a empresa;




    2.	UTILIZAÇÃO DO CARTÃO CORPORATIVO:

    2.1.	A utilização do cartão é de uso exclusivo do portador e somente para despesas relacionadas a EQS ENGENHARIA S/A, sendo estritamente proibido o uso do Cartão Corporativo para despesas pessoais;
    2.2.	O saldo disponibilizado no cartão do portador é de inteira responsabilidade do mesmo e deve ser prestado contas junto a EQS ENGENHARIA S/A, conforme descrito no item 3 (três);
    2.3.	O mal uso do cartão ou apropriação indébita do saldo disponibilizado, é passivo de desconto do colaborador podendo até, acarretar em demissão por justa causa;
    2.4.	A Flash disponibiliza um aplicativo para consultas via smartphones ou tablets. Verifique as condições gerais do aplicativo disponibilizado na loja de aplicativos.
    2.5.	Caso o cartão possua a funcionalidade de saque, as transações são acrescidas do custo de saque, debitadas diretamente no cartão do portador e diminuindo do saldo disponível;
    2.6.	É de inteira responsabilidade do colaborador o manuseio e utilização do valor sacado e o mesmo também deve ser prestado contas conforme item 3 (três);
    2.7.	As compras corporativas serão autorizadas mediante a existência de saldo disponível no cartão;
    2.8.	Caso a senha do cartão for digitada incorretamente por 3 (três) vezes, o cartão será bloqueado automaticamente. O desbloqueio deve ser realizado no aplicativo Flash pelo portador do cartão.
    2.9.	Por ser um cartão pré-pago não é possível a realização de compras parceladas;


    3.	SOBRE A PRESTAÇÃO DE CONTAS: 

    3.1.	O portador terá acesso a plataforma Flash onde o mesmo deve inserir todas as suas despesas; 
    3.2.	A prestação de contas é obrigatória e de inteira responsabilidade do portador do cartão e a falta e/ou atraso na prestação de contas intervirá diretamente no próximo saldo a ser depositado para o portador;
    3.3.	O setor de GESTÃO DE CAIXA não faz lançamentos de documentos recebidos via malote ou e-mail;
    3.4.	A prestação de contas do mês vigente deve ser totalmente lançada, submetida e aprovada no sistema até o dia 30 onde o nome padrão dos relatórios deve começar por “CAIXA” e seguir com o mês e ano (MM/AAA). Exemplo: CAIXA 08/2024; 
    3.5.	Não é aceito despesas com datas de meses diversos sendo, portanto, de responsabilidade do portador prestar contas dentro do mês vigente da despesa, exceto em casos excepcionais como, por exemplo, férias, pericia, etc., tendo o limite máximo 2 meses;
    3.6.	É obrigatório em todos os lançamentos conter a data do documento, Centro de custo, categoria do lançamento, tipo de documento, número do comprovante e valor;
    3.7.	Quando o documento for do tipo DANFE, preencher o campo CHAVE DA DANFE com a numeração da chave com os 44 dígitos. Qualquer outro tipo de documento, deixar o campo CHAVE DA DANFE em branco;
    3.8.	As notas referentes as despesas devem ser legíveis, sem rasuras ou ocultação de dados;
    3.9.	Somente serão aceitas Notas Fiscais contendo: data, nome da empresa e discriminação de despesa. 
    3.10.	Não é permitida a inclusão de NF de pessoa física ou em nome e CNPJ de outra empresa, que não seja a EQS ENGENHARIA S/A;
    3.11.	Não serão aceitos Recibos, com exceção dos autorizados pelo Gestor do Contrato em acordo com a Direção, sendo obrigatório o envio do documento de identificação (RG, CNH, CARTÃO CNPJ) junto ao recebido assinado pelo prestador de serviço.
    3.12.	A compra de material ou prestações de serviços acima de $500,00 deve ser realizada pelo setor de compras;
    3.13.	Hospedagens devem ser realizadas pelo parceiro KENNEDY. Em caso de dúvida, entrar em contato com o setor ADMINISTRATIVO da EQS ENGENHARIA S/A; 
    3.14.	Não é permitido o uso do cartão para aquisição de bebidas alcoólicas, cigarros, recargas de telefones e combustível;
    3.15.	Não é permitido o uso do cartão para alimentação/café/almoço/janta pois o processo deve ser feito entre gestor e departamento pessoal/benefícios;
    3.16.	A falta de prestação de contas e/ou desacordo com políticas descritas acima, ensejará de ações administrativas e o possível desconto do colaborador; 




    4.	CONSULTA DE SALDOS E EXTRATOS DO CARTÃO

    4.1.	Para obter informações sobre saldo e extrato do cartão, basta acessar Aplicativo Móvel Flash que está no verso do cartão ou através do site. Se preferir, também é possível ligar para a Central de Relacionamento nos telefones informados no verso do cartão.


    5.	PERDA, EXTRAVIO, ROUBO OU FURTO DO CARTÃO:

    5.1.	 Em caso de perda, extravio, roubo ou furto, o Portador deverá comunicar imediatamente a Central de Relacionamento, para que o cartão seja bloqueado. Até que o bloqueio seja solicitado e feito, todas as operações efetuadas são de responsabilidade do portador do cartão;
    5.2.	É de extrema importância que a senha seja mantida separada do cartão, para evitar o uso indevido;
    5.3.	O prazo de entrega para reposição do cartão dependerá do local da entrega;
    5.4.	Caso o cartão relatado pelo Portador como perdido, extraviado, roubado ou furtado for encontrado, não poderá ser utilizado, a menos que a Central de Relacionamento confirme a possibilidade de reativação;


    6.	MEDIDAS DE SEGURANÇA:

    6.1.	Lembre-se sempre de manter a senha do cartão separada do mesmo, para evitar o seu uso indevido;
    6.2.	É de responsabilidade do portador do cartão:
    6.2.1.	Guardar o cartão num local seguro, nunca permitindo o uso por terceiros;
    6.2.2.	Memorizar a senha e mantê-la em sigilo, não a informando a terceiros;
    6.2.3.	Nunca anotar ou guardar a senha com o cartão.
    6.3.	Como medida de segurança, a EQS ENGENHARIA S/A poderá bloquear o cartão sem aviso prévio, caso verifique operações fora do perfil de uso do portador ou não haja a devida prestação de contas;
    6.4.	O portador do cartão autoriza a EQS ENGENHARIA S/A e a FLASH a contatá-lo por qualquer meio, inclusive telefônico, e-mail e SMS, afim de enviar comunicações a respeito do cartão;
    6.5.	O portador do cartão declara que todas as informações fornecidas no momento da solicitação do cartão, assim como o desbloqueio/bloqueio são verídicas;
    6.6.	A fim de validar as informações do Comprador/Portador do cartão descrito neste documento, este autoriza a Flash consultar seus dados cadastrais nos órgãos de informação ao crédito.
    6.7.	Por estar de pleno acordo com o aqui descrito, assino o presente termo.



    ALAN RODRIGO SILVA ANDRADE
    CPF 000.000.000-00 – MATRICULA: 555555
    """

    mes_ano = data[3:]

    for indice, cpf in enumerate(cpfs_formatados):
        texto_editado = string.replace("000.000.000-00", str(cpf))
        texto_editado = texto_editado.replace("22/08/2024", data)
        texto_editado = texto_editado.replace("08/2024", mes_ano)
        nome = lista_de_nomes[indice].upper()
        nome = nome.strip()
        texto_editado = texto_editado.replace("ALAN RODRIGO SILVA ANDRADE", nome)
        texto_editado = texto_editado.replace("555555", str(lista_de_matricula[indice]))
        arquivos.append([texto_editado])
        
    caminho = "PDFs"
    os.mkdir(caminho)

    for nome in lista_de_nomes:
        nome = nome.upper()
        nome = nome.strip()
        nomes_arquivo = caminho + "\TERMO DE RECEBIMENTO - CARTÃO FLASH - " + nome + ".pdf"
        nomes_arquivos.append(nomes_arquivo)


    def criar_pdf_com_fundo(texto, nome_arquivo, imagem_fundo):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        largura, altura = A4
        
        styles = getSampleStyleSheet()
        style = ParagraphStyle(
            'CenterStyle',
            parent=styles['Normal'],
            alignment=1,
            fontName='Helvetica',
            fontSize=12,
            textColor=colors.black,
            leading=18
        )
        
        formatted_text = texto.replace('\n', '<br/>')
        paragraph = Paragraph(formatted_text, style)
        
        def on_page(canvas, doc):
            canvas.drawImage(imagem_fundo, 0, 0, width=largura, height=altura)

        def build_pdf():
            doc.build([paragraph], onFirstPage=on_page, onLaterPages=on_page)

        build_pdf()

        with open(nome_arquivo, 'wb') as f:
            f.write(buffer.getvalue())


    for i, arquivo in enumerate(arquivos):
        for texto in arquivo:
            criar_pdf_com_fundo(texto, nomes_arquivos[i], r'_internal\Imagens\background_no_alpha.png')

