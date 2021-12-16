import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp";
import FooterComp from "../components/FooterComp";


function ObjectPage(params) {
    const langsList = params.location.data
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Язык программирования {langsList.language_name}</h2>
            <h4>Описание языка:</h4>
            <p>{langsList.descript}</p>
            <p><b>Год создания: </b>{langsList.creation_year}</p>
            <Link to="/list"><button>Назад</button></Link>
            <FooterComp></FooterComp>
        </div>
    );
}

export default ObjectPage;