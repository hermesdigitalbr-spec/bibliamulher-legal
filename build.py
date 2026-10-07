#!/usr/bin/env python3
"""Gera as páginas estáticas (CSS embutido, como nos demais repos -legal). Uso: python3 build.py"""
import pathlib
ROOT = pathlib.Path(__file__).parent
BRAND = "Bíblia da Mulher"
PLUS = "Bíblia da Mulher Plus"
MAIL = '<a href="mailto:support@hermes.com.br">support@hermes.com.br</a>'
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
UPDATED = "Última atualização: 7 de outubro de 2026"
TAG = "Devocional para mulheres · Hermes Digital"
CSS = """
:root{
  --ground:#F6F1EA; --surface:#FFFFFF; --sunken:#FBF3EE;
  --ink:#3A2E29; --brand:#B8543A; --accent:#B8543A;
  --text2:#5E4F47; --faint:#7A675C; --hairline:rgba(46,42,36,.12);
  --serif:ui-serif,"New York","Iowan Old Style",Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:16.5px;line-height:1.62;padding:0 22px 90px;-webkit-font-smoothing:antialiased}
.wrap{max-width:40rem;margin:0 auto}
.lang{text-align:right;padding-top:18px;font-size:13px}
header{position:relative;padding:40px 0 26px;text-align:center}
header::before{content:"";position:absolute;left:50%;top:-10px;transform:translateX(-50%);
  width:190px;height:190px;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle at 40% 35%, rgba(242,217,204,.75), rgba(242,217,204,0) 62%),
    radial-gradient(circle at 62% 60%, rgba(184,84,58,.18), rgba(184,84,58,0) 62%);
  filter:blur(26px)}
.brand{position:relative;font-family:var(--serif);font-size:23px;letter-spacing:.01em;color:var(--brand)}
h1{position:relative;font-family:var(--serif);font-size:clamp(31px,8vw,40px);font-weight:500;
  line-height:1.12;letter-spacing:-.015em;margin:12px 0 8px;text-wrap:balance}
.updated{position:relative;font-size:13px;color:var(--faint);margin:0}
.rule{height:1px;background:var(--hairline);margin:6px 0 4px}
h2{font-family:var(--serif);font-size:20.5px;font-weight:500;letter-spacing:-.01em;margin:38px 0 8px;color:var(--ink)}
p,li{color:var(--text2);max-width:60ch;margin:0 0 .85rem}
ul{padding-left:1.15rem;margin:.2rem 0 1rem}
li{margin:.34rem 0}
li::marker{color:var(--accent)}
strong{color:var(--ink);font-weight:640}
a{color:var(--accent);text-underline-offset:2px;text-decoration-thickness:1px}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:3px}
.card{background:var(--surface);border:1px solid var(--hairline);border-radius:16px;padding:20px 22px;
  margin:26px 0 6px;box-shadow:0 1px 2px rgba(46,42,36,.03),0 10px 30px -18px rgba(46,42,36,.16)}
.card p{margin:0}
.card.quiet{background:var(--sunken);box-shadow:none}
.docs{list-style:none;padding:0;margin:8px 0 0}
.docs li{margin:0;border-top:1px solid var(--hairline);max-width:none}
.docs li:first-child{border-top:0}
.docs a{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:15px 2px;
  text-decoration:none;font-family:var(--serif);font-size:17.5px;color:var(--ink)}
.docs a span{font-family:var(--sans);font-size:13px;color:var(--faint)}
.docs a:hover{color:var(--accent)}
footer{margin-top:52px;padding-top:20px;border-top:1px solid var(--hairline);font-size:13px;color:var(--faint);text-align:center}
footer a{color:var(--faint)}
@media (prefers-color-scheme:dark){
 :root{--ground:#1A1713; --surface:#231F19; --sunken:#2A251E; --ink:#F1E8D6; --brand:#F2D9CC;
   --accent:#F0A07E; --text2:#CFC4B2; --faint:#A89A85; --hairline:rgba(241,232,214,.14)}
 .card{box-shadow:none}
}
"""


def page(slug, title, sub, body):
    # links relativos e sem extensão; o app abre /terms.html e /privacy.html, que são estes mesmos arquivos
    foot = "" if slug == "index" else ' · <a href="./">Documentos legais</a>'
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<style>{CSS}</style>
<title>{BRAND} — {title}</title>
</head>
<body>
<div class="wrap">
<header>
<div class="brand">{BRAND}</div>
<h1>{title}</h1>
<p class="updated">{sub}</p>
</header>
<div class="rule"></div>
{body.strip()}

<footer>Hermes Digital · {BRAND}{foot}</footer>
</div>
</body>
</html>
"""
    (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")


page("index", "Documentos legais", TAG, f"""
<div class="card">
<ul class="docs">
<li><a href="terms">Termos de Uso<span>ler →</span></a></li>
<li><a href="privacy">Política de Privacidade<span>ler →</span></a></li>
<li><a href="support">Suporte<span>abrir →</span></a></li>
</ul>
</div>

<h2>Suporte</h2>
<p>Dúvidas sobre o app, sua assinatura ou seus dados, escreva para {MAIL}.</p>

<div class="card quiet">
<p>O app {BRAND} funciona no seu iPhone ou iPad: sem conta, sem anúncios, e as suas anotações e orações ficam no aparelho.</p>
</div>
""")

page("privacy", "Política de Privacidade", UPDATED, f"""
<div class="card">
<p><strong>Em uma frase:</strong> o app {BRAND} funciona no seu aparelho. Suas leituras, anotações e orações ficam nele — nada é enviado para nós, não existe conta de usuário, não há anúncios e não usamos ferramentas de análise de terceiros.</p>
</div>

<h2>Quem somos</h2>
<p>{BRAND} é um app de leitura bíblica e devocional para iPhone e iPad desenvolvido pela Hermes Digital. Contato: {MAIL}</p>

<h2>Que dados o app trata e onde ficam</h2>
<p>Tudo o que o app guarda fica no armazenamento do seu próprio aparelho:</p>
<ul>
<li><strong>o nome</strong> pelo qual você pede para ser chamada, se informar;</li>
<li><strong>suas escolhas</strong> de objetivos, rotina, horários de lembrete, versão da Bíblia e aparência;</li>
<li><strong>seu conteúdo</strong> — anotações, destaques, versículos guardados e o diário de oração;</li>
<li><strong>seu progresso</strong> — capítulos lidos, planos, sequência de dias, conquistas e missões.</li>
</ul>
<p>Esses dados <strong>não são enviados para nossos servidores</strong> — o app não tem servidor próprio nem cadastro, e não temos acesso a eles. Os widgets leem um resumo (versículo do dia, sequência e próxima leitura) que também fica só no aparelho. Dependendo dos seus ajustes, esses dados podem fazer parte do backup do aparelho que a Apple faz para você; esse backup é controlado pela sua conta Apple, não por nós.</p>

<h2>Oração por voz: microfone e reconhecimento de fala</h2>
<p>Gravar uma oração por voz é opcional e só funciona se você permitir o microfone e o Reconhecimento de Fala. O app usa o reconhecimento de fala do próprio sistema da Apple para transformar a sua voz em texto. Quando o aparelho oferece reconhecimento no próprio dispositivo para o português, o app pede que a transcrição seja feita nele; quando não oferece, o áudio pode ser enviado à Apple para ser transcrito, conforme a política de privacidade dela. <strong>Nós não recebemos o áudio nem o texto</strong>: o app guarda apenas a transcrição, no seu aparelho, e não guarda a gravação. Você pode retirar essas permissões a qualquer momento nos Ajustes do aparelho e escrever suas orações com o teclado.</p>

<h2>Fotos</h2>
<p>Se você escolher salvar a imagem de um versículo, o app pede permissão apenas para <strong>adicionar</strong> essa imagem às suas Fotos. Ele não lê nem acessa as fotos que já estão no aparelho.</p>

<h2>Notificações</h2>
<p>Os lembretes são opcionais e só aparecem se você permitir. Eles são <strong>locais</strong>: agendados pelo próprio aparelho, sem passar por um servidor nosso. Você pode desligá-los a qualquer momento no app ou nos Ajustes do aparelho.</p>

<h2>Compartilhar e exportar</h2>
<p>Quando você compartilha um versículo, uma oração ou exporta suas anotações, é <strong>você</strong> quem escolhe o destino na folha de compartilhamento do sistema. O app não envia nada sozinho.</p>

<h2>Contato por e-mail</h2>
<p>Se você nos escrever, recebemos o que qualquer e-mail traz: seu endereço, o nome configurado na sua conta de e-mail e o texto que você escreveu. Usamos isso só para ler e responder.</p>

<h2>O que não coletamos</h2>
<ul>
<li>Não pedimos e-mail, telefone, data de nascimento nem criação de conta.</li>
<li>Não coletamos localização nem contatos.</li>
<li>Não usamos SDKs de análise ou de publicidade de terceiros e não rastreamos você entre apps ou sites.</li>
<li>Não exibimos anúncios.</li>
<li>Não vendemos, alugamos nem compartilhamos dados pessoais.</li>
</ul>

<h2>Compras</h2>
<p>A assinatura é vendida e cobrada pela Apple, pela App Store. O app recebe da Apple apenas a informação de que a sua assinatura está ativa, para liberar o {PLUS}. Não vemos, não recebemos e não guardamos dados do seu cartão. O tratamento que a Apple faz dos dados de compra segue a política de privacidade dela.</p>

<h2>Crianças</h2>
<p>O app é voltado a mulheres adultas e não é direcionado a crianças. Não coletamos dados pessoais de ninguém, inclusive de menores de idade.</p>

<h2>Como apagar os seus dados</h2>
<ul>
<li>Nos Ajustes do app, toque em <strong>“Apagar todos os meus dados”</strong>; ou</li>
<li>desinstale o app — os dados guardados no aparelho são removidos junto.</li>
</ul>
<p>Apagar os dados não cancela a assinatura: ela é gerenciada na sua conta Apple. Se você nos enviou um e-mail e quer que ele seja apagado, basta pedir em {MAIL}.</p>

<h2>Seus direitos (LGPD)</h2>
<p>A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) garante a você, entre outros, os direitos de confirmar a existência de tratamento, acessar, corrigir, eliminar e pedir a portabilidade dos seus dados, além de obter informações sobre compartilhamento e de revogar o consentimento.</p>
<p>Como não mantemos cadastro nem identificamos você, os dados do app simplesmente não estão em nossos sistemas — você os controla diretamente no aparelho. Os únicos dados pessoais que podemos ter são os de e-mails que você nos enviou. Para qualquer solicitação, escreva para {MAIL}. Você também pode recorrer à Autoridade Nacional de Proteção de Dados (ANPD).</p>

<h2>Mudanças nesta política</h2>
<p>Se esta política mudar, atualizamos a data no topo desta página. Mudanças relevantes — por exemplo, se o app passar a ter recursos online — serão descritas aqui antes de entrarem em vigor.</p>

<h2>Vigência</h2>
<p>Esta política vale a partir de 7 de outubro de 2026.</p>
""")

page("terms", "Termos de Uso", UPDATED, f"""
<div class="card">
<p><strong>O essencial:</strong> {BRAND} é um app de leitura bíblica, estudo e oração. Há uma parte gratuita e a assinatura {PLUS}, vendida e cobrada pela Apple, que você cancela quando quiser nos Ajustes do aparelho.</p>
</div>

<h2>1. Aceitação</h2>
<p>Ao usar o app {BRAND}, você concorda com estes termos. Se não concordar, não use o app.</p>

<h2>2. Licença de uso</h2>
<p>A Hermes Digital concede a você uma licença pessoal, limitada, não exclusiva, intransferível e revogável para usar o app nos aparelhos Apple que você possui ou controla, conforme as regras da App Store. O app, os devocionais, os planos, os estudos, o design e a marca pertencem à Hermes Digital ou aos seus licenciantes. Você concorda em não copiar, revender, fazer engenharia reversa nem tentar burlar o app.</p>

<h2>3. Textos bíblicos e conteúdo</h2>
<p>As traduções da Bíblia incluídas no app são obras em domínio público ou distribuídas sob licenças abertas, e pertencem aos seus respectivos titulares. Os créditos e as licenças de cada uma estão dentro do app, em Ajustes → Créditos e licenças; a licença de cada tradução continua valendo para o texto dela.</p>
<p>Os devocionais, estudos e reflexões têm <strong>caráter devocional e educativo</strong>. O app <strong>não tem vínculo com nenhuma igreja, denominação ou instituição religiosa</strong> e não substitui acompanhamento pastoral, psicológico ou médico. Traduções e tradições diferem entre si; cuidamos da precisão do conteúdo, mas erros podem acontecer — se encontrar um, avise em {MAIL}.</p>

<h2>4. Seu conteúdo</h2>
<p>Anotações, destaques e orações que você escreve são seus e ficam no seu aparelho. Não temos acesso a eles nem cópia deles; por isso, não temos como recuperá-los se o aparelho for perdido, trocado ou restaurado sem backup, ou se o app for desinstalado.</p>

<h2>5. Assinatura</h2>
<p>O app tem uma versão gratuita e o <strong>{PLUS}</strong>, oferecido como assinatura auto-renovável em dois planos: <strong>mensal</strong> e <strong>anual</strong>. O plano anual pode incluir um período de teste grátis de 7 dias, quando disponível para você.</p>
<ul>
<li>O preço e a periodicidade de cada plano são exibidos na tela de compra, antes da confirmação.</li>
<li>A cobrança é feita na sua conta Apple na confirmação da compra e a cada renovação.</li>
<li>A assinatura <strong>renova automaticamente</strong> ao fim de cada período, pelo mesmo preço, salvo se for cancelada com pelo menos 24 horas de antecedência do fim do período em curso.</li>
<li><strong>Teste grátis:</strong> ao fim do período de teste, a assinatura passa a ser cobrada automaticamente pelo preço exibido, a menos que você cancele com pelo menos 24 horas de antecedência do fim do teste.</li>
<li>Você gerencia e cancela a assinatura nos Ajustes do aparelho, em seu nome → Assinaturas. Desinstalar o app não cancela a assinatura. Após o cancelamento, o {PLUS} continua até o fim do período já pago.</li>
</ul>

<h2>6. Reembolsos</h2>
<p>As compras são processadas pela Apple e seguem as políticas dela. Pedidos de reembolso devem ser feitos em <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. Não temos como processar reembolsos diretamente. Nada aqui limita os direitos que a legislação de defesa do consumidor garante a você.</p>

<h2>7. Disponibilidade</h2>
<p>Fazemos o possível para manter o app funcionando bem, mas ele é fornecido “como está”. Não garantimos funcionamento ininterrupto nem ausência de erros, e podemos alterar, acrescentar ou retirar recursos e conteúdos.</p>

<h2>8. Limitação de responsabilidade</h2>
<p>Na máxima extensão permitida em lei, a Hermes Digital não se responsabiliza por danos indiretos decorrentes do uso do app, nem pela perda de conteúdo guardado no aparelho. A responsabilidade total, em qualquer hipótese, fica limitada ao valor efetivamente pago por você nos últimos doze meses.</p>

<h2>9. Apple</h2>
<p>O app é distribuído pela App Store. No que estes termos não tratarem, vale o <a href="{EULA}">Contrato de Licença de Usuário Final padrão da Apple (EULA)</a>. A Apple não é parte destes termos e não é responsável pelo app nem pelo suporte a ele.</p>

<h2>10. Privacidade</h2>
<p>O tratamento de dados está descrito na <a href="privacy">Política de Privacidade</a>.</p>

<h2>11. Alterações</h2>
<p>Podemos atualizar estes termos; a data no topo indica a última revisão. O uso continuado após a atualização representa concordância.</p>

<h2>12. Contato</h2>
<p>Contato: {MAIL}</p>
""")

page("support", "Suporte", TAG, f"""
<div class="card">
<p><strong>Fale com a gente:</strong> {MAIL}</p>
</div>

<h2>Como podemos ajudar</h2>
<p>Escreva para o e-mail acima contando o que aconteceu. Se for um problema no app, ajuda muito informar o modelo do aparelho, a versão do iOS e o que você estava fazendo na hora.</p>

<h2>Assinatura</h2>
<ul>
<li><strong>Cancelar:</strong> Ajustes do aparelho → seu nome → Assinaturas → {BRAND}. Desinstalar o app não cancela a assinatura.</li>
<li><strong>Restaurar:</strong> na tela do {PLUS}, toque em “Restaurar compra”, ou em Ajustes do app → “Restaurar compras”, usando a mesma conta Apple da compra.</li>
<li><strong>Reembolso:</strong> é a Apple quem processa, em <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
</ul>

<h2>Lembretes não chegam</h2>
<p>Confira se as notificações do app estão permitidas em Ajustes do aparelho → Notificações, e se o horário do lembrete está ligado dentro do app.</p>

<h2>Seus dados</h2>
<p>Anotações, orações e progresso ficam só no aparelho. Para apagar tudo, use “Apagar todos os meus dados” nos Ajustes do app, ou desinstale o app. Detalhes na <a href="privacy">Política de Privacidade</a>.</p>

<h2>Documentos</h2>
<ul>
<li><a href="terms">Termos de Uso</a></li>
<li><a href="privacy">Política de Privacidade</a></li>
</ul>
""")
