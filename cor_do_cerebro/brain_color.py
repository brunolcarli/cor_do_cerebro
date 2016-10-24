# -*- Encoding:utf-8 -*-

from tkinter import *
from user import User
import sqlite3

# Define as paginas da janela
pagina = 0
# Cria uma instancia de usuario
nuser = User()


def pergunta(frm,qa,qb,qc,qd,val,pa,pb,pc,pd):
    '''Define a pergunta do teste'''
    Label(frm, text='Pergunta #%i' % (pagina - 1), bg='#D6FFC8').grid(sticky=N)
    Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)
    Label(frm, text='%s' % (nuser.nome), bg='#D6FFC8').grid(sticky=N)

    Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)

    titulo = Label(frm, text='Preencha os valores de 1 a 4 sem repetir '
                             'os números para cada comportamento', bg='#D6FFC8')
    titulo.grid(sticky=N)
    titulo2 = Label(frm, text='4 para os que mais representam sua personalidade e ', bg='#D6FFC8')
    titulo2.grid(sticky=N)
    titulo3 = Label(frm, text='1 para os que menos representam sua personalidade', bg='#D6FFC8')
    titulo3.grid(sticky=N)

    Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)

    # As perguntas 10, 11 e 12 possuem enunciados diferentes
    # então essa estrutura abaixo de decisão define qual
    # enunciado deve aparecer em qual pergunta

    # Enunciado da pergunta 10
    if pagina == 11:
        Label(frm, text='Quando tomo decisões eu gosto de:', bg='white').grid(sticky=N)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)
    # Enunciado da pergunta 11
    elif pagina == 12:
        Label(frm, text='Quando eu trabalho em equipe, me vejo como:', bg='white').grid(sticky=N)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)
    # Enunciado da pergunta 12
    elif pagina == 13:
        Label(frm, text='Me sinto mais à vontade e me destaco em ambientes que apoiam meu senso de:', bg='white').grid(sticky=N)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)

    Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)

    a = Label(frm, text=pa, bg='#D6FFC8')
    a.grid(sticky=N + W, row=10)
    a1 = OptionMenu(frm, qa, val[0], val[1], val[2], val[3])
    a1.config(bg='#D6FFC8')
    a1['menu'].config(bg='#C6FFE2')
    a1.grid(sticky=N + W, row=11)

    b = Label(frm, text=pb, bg='#D6FFC8')
    b.grid(sticky=N, row=12)
    b1 = OptionMenu(frm, qb, val[0], val[1], val[2], val[3])
    b1.config(bg='#D6FFC8')
    b1['menu'].config(bg='#C6FFE2')
    b1.grid(sticky=N, row=13)

    c = Label(frm, text=pc, bg='#D6FFC8')
    c.grid(sticky=N, row=10)
    c1 = OptionMenu(frm, qc, val[0], val[1], val[2], val[3])
    c1.config(bg='#D6FFC8')
    c1['menu'].config(bg='#C6FFE2')
    c1.grid(sticky=N, row=11)

    d = Label(frm, text=pd, bg='#D6FFC8')
    d.grid(sticky=N + E, row=10)
    d1 = OptionMenu(frm, qd, val[0], val[1], val[2], val[3])
    d1.config(bg='#D6FFC8')
    d1['menu'].config(bg='#C6FFE2')
    d1.grid(sticky=N + E, row=11)

    Label(frm, text='*' * 90, bg='#D6FFC8').grid(sticky=S)
    Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)

    # botoes
    home = Button(frm, text='Tela Inicial',bg='orange', command=inicio)
    home.grid(sticky=S + W, row=20)

    Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)
    Label(frm, text='*' * 90, bg='#D6FFC8').grid(sticky=S)

def get_names_from_db():
    # Cria uma conexão com o banco de dados
    connection = sqlite3.connect('brain_color_db.sqlite')
    # Cria um cursor para manipular o banco de dados
    cursor = connection.cursor()
    # Seleciona os dados do banco de dados
    id = cursor.execute("SELECT id FROM usuarios")
    dic = {}
    for i in id.fetchall():
        results = cursor.execute('''SELECT name, cor FROM usuarios WHERE id=?''', i)
        (name, cor) = results.fetchone()
        dic[name] = cor

    connection.close()
    return(dic)

def view_db():
    '''Abre a pagina para visualizar os registros'''
    global pagina
    pagina = 50
    refresh()

def refresh():
    '''Atualiza o frame'''
    global frame
    global pagina
    frame.destroy()
    frame = Frame(app, bg='#D6FFC8')
    frame.pack()
    gen_page(frame, pagina)

def inicio():
    '''Voltar para a tela de inicio e reinicia os valores'''
    global pagina
    pagina = 0
    global nuser
    nuser.reset_value()
    refresh()


def begin():
    '''Começar o teste'''
    global pagina
    pagina = 1
    refresh()


def verify(qa, qb, qc, qd):
    ''' Verifica se as entradas são todas diferentes'''
    # guarda as informações
    a = qa.get()
    b = qb.get()
    c = qc.get()
    d = qd.get()
    # se forem diferentes
    if a != b and a != c and a != d and b != a and b != c and b != d and c != a and c != b and c != d:
        global pagina
        pagina += 1
        nuser.add_value(a,b,c,d) # adicionamos esses valores aos atributos da instancia user
        refresh()
    # se algum valor for repetido aparece uma msg de erro
    else:
        refresh()
        l = Label(frame, text='Por favor selecione valores diferentes para cada opção', bg='RED')
        l.grid(sticky=S)




def gen_page(frm, pagina):
    '''Gera as paginas da janela'''
    # option menus
    qa = IntVar(frm)
    qb = IntVar(frm)
    qc = IntVar(frm)
    qd = IntVar(frm)
    # valor das opções
    val = [1, 2, 3, 4]
    qa.set(val[0])
    qb.set(val[1])
    qc.set(val[3])
    qd.set(val[2])

    def about():
        global pagina
        pagina = 51
        refresh()

    def new_user():
        '''Esta função define o novo usuario'''
        global nuser # Chama a variavel que guarda a instancia de usuario
        e = entry.get().title() # Guarda a entrada do usuario na variavel 'e'
        if len(e) < 3 and len(e) > 0: # A entrada deve ter mais de 3 caracteres
            Label(frm, text="Nome muito curto", bg='YELLOW').grid(sticky=N)
        elif len(e) < 1: # e não pode ser vazia
            Label(frm, text="Insira um nome", bg='RED').grid(sticky=N)
        else:
            nuser.muda_nome(e) # Atribui um nome de usuario
            global pagina # chama a variavel que  muda a pagina


            pagina = 2    # define a prózima página
            refresh()     # Atualiza a página

    def check():
        '''chama a função de verificação'''
        verify(qa, qb, qc, qd)


    # Pagina inicial
    if pagina == 0:
        # Define a pagina inicial
        imagem = PhotoImage(file="images/gbrain2.gif")
        w = Label(frm, image=imagem)
        w.imagem = imagem
        w.grid(column=1, row=2)
        Label(frm, text='Qual a cor do seu cérebro?').grid(column=1, row=0, rowspan=5)

        # Botão para começar o teste
        btn = Button(frame, text='* Começar o teste  * ', bg="#1E93EE", command=begin)
        btn.grid(column=1, row=8)

        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(column=1, row=9)

        # Botão para ver os cérebros registrados
        viewdb = Button(frame, text='Cérebros registrados', bg='#00D571', command=view_db)
        viewdb.grid(column=1, row=10)

        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(column=1, row=11)

        # Botao para ver a pagina de informações
        infob = Button(frame, text='Sobre este aplicativo', bg='#00FFE5', command=about)
        infob.grid(column=1, row=12)


    # Recebe Nome
    elif pagina == 1:
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)

        titulo = Label(frm, text='Insira seu nome no campo abaixo', bg='#D6FFC8')
        titulo.grid(sticky=N)

        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)
        Label(frm, text='*' * 90, bg='#D6FFC8').grid(sticky=S)

        # Caixa de entrada para o nome
        entry = Entry(frm)
        entry.grid(sticky=N)


        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)

        # Botão
        get = Button(frm, text="Confirma",bg='#1E93EE', command=new_user)
        get.grid(sticky=N)

        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)
        Label(frm, text='*' * 90, bg='#D6FFC8').grid(sticky=S)

    # Pergunta 1
    elif pagina == 2:
        pergunta(frm,qa,qb,qc,qd,val, 'Organizado', 'Criativo', 'Independente', 'Impulsivo')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 2
    elif pagina == 3:
        pergunta(frm,qa,qb,qc,qd,val, 'Pontual', 'Comunicativo', 'Curioso', 'Divertido')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 3
    elif pagina == 4:
        pergunta(frm, qa, qb, qc, qd, val, 'Detalhista', 'Flexivel', 'Calmo', 'Competitivo')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 4
    elif pagina == 5:
        pergunta(frm, qa, qb, qc, qd, val, 'Responsável', 'Atencioso', 'Analístico', 'Engenhoso')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 5
    elif pagina == 6:
        pergunta(frm, qa, qb, qc, qd, val, 'Comprometido', 'Sensível', 'Pensativo', 'Corajoso')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 6
    elif pagina == 7:
        pergunta(frm, qa, qb, qc, qd, val, 'Cuidadoso', 'Coperativo', 'Técnico', 'Ativo')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 7
    elif pagina == 8:
        pergunta(frm, qa, qb, qc, qd, val, 'Disciplinado', 'Carinhoso', 'Independente', 'Ousado')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 8
    elif pagina == 9:
        pergunta(frm, qa, qb, qc, qd, val, 'Respeitoso', 'Autêntico', 'Competente', 'Generoso')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 9
    elif pagina == 10:
        pergunta(frm, qa, qb, qc, qd, val, 'Previsível', 'Protetor', 'Questionador', 'Espontâneo')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 10
    elif pagina == 11:
        pergunta(frm, qa, qb, qc, qd, val, 'Ter um plano', 'Conversar com outras pessoas',
                 'Colher fatos e informações', 'Confiar nos instintos')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 11
    elif pagina == 12:
        pergunta(frm, qa, qb, qc, qd, val, 'Instrutor', 'Membro da equipe',
                 'Solucionador de problemas', 'Negociador de impasses')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    # Pergunta 12
    elif pagina == 13:
        pergunta(frm, qa, qb, qc, qd, val, 'Estabilidade', 'harmonia',
                 'Privacidade', 'Liberdade')
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)
    # Resultado
    elif pagina == 14:
        # Exibe o resultado para o usuario
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='RESULTADO', bg='#D6FFC8').grid(sticky=N)
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='%s' % (nuser.nome), bg='#D6FFC8').grid(sticky=N)
        titulo = Label(frm, text='A cor do seu cérebro é: ', bg='#D6FFC8')
        titulo.grid(sticky=N)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)

        nuser.get_user_brain() # Verifica qual cerebro caracteriza a personalidade do usuario

        # Se resultar amarelo
        if nuser.brain_color == 'Amarelo':
            imagem = PhotoImage(file="images/ybrain.gif")
            w = Label(frm, image=imagem)
            w.imagem = imagem
            w.grid(sticky=N+S)
            x = '#D1DC02'
        # Se resultar azul
        elif nuser.brain_color == 'Azul':
            imagem = PhotoImage(file="images/bbrain.gif")
            w = Label(frm, image=imagem)
            w.imagem = imagem
            w.grid(sticky=N+S)
            x = '#364CE6'
        # se resultar verde
        elif nuser.brain_color == 'Verde':
            imagem = PhotoImage(file="images/ggbrain.gif")
            w = Label(frm, image=imagem)
            w.imagem = imagem
            w.grid(sticky=N+S)
            x = '#1A9500'
        # se resultar laranja
        elif nuser.brain_color == 'laranja':
            imagem = PhotoImage(file="images/obrain.gif")
            w = Label(frm, image=imagem)
            w.imagem = imagem
            w.grid(sticky=N+S)
            x = '#FF9700'

        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text=nuser.brain_color, bg='#D6FFC8', fg=x).grid(sticky=S)
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)

        # insere o resultado no banco de dados

        # Cria uma conexão com o banco de dados
        connection = sqlite3.connect('brain_color_db.sqlite')
        # Cria um cursor para manipular o banco de dados
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuarios(name, cor) VALUES (?,?)", (nuser.nome, nuser.brain_color))
        connection.commit() # envia ao banco de dados
        connection.close()

        #botão
        next = Button(frm, text='Proximo',bg='#1E93EE', command=check)
        next.grid(sticky=S + E, row=20)

    elif pagina == 15:
        # Essa pagina vai mostrar as caracteristicas da cor resultante

        # AMARELO
        if nuser.brain_color == 'Amarelo':
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)
            Label(frm, text='Caracteristicas da pessoa de cérebro amarelo', bg='#D6FFC8').grid(sticky=N)
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=N)
            Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=N)

            Label(frm, text='- Cuidadosa e responsável ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Tem uma atitude de líder e segue as regras ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Auxilia o professor e aprende melhor quando sente que está preparado ',
                  bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Com os amigos faz planos para estarem juntos', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Em casa, precisa de instruções e cuidados e fica frustrada com a desorganização',
                  bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Gosta de história e de ler biografias', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- É uma pessoa que quando esta triste fica nervosa e preocupada ', bg='#D6FFC8').grid(
                sticky=N + S)
            Label(frm, text='- Seu quarto é imaculado ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Não gosta que mecham em suas coisas ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Gosta que suas coisas sempre estejam em ordem ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Pessoa confiável, pontual e responsável ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Leal, respeitadora e organizada ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Preocupa-se com o futuro ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Reclama e sente autopiedade ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Crítico e sistemático ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='- Emprega tom diplomático e utiliza linguagem formal ', bg='#D6FFC8').grid(
                sticky=N + S)
            Label(frm, text='- Necessita que entemdam seu senso de comprometimento ', bg='#D6FFC8').grid(
                sticky=N + S)
            Label(frm, text='- Seu lema é "Siga as regras" ', bg='#D6FFC8').grid(sticky=N + S)
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

            home = Button(frm, text='Tela Inicial', bg='orange', command=inicio)
            home.grid(sticky=S)

        #AZUL
        elif nuser.brain_color == 'Azul':
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
            Label(frm, text='Caracteristicas da pessoa de cérebro azul', bg='#D6FFC8').grid(sticky=N)
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

            Label(frm, text='- Gosta de falar abertamente sobre seus sentimentos ', bg='#D6FFC8').grid(sticky=S+N)
            Label(frm, text='- Artista, coopera e ajuda os colegas ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É bom ouvinte ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Aprende melhor com exemplos visuais ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Prefere trabalhar em equipe', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Precisa de demonstrações de amor, abraços e beijos ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Gosta de hostórias de animais e fantasias ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Fica frustrado com o egoísmo dos outros e quando está infeliz chora ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Não abandona os companheiros ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Prestativo, criativo e comunicativo ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Pessoa que gosta de ajudar e se dispor ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Valorizam a confiaça, empatia e cooperação ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Utiliza abordagem amistosa ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Precisam se sentir estimados e que entendam sua sensibilidade ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Chora e fica histérico, fica deprimido e com remorso ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Diz que está bem mas não está. Não encara a realidade ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Em conflito, age de forma irracional ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Seu lema é "Nós podemos ajudar" ', bg='#D6FFC8').grid(sticky=S + N)

            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

            home = Button(frm, text='Tela Inicial', bg='orange', command=inicio)
            home.grid(sticky=S)

        # VERDE
        elif nuser.brain_color == 'Verde':
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
            Label(frm, text='Caracteristicas da pessoa de cérebro verde', bg='#D6FFC8').grid(sticky=N)
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

            Label(frm, text='- Gosta de resolver quebra-cabeças e jogos de computador e video game ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Tem atitude individualista ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É curioso e prefere trabalhar sozinho ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Aprende melhor com computadores e livros ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É solitário e não segue a multidão, nem os amigos, nem a moda ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Precisa de tempo para descobrir as coisas, as coisas precisam fazer sentido para ela ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Gosta de privacidade e não mostra suas emoções ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Aprecia mistérios e ficção científica ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Fica frustrado com rotinas e quando está triste não gosta de falar ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Precisa que valorize sua inteligência e entendam seu senso de concisão', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É uma pessoa lógica, inteligente e comedido ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Valorizam a sabedoria, competência e independência ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- São pessoas reservadas ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Emprega tom informativo e utiliza abordagem acadêmica ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É crítico e sarcástico. Trata as pessoas com indiferença ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É indiferente e insensível. Não é cooperativo ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Demonstra seu descontentamento quando algo não lhe agrada ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Seu lema é "Pense cuidadosamente sobre o assunto" ', bg='#D6FFC8').grid(sticky=S + N)

            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

            # Botão
            home = Button(frm, text='Tela Inicial', bg='orange', command=inicio)
            home.grid(sticky=S)

        # lARANJA
        elif nuser.brain_color == 'laranja':
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
            Label(frm, text='Caracteristicas da pessoa de cérebro laranja', bg='#D6FFC8').grid(sticky=N)
            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)


            Label(frm, text='- E atleta e gosta de ter uma boa performance ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Tem atitude alegre. Aprende melhor com atividades manuais e variadas ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Gosta mais de fazer do que de ouvir. ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Em casa, gosta de fazer as próprias coisas ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Pessoa energética ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Fica frustrado com regras e quando está infeliz porta-se mal ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Nao se incomoda em ambientes desorganizados ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É uma pessoa dinâmica, generosa e espontânea ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Energética e corajosa ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Valorizam o empreendedorismo, desenvoltura e generosidade ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Precisa de incentivo ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Utiliza abordagem descontraída ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Precisa que aceitem sua informalidade e seu estilo "não tradicional"', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- É imaturo, desbediente, rude e agressivo. Apresenta comportamento compulsivo ', bg='#D6FFC8').grid(sticky=S + N)
            Label(frm, text='- Seu lema é "Vamos nessa" ', bg='#D6FFC8').grid(sticky=S + N)

            Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

            # Botão
            home = Button(frm, text='Tela Inicial', bg='orange', command=inicio)
            home.grid(sticky=S)

    # Pagina da tabela de cerebros
    elif pagina == 50:

        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='RESULTADOS ANTERIORES', bg='#D6FFC8').grid(sticky=N)
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)
        f = Frame(frm, width=300, height=100)
        f.grid(sticky=N)
        # Criar um canvas para exibir os resultados
        canvas = Canvas(f, bg='#FFFFFF', width=300, height=100, scrollregion=(0, 0, 500, 500))
        vbar = Scrollbar(f, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=300, height=100)
        canvas.config(yscrollcommand=vbar.set)
        canvas.config(scrollregion=canvas.bbox(ALL))
        canvas.pack(side=LEFT, expand=False, fill=BOTH)

        results = get_names_from_db()


        for key, value in results.items():
            Label(canvas,bg='#7CFFBD', text='# Nome:  %s   Cor:  %s ' %(key,value)).pack()


        #hbar = Scrollbar(f, orient=HORIZONTAL)
        #hbar.pack(side=BOTTOM, fill=X)
        #hbar.config(command=canvas.xview)


        # Botão
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        home = Button(frm, text='Tela Inicial', bg='orange', command=inicio)
        home.grid(sticky=S)

    elif pagina == 51:
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='*  Sobre este aplicativo  *', bg='#D6FFC8').grid(sticky=N)
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)

        Label(frm, text='Este aplicativo foi baseado na teoria de Sheila Glazov sobre as cores'
                        ' do cérebro.', bg='#D6FFC8').grid(stick=S)
        Label(frm, text='Através da metáfora das cores podemos traçar perfis psicológicos',bg='#D6FFC8').grid(stick=S)
        Label(frm, text='e compreender melhor o comportamento humano. ', bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='Este teste tem por objetivo melhorar as relações '
                        'humanas dado que possamos ', bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='compreender as diferentes caracteristicas psicológicas das pessoas. ', bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='Você pode ler mais a respeito no livro da autora: ', bg='#D6FFC8').grid(sticky=S)

        imagem = PhotoImage(file="images/livro.gif")
        w = Label(frm, image=imagem)
        w.imagem = imagem
        w.grid(sticky=N + S)

        Label(frm, text='E através do site: ', bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='http://www.sheilaglazov.com/booksdvd/a-cor-do-seu-cerebro/', bg='#D6FFC8').grid(sticky=S)

        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)
        Label(frm, text='- Bruno L. Carli ', bg='#D6FFC8').grid(sticky=S+E)
        Label(frm, text=' ' * 90, bg='#D6FFC8').grid(sticky=S)

        # Botão
        Label(frm, text='-' * 90, bg='#D6FFC8').grid(sticky=S)
        home = Button(frm, text='Tela Inicial', bg='orange', command=inicio)
        home.grid(sticky=S)


app = Tk()
app.configure(background='#D6FFC8')
app.title("Brain Color")
app.geometry("500x550")
frame = Frame(app, bg='#D6FFC8')
frame.pack()
gen_page(frame, pagina)



app.mainloop()



