import { LangCardComponent } from "../../components/lang/LangCardComponent.js"
import { ajax } from "../../modules/ajax.js"
import { urls } from "../../modules/urls.js"
import { LangPage } from "../../pages/lang/LangPage.js"

export class MainPage {
    constructor(parent) {
        this.parent = parent
    }

    async getData() {
        return ajax.get(urls.langs())
    }

    page() {
        return document.getElementById('main-page')
    }

    getHTML() {
        return '<div id="main-page" class="d-flex flex-wrap"><div/>'
    }

    clickCard(e) {
        const cardId = e.target.dataset.id
        const langPage = new LangPage(this.parent, cardId)
        langPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const data = await this.getData()
        data.data.forEach((item) => {
            const lang_card = new LangCardComponent(this.page())
            lang_card.render(item, this.clickCard.bind(this))
        })
    }
}