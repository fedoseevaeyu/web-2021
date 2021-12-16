import { LangComponent } from "../../components/lang/LangComponent.js"
import { BackButtonComponent } from "../../components/back-button/BackButtonComponent.js"
import { MainPage } from "../main/MainPage.js"
import { ajax } from "../../modules/ajax.js"
import { urls } from "../../modules/urls.js"

export class LangPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }

    async getData() {
        return ajax.get(urls.lang(this.id))
    }

    page() {
        return document.getElementById('stock-page')
    }

    getHTML() {
        return '<div id="stock-page"></div>'
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const back_button = new BackButtonComponent(this.page())
        back_button.render(this.clickBack.bind(this))

        const data = await this.getData()
        const lang_card = new LangComponent(this.page())
        lang_card.render(data.data)
    }
}