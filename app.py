from flask import Flask,render_template,redirect,url_for,abort


app = Flask(__name__,static_url_path='/static')

links = ["Heim","Lögreglan hafði afskipti af nýnasistum","Samkomulag um örugga skemmti staða og gegn vændi"]
hrefs = ["/","Logreglan_hafdi_afskipti__af_nynasistum","Samkomulag_um_orugga_skemmti_stada_og_gegn_vaendi"]

Mainpage = {
                "title":"Fréttir",
                "Writer":"Friðrik Fannar Söebech",
                "Date":"10.9.2019",
                "Time of Creation": "19:22"
            }

content = {"Logreglan_hafdi_afskipti__af_nynasistum":{"title":"Lögreglan hafði afskipti af nýnasistum",
                                                "mainContent":"Félagsmenn í nýnasistasamtökunum Norðurvígi komu saman á "
                                                "Lækjartorgi í Reykjavík í dag og dreifðu áróðri sínum. "
                                                "Tilkynnt var um veru þeirra þar og mætti lögreglan á staðinn."
                                                "Rafn Hilmar Guðmundsson, aðalvarðstjóri hjá lögreglu "
                                                "höfuðborgarsvæðisins, staðfestir í samtali við mbl.is að "
                                                "tilkynning hafi borist í þessum efnum og að lögregluþjónar "
                                                "hafi verið sendir á staðinn. Þeir hafi rætt við mennina og "
                                                "tekið niður nöfn þeirra."
                                                "Dreifirit, sem mennirnir buðu vegfarendum að taka við, "
                                                "er það sama og dreift var í íbúðarhús á Kársnesi í "
                                                "Kópavogi í gær og hugsanlega víðar á höfuðborgarsvæðinu."
                                                "Þar segir meðal annars að hugmyndafræði samtakanna sé "
                                                "þjóðernisfélagshyggja sem er bein þýðing á þýska hugtakinu "
                                                "„Nationalsozialismus“ sem aft­ur er sú stefna sem "
                                                "þýskir nasistar undir forystu Adolfs Hitlers "
                                                "stóðu fyrir á fyrri hluta síðustu aldar."
                                                "Samtökin eru hluti af norrænni hreyfingu nýnasista.",
                                                "Writer":"Arnþór",
                                                "Date":"5.9.2019",
                                                "Time of Creation": "13:15",
                                                "image":"police_img.jpg"},
           "Samkomulag_um_orugga_skemmti_stada_og_gegn_vaendi":{"title":"Samkomulag um örugga skemmtistaða og gegn vændi",
                                                        "mainContent":"Samkomulag um að bæta öryggi á og við "
                                                            "skemmtistaði í "
                                                            "Reykjavík var undirritað í dag, svo og samkomulag um "
                                                            "að sporna gegn vændi á hótelum og gistiheimilum."
                                                            "Þetta kemur fram í tilkynningu frá Reykjavíkurborg."
                                                            "Þar seg­ir að vel hafi gengið að fá starfsfólk "
                                                            "skemmtistaða til að sækja námskeið og skrifa undir"
                                                            " yfirlýsingu um að gera sitt til að fyrirbyggja "
                                                            "allt ofbeldi á skemmtistöðum. Ofbeldi í hvaða mynd"
                                                            " sem er eigi ekki að líðast; þar með talið "
                                                            "kynferðisleg áreitni, vændi og mansal, sem og ofbeldi"
                                                            " sem byggist á fordómum eða hatri, svo sem í garð"
                                                            " innflytjenda eða hinsegin fólks."
                                                            "Auk fræðslu fyrir dyraverði og starfsfólk felur"
                                                            "samkomulagið í sér að farið er í úttektarheimsóknir"
                                                            "á skemmtistaði. Markmiðið er að efla öryggi borgarbúa"
                                                            "allra. Forsvarsmenn, rekstraraðilar og starfsfólk"
                                                            "skemmtistaða, lögreglan, slökkviliðið og"
                                                            "Reykjavíkurborg líta á sig sem samstarfsaðila enda"
                                                            "eru hagsmunirnir sameiginlegir, aukið öryggi"
                                                            "borgaranna."
                                                            "Einnig gerði borgin, Samtök ferðaþjónustu (SAF),"
                                                            "fyrir hönd hótela og gististaða í Reykjavík,"
                                                            "og Lögreglan á höfuðborgarsvæðinu með sér samkomulag"
                                                            "um að vinna saman að því að uppræta vændi á  hótelum"
                                                            "og gististöðum."
                                                            "Markmið samkomulagsins er að skapa ofbeldislaust"
                                                            "og öruggt umhverfi fyrir gesti og starfsfólk hótela"
                                                            "og gististaða. Stefnt er að því að vændiskaup verði"
                                                            "ávallt tilkynnt og vændisseljendum veittar"
                                                            "upplýsingar um þann stuðning sem þeim stendur til boða."
                                                            "Aðilar samkomulagsins eru meðvitaðir um að í mörgum "
                                                            "tilvikum tengjast vændi og mansal órofa böndum þar "
                                                            "sem vændisseljendur virðast oft ginntir til starfans.",
                                                        "Writer":"N/A",
                                                        "Date":"10.9.2019 ",
                                                        "Time of Creation": "19:49",
                                                        "image":"vaendi.jpg"}}

@app.route('/')
def index():
    return render_template('Contentpage.html', cnt=Mainpage,link_data=zip(hrefs,links), subpage = False)

@app.route('/<news>')
def sub(news):
    if news in content:
        return render_template('Contentpage.html', cnt=content[news], link_data=zip(hrefs, links), subpage=True)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
