export class LangCardComponent {
    constructor(parent) {
        this.parent = parent
    }

    getHTML(data) {
        return (
            `
            <div class='card text-white text-center bg-dark'>
                <div class='card-body'>
                    <h4 class='card-title'>${data.language_name}</h4>
                    <!--<p class='card-text'>${data.descript}</p>-->
                    <!--<p class='card-text'>${data.creation_year}</p>-->
                    <button class='btn btn-primary', id='click-card-${data.id_language}', data-id='${data.id_language}'>Подробнее</button>
                </div>
            </div>
            `
        )
    }

    addListeners(data, listener) {
        document.getElementById(`click-card-${data.id_language}`).addEventListener('click', listener)
    }

    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
}