import streamlit as st

st.set_page_config(page_title="Stadt Führer für Jerusalem", layout="wide")

# Titel
st.markdown("<h1 style='text-align: center;'>Stadtführer für Jerusalem</h1>", unsafe_allow_html=True)

# Button "Quelle" oben rechts mit Anzeige der Quellen bei Klick
col_quelle, col_leer = st.columns([9, 1])
with col_leer:
    if st.button("Quellen", key="quelle_btn", help="Informationen zu den Quellen anzeigen", use_container_width=True):
        st.session_state["show_quellen"] = True

# Quellen-Infobox anzeigen, wenn Button geklickt wurde (schwarzer Kasten)
if st.session_state.get("show_quellen", False):
    st.markdown(
        """
        <div style="background-color: #080808; color: #fff; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <b>Quellen:</b><br>
            - Tripadvisor <br>
            - Religionen-entdecken.de <br>
            - Wikipedia <br>
            - Googlemaps <br>

        </div>
        """,
        unsafe_allow_html=True
    )
    # Button zum Schließen der Quellenbox
    if st.button("Schließen", key="close_quellen", use_container_width=True):
        st.session_state["show_quellen"] = False

# Session-State initialisieren
if "btn" not in st.session_state:
    st.session_state["btn"] = None

# Drei große Buttons nebeneinander (Streamlit-only)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🛐 Christen", use_container_width=True):
        st.session_state["btn"] = "christen"

with col2:
    if st.button("✡️ Juden", use_container_width=True):
        st.session_state["btn"] = "juden"

with col3:
    if st.button("☪️ Muslime", use_container_width=True):
        st.session_state["btn"] = "muslime"

# Infobox-Funktion mit Google-Maps-Link und Quellenangabe
def zeige_infokasten(bild_url, titel, text, maps_url, quelle):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="{bild_url}" width="1200" style="border-radius:10px;">
        </div>
        """,
        unsafe_allow_html=True,
        
    )
    st.subheader(titel)
    st.markdown(f"<h4 style='font-size:1.3em'>{text}</h4>", unsafe_allow_html=True)
    st.write("Bildquelle:",bild_url)
    st.link_button("📍 Auf Google Maps ansehen", url=maps_url)
    st.markdown("---")


def lese_datei(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:
        return datei.read()

btn = st.session_state["btn"]

# Inhalte für Christen
if btn == "christen":
    st.subheader("⛪ Jerusalem für die Christen")
    zeige_infokasten(
        "https://dannythedigger.com/wp-content/uploads/shutterstock_1324655747-ascension.jpg",
        "Himmelfahrtskapelle",
        "Die Himmelfahrtskapelle liegt an der höchsten Stelle des Ölbergs. Hier soll Jesus Christus seinen Fußabdruck hinterlassen haben. Sie ist heute eine Moschee. Trotzdem treffen sich hier in jedem Jahr christliche Pilger, um das Himmelfahrtsfest zu feiern.",
        "https://www.google.com/maps/place/Chapel+of+the+Ascension/@31.7788971,35.2424885,17z/data=!3m1!4b1!4m6!3m5!1s0x150329bb08e80265:0x5cf7f78b1d60fd29!8m2!3d31.7788971!4d35.2450634!16s%2Fm%2F09k70nx?entry=ttu&g_ep=EgoyMDI1MDQyOS4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://entail-assets.com/artzabox/Walking%20Via%20Dolorosa-1646747723861.jpg",
        "Via Dolorosa",
        "Die Via Dolorosa heißt auch Der Weg der Schmerzen. Diesen Weg musste Jesus nach seiner Verurteilung bis zum Hügel Golgotha gehen. Dort wurde er ans Kreuzgeschlagen und starb. Noch heute denken Christinnen und Christen an jedem Freitag mit einer Prozession daran.",
        "https://www.google.com/maps/place/Via+Dolorosa/@31.7794091,35.2291372,17z/data=!3m1!4b1!4m6!3m5!1s0x1502d7d634ea0083:0x69e91e50f2dd6fc5!8m2!3d31.7794091!4d35.2317121!16s%2Fg%2F1tk1wdmv?entry=ttu&g_ep=EgoyMDI1MDQyOS4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://www.diesenhaus.de/fileadmin/_migrated/pics/Kirche_aller_Nationen.jpg",
        "Garten Gethsemane",
        "Im Garten Gethsemane  soll Jesus vor seiner Festnahme gebetet haben, während seine Jünger schliefen. Dort versammelten sich später auch die ersten Christinnen und Christen.",
        "https://www.google.com/maps/place/Getsemani/@31.7742252,35.2331745,14.67z/data=!4m6!3m5!1s0x150329b84d1803cd:0x9b6e50a1cb5945d8!8m2!3d31.7793098!4d35.2397801!16zL20vMDIwa3hr?entry=ttu&g_ep=EgoyMDI1MDQyOS4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://arthur-hotel-an-atlas-boutique-hotel-jerusalem.hotel-mix.de/data/Photos/OriginalPhoto/12779/1277960/1277960350/Arthur-Hotel-An-Atlas-Boutique-Hotel-Jerusalem-Exterior.JPEG",
        "Arthur Hotel",
        "Das Arthur Hotel ist ein modernes Hotel im Herzen Jerusalems. Es bietet eine komfortable Unterkunft für christliche Touristen, die die Stadt erkunden möchten. Mit einem Preis von 169 Euro ist es eine sehr gute Wahl. Das Hotel ist mitten in der altstadt und man kann viele sehenswürdigkeiten zu fuß erreichen.", 
        "https://www.google.com/maps/place/Arthur/@31.7820915,35.2029802,15z/data=!4m13!1m2!2m1!1sArthur!3m9!1s0x150329d6fc2fb16b:0x3df2e7b8cca148a2!5m2!4m1!1i2!8m2!3d31.7820923!4d35.2185469!15sCgZBcnRodXJaCCIGYXJ0aHVykgEFaG90ZWyqAToQASoKIgZhcnRodXIoBTIeEAEiGtxkRPbdHgXYqkZMitHnnetyYUlTcyNTiRpoMgoQAiIGYXJ0aHVy4AEA!16s%2Fg%2F12hkhbhdm?entry=ttu&g_ep=EgoyMDI1MDUwNi4wIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D",
        "platzhalter der code ist in der sicht  etwas unordentlich geworden..."
    )



# Inhalte für Juden
elif btn == "juden":
    st.subheader("🕍 Jerusalem für die Juden")
    zeige_infokasten(
        "https://upload.wikimedia.org/wikipedia/commons/6/69/Yad_Vashem_Hall_of_Names_by_David_Shankbone.jpg",
        "Jad Waschem",
        "Yad Vashem, die Internationale Holocaust Gedenkstätte, wurde im Jahr 1953 durch ein von der Knesset, dem israelischen Parlament, beschlossenes Gesetz gegründet. Seine Aufgabe ist das Gedenken an den Holocaust, seine Dokumentation, Erforschung und Vermittlung.",
        "https://www.google.com/maps/place/Jad+Waschem/@31.7741981,35.1727269,17z/data=!3m1!4b1!4m6!3m5!1s0x150329d1a4886b3f:0x642a9fd5d5c70ae6!8m2!3d31.7741936!4d35.1753018!16zL20vMDE4dnd3?entry=ttu&g_ep=EgoyMDI1MDUwMy4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://www.diesenhaus.de/fileadmin/user_upload/Klagemauer_Jerusalem.jpg",
        "Klagemauer",
        "Im Judentum war der Tempel und damit die Klagemauer ein Ort, an dem Gott zu den Gläubigen kommt und gilt als heiligster Ort der Juden. Aufgrund dieser Annahme ist auch das Ritual der kleinen Zettel mit Gebeten oder mit verschiedenen Segenswünschen entstanden.",
        "https://www.google.com/maps/place/Klagemauer/@31.7767189,35.2319336,17z/data=!3m1!4b1!4m6!3m5!1s0x150329c939ceab8f:0x83ad5efed1777179!8m2!3d31.7767189!4d35.2345085!16zL20vMGpfcHA?entry=ttu&g_ep=EgoyMDI1MDUwMy4wIKXMDSoASAFQAw%3D%3D",
        "Yad Vashem"
    )
    zeige_infokasten(
        "https://www.disorient.de/sites/disorient.de/files/styles/blog_detail_image/public/blog/israel-20132-aerial-jerusalem-temple_mount-al-aqsa_and_dome_of_the_rock_se_exposure.jpg?itok=9jGhoqHa",
        "Tempelberg",
        lese_datei("app/tberg"),
        "https://www.google.com/maps/place/Temple+Mount/@31.7781161,35.2334178,17z/data=!3m1!4b1!4m6!3m5!1s0x150329c91f33ffdb:0x6d2bbd5ce62d60ab!8m2!3d31.7781161!4d35.2359927!16zL20vMGhmOGc?entry=ttu&g_ep=EgoyMDI1MDUwMy4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://upload.wikimedia.org/wikipedia/commons/4/4c/2013-Aerial-Mount_of_Olives.jpg",
        "Ölberg",
        "Als König David vor seinem rebellierenden Sohn Absalom fliehen musste, verließ er schweren Herzens Jerusalem und stieg den Ölberg hinauf – barfuß, weinend und tief erschüttert (2. Samuel 15,30). Der Ölberg wurde so zum Ort des Schmerzes, aber auch der Hoffnung.",
        "https://www.google.com/maps/place/%C3%96lberg/@31.7779296,35.2250987,14z/data=!3m1!4b1!4m6!3m5!1s0x150329b09e2e946b:0xd35396668e71535c!8m2!3d31.7779317!4d35.2456983!16zL20vMGo0ODg?entry=ttu&g_ep=EgoyMDI1MDUwMy4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://bilder.deutschlandfunk.de/FI/LE/_e/f8/FILE_ef80cdd78dd6134447177d954ccc33f1/000-mv44z-jpg-100-1280x720.jpg",
        "Grabeskirche",
        "Am Ende der Via Dolorosa, des traditionellen Leidenswegs Jesu, liegt in der Altstadt von Jerusalem eines der heiligsten Heiligtümer der Christenheit: die Grabeskirche. Der Überlieferung nach markiert sie den Ort, an dem Jesus gekreuzigt wurde – Golgatha – und zugleich seine letzte Ruhestätte, das heilige Grab.",
        "https://www.google.com/maps/place/Grabeskirche/@31.7784813,35.2270253,17z/data=!3m1!4b1!4m6!3m5!1s0x150329cf1c246db5:0x2d04a75cfc390360!8m2!3d31.7784813!4d35.2296002!16zL20vMDI1eWc?entry=ttu&g_ep=EgoyMDI1MDUwMy4wIKXMDSoASAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://www.wyndhamhotels.com/content/dam/property-images/en-us/ra/il/others/jerusalem/23777/23777_exterior_view_12.jpeg?crop=5976:3984;*,*&downsize=1800:*",
        "Ramada Jerusalem Hotel",
        "Nur wenige Gehminuten von der lebendigen Innenstadt Jerusalems entfernt bietet dieses moderne Hotel eine ideale Unterkunft für jüdische Touristen. Mit einem Preis von nur etwa 100 Euro pro Nacht verbindet es Komfort, zentrale Lage und ein hervorragendes Preis-Leistungs-Verhältnis. Das Hotel ist auf die Bedürfnisse jüdischer Gäste ausgerichtet – mit koscherer Küche, Schabbat-freundlicher Ausstattung und persönlichem Service, der auf Tradition und Gastfreundschaft Wert legt.",
        "https://www.google.com/maps/place/Ramada+by+Wyndham+Jerusalem/@31.7832803,35.1938737,17z/data=!4m9!3m8!1s0x1502b6fd51a25c4d:0x9dac9009b9ad9fee!5m2!4m1!1i2!8m2!3d31.7832803!4d35.1964486!16s%2Fg%2F1tcxm00r?entry=ttu&g_ep=EgoyMDI1MDUwMy4wIKXMDSoASAFQAw%3D%3D",
        "Tripadvisor"
    )
    




# Inhalte für Muslime
elif btn == "muslime":
    st.subheader("🕌 Jerusalem für die Muslime")
    zeige_infokasten(
        "https://upload.wikimedia.org/wikipedia/commons/d/d3/16-04-04-Felsendom-Tempelberg-Jerusalem-RalfR-WAT_6385.jpg",
        "Felsendom",
        lese_datei("app/fdom"),
        "https://www.google.com/maps/place/Dome+of+the+Rock/@31.7780451,35.2328206,17z/data=!3m1!4b1!4m6!3m5!1s0x150329c86ce8896f:0xe33f01a44e2808aa!8m2!3d31.7780191!4d35.2354079!16zL20vMGhmOWQ?entry=ttu&g_ep=EgoyMDI1MDUwNi4wIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Jerusalem-2013-Temple_Mount-Al-Aqsa_Mosque_%28NE_exposure%29.jpg/2880px-Jerusalem-2013-Temple_Mount-Al-Aqsa_Mosque_%28NE_exposure%29.jpg",
        "Al-Aqsa-Moschee",
        "Die eher unauffällige Al-Aqsa-Moschee gleich neben dem Felsendom gilt im Islam als drittheiligste Moschee. In der Anfangszeit beteten Musliminnen und Muslime auch nicht Richtung Mekka, sondern Richtung Jerusalem. Erst nachdem sich Mohammed mit den jüdischen Stämmen Medinas zerstritten hatte, änderte er die Gebetsrichtung zur Kaaba nach Mekka.",
        "https://www.google.com/maps/place/al-Aqsa-Moschee/@31.7760692,35.2357802,17z/data=!3m1!4b1!4m6!3m5!1s0x150329c9c96f3a51:0x9d880658c9248aad!8m2!3d31.7760692!4d35.2357802!16zL20vMGhmazE?entry=ttu&g_ep=EgoyMDI1MDUwNi4wIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://www.israelmagazin.de/wp-content/webp-express/webp-images/uploads/2020/09/jerusalem-altstadt-arabisch-1692962.jpg.webp",
        "Mulimischesviertel In der Altstadt ",
        lese_datei("app/astadt"),
        "https://www.google.com/maps/place/Old+City,+Jerusalem/@31.779873,35.2143195,14.33z/data=!4m6!3m5!1s0x150329c8dc262c8b:0x9ab61a59c838a400!8m2!3d31.7767923!4d35.2310338!16zL20vMDFzM3dr?entry=ttu&g_ep=EgoyMDI1MDUwNi4wIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D",
        "Wikipedia"
    )
    zeige_infokasten(
        "https://cdn.worldota.net/t/828x560/content/b6/c6/b6c60f5242c7d78490229ae7c5d379494dd8a149.jpeg",
        "Blick auf Tempelberg ",
        "Blick auf Tempelberg auf Ölberg mitten in  Altstadt 82 Euro pro Nacht in dem Hotel gibt es zwei Kühlschänke und das Frühstück und Abendessen ist halal.",
        "https://www.google.com/maps/place/Jerusalem+Panorama+Hotel./@31.7731391,35.2374192,17z/data=!4m9!3m8!1s0x150329b6e660864d:0x406058ccac25b233!5m2!4m1!1i2!8m2!3d31.7731391!4d35.2399941!16s%2Fg%2F1tfm3_sz?entry=ttu&g_ep=EgoyMDI1MDUwNi4wIKXMDSoJLDEwMjExNDU1SAFQAw%3D%3D",
        "Tripadvisor"
    )
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("**© 2025 Stadtführer Jerusalem – Lirox-python.**")
    st.markdown("**Alle Rechte vorbehalten.**")
    st.markdown("**Diese Anwendung ist nicht mit Google verbunden.**")
#hallo github nutzer dies ist eine anmerkung an euch der code wurde von mir erstellt bitte entschuldigt bugs oder kleinere fehler soweit sollte aber alles klar gehen ps: ihr dürft den code gerne auch für andere projekte verwenden ich würde mich aber freuen wenn ihr mich als autor angeben würdet. Lirox-python