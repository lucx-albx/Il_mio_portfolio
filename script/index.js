const Thome = document.querySelector(".home-text")
const Tprogetti = document.querySelector(".progetti-text")
const Tabout = document.querySelector(".about-text")
const duration = 1500
const interval = 10
const API_PROGETTI = "https://raw.githubusercontent.com/lucx-albx/Progetti/main/Progetti.json"

let sezione = sessionStorage.Sezione === undefined ? "Home" : sessionStorage.Sezione
let isAnimationRunning = false
let isAnimationRunningPercentuale = false

const carica_impostazioni =()=>{

    if (sezione !== Thome.textContent.trim()){
        Thome.style.color = "#99a1aa"
        Thome.style.fontWeight = "400"
    } else {
        Thome.style.color = "white"
        Thome.style.fontWeight = "700"
    }
        
    if(sezione !== Tprogetti.textContent.trim()){
        Tprogetti.style.color = "#99a1aa"
        Tprogetti.style.fontWeight = "400"
    } else {
        Tprogetti.style.color = "white"
        Tprogetti.style.fontWeight = "700"
    }

    if(sezione !== Tabout.textContent.trim()){
        Tabout.style.color = "#99a1aa"
        Tabout.style.fontWeight = "400"
    } else {
        Tabout.style.color = "white"
        Tabout.style.fontWeight = "700"
    }

}

const evidenzia =(el)=>{
    el.style.fontWeight = "700"
    el.style.color = "white"

    if (el.textContent.trim() !== Thome.textContent.trim()){
        sessionStorage.setItem("Sezione", el.textContent.trim())

        Thome.style.color = "#99a1aa"
        Thome.style.fontWeight = "400"
    }
        
    if(el.textContent.trim() !== Tprogetti.textContent.trim()){
        sessionStorage.setItem("Sezione", el.textContent.trim())

        Tprogetti.style.color = "#99a1aa"
        Tprogetti.style.fontWeight = "400"
    }

    if(el.textContent.trim() !== Tabout.textContent.trim()){
        sessionStorage.setItem("Sezione", el.textContent.trim())

        Tabout.style.color = "#99a1aa"
        Tabout.style.fontWeight = "400"
    }
    
}

const apri_menu =()=>{
    let controlla = document.querySelector(".tipi-sezioni")
    let altezza = -130

    controlla.style.top = altezza + 'px'

    let id = setInterval(frame, 1)

    if(controlla.classList.contains("not-visible"))
        controlla.classList.remove("not-visible")
    else
        controlla.classList.add("not-visible")

    function frame(){
        if (altezza === 68) {
            clearInterval(id)
        } else {
            altezza++
            controlla.style.top = altezza + 'px'
        }
    
    }
    
}

const checkScreenWidth =()=> {
    let controlla = document.querySelector(".tipi-sezioni")
    let descrizione = document.querySelector(".desc")
    let servizi = document.querySelector(".ser")

    if (window.innerWidth >= 768) {
        controlla.classList.add("visible-tel")
        descrizione.classList.add("posiziona-verticale-centrale")
        servizi.classList.add("posiziona-verticale-centrale")        
    } else {
        controlla.classList.remove("visible-tel")
        servizi.classList.remove("posiziona-verticale-centrale")
        descrizione.classList.remove("posiziona-verticale-centrale")
    }

}

const anima_numero_progetti =(finalNumber, numero)=> {
    let currentNumber = 0
    const increment = finalNumber / (duration / interval)

    const intervalId = setInterval(() => {
        currentNumber += increment
        numero.textContent = Math.round(currentNumber)

        if (currentNumber >= finalNumber) {
            numero.textContent = finalNumber
            clearInterval(intervalId)
        }
    }, interval)
}

class card_progetti{

    crea(nome, desc, link){
        return (
                `<div class="col-xl-3 col-lg-3 col-md-5 col-10 card-progetti" data-aos="fade-right" data-aos-offset="10" data-aos-easing="ease-in-sine">
                        <h2 class="text-center testo-progetti-tit">${nome}</h2>
                        <p>
                            ${desc}
                        </p>
                        <a href="${link}" target="_blank" class="more mt-2 d-flex justify-content-start align-items-center">Esplora <svg class="centra-freccia" height="20" width="25" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75" stroke-linejoin="round" stroke-linecap="round"></path></svg></a>
                </div>`
            )
    }

    crea_python(nome, desc, link, percentuale){
        return (
            `<div class="col-xl-3 col-lg-3 col-md-5 col-10 card-progetti" data-aos="fade-right" data-aos-offset="10" data-aos-easing="ease-in-sine">
                    <h2 class="text-center testo-progetti-tit">${nome}</h2>
                    <p>
                        ${desc}
                    </p>
                    <a href="${link}" class="more mt-2 d-flex justify-content-start align-items-center" download>Scarica <svg class="centra-freccia" height="20" width="25" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75" stroke-linejoin="round" stroke-linecap="round"></path></svg></a>
            </div>`
        )

    }

}

const carica_progetti =()=>{
    
    let main_webapp = document.querySelector(".proj-webapp")
    let main_siti = document.querySelector(".proj-siti")
    let main_python = document.querySelector(".proj-python")
    let insert = ""

    fetch(API_PROGETTI)
    .then(testo=>testo.json())
    .then((data)=>{
        try {
            //carico info webapp
            data.Web_app.map((elem, i)=>{
                insert += new card_progetti().crea(elem.nome, elem.descrizione, elem.link)
            })

            main_webapp.innerHTML = insert

            //carico info siti web
            insert = ""

            data.Siti_web.map((elem, i)=>{
                insert += new card_progetti().crea(elem.nome, elem.descrizione, elem.link)
            })

            main_siti.innerHTML = insert

            //carico info python
            insert = ""

            data.Python_progetti.map((elem, i)=>{
                insert += new card_progetti().crea_python(elem.nome, elem.descrizione, elem.link, "100")
            })

            main_python.innerHTML = insert

        } catch(err){}
    })
    
}

const carica_percentuali =()=>{
    let progressHtml = document.querySelector(".completamento1")
    let progressCss = document.querySelector(".completamento2")
    let progressJs = document.querySelector(".completamento3")
    let progressReact = document.querySelector(".completamento4")
    let progressPython = document.querySelector(".completamento5")
    let progressC = document.querySelector(".completamento6")
    let progressBash = document.querySelector(".completamento7")
    let progressSql = document.querySelector(".completamento8")
    let progressFirebase = document.querySelector(".completamento9")
    
    progressHtml.classList.add("animate")
    progressCss.classList.add("animate")
    progressJs.classList.add("animate")
    progressReact.classList.add("animate")
    progressPython.classList.add("animate")
    progressC.classList.add("animate")
    progressBash.classList.add("animate")
    progressSql.classList.add("animate")
    progressFirebase.classList.add("animate")
}

const scrollToTop =()=> {
    const topElement = document.documentElement;
    topElement.scrollIntoView({
        behavior: 'smooth'
    })
}

checkScreenWidth()
window.addEventListener('resize', checkScreenWidth)

window.addEventListener('scroll', () => {
    try{
        const section = document.getElementById('animazionePercentuale')
        const sectionTop = section.getBoundingClientRect().top

        if (sectionTop <= window.innerHeight / 2 && !isAnimationRunningPercentuale) {
            carica_percentuali()

            isAnimationRunningPercentuale = true
        }
    } catch(err){}

})

window.addEventListener('scroll', () => {
    try{
        const section = document.getElementById('animazioneNumeri')
        const sectionTop = section.getBoundingClientRect().top

        if (sectionTop <= window.innerHeight / 2 && !isAnimationRunning) {
            anima_numero_progetti(12, document.querySelector(".progetti-pubblicati-numero"))
            anima_numero_progetti(30, document.querySelector(".progetti-sviluppati-numero"))
            anima_numero_progetti(6, document.querySelector(".progetti-iconici-numero"))
            anima_numero_progetti(10, document.querySelector(".progetti-webapp-numero"))

            isAnimationRunning = true
        }
    } catch(err){}

})

carica_progetti()


