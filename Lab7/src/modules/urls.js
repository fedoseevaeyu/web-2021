class Urls {
    constructor() {
        this.url = 'http://localhost:8000/api/';
    }

    langs() {
        return `${this.url}lang/`
    }

    lang(id) {
        return `${this.url}lang/${id}/`
    }
}

export const urls = new Urls()