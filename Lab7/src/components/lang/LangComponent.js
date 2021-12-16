export class LangComponent {
    constructor(parent) {
        this.parent = parent
    }

    getHTML(data) {
        return (
            `
            <div class='card text-white bg-dark' style='width: 300px'>
                <div class="card-header">
                    Язык программирования
                </div>
                <div class='card-body'>
                    <h4 class='card-title'>${data.language_name}</h4>
                    <p class='card-text'>${data.descript}</p>
                    <p class='card-text'>Год создания: ${data.creation_year}</p>
                </div>
            </div>
            `
        )
    }

    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
    }
}