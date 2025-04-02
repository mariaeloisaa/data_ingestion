
// //FATCH

// async function puxando_api() {
//     const response = await fetch("http://localhost:8000/api/v1/wilson/");
//     const data = await response.json();
//     return data
// }

// async function mostrar_info() {
//     const wilsons = await puxando_api();
//     const conteiner = document.getElementById("wilson-conteiner")
//     wilsons.forEach(wilson => {
//         const wilsonDiv = document.createElement("div");
//         wilsonDiv.classList.add("Wilson")
//         wilsonDiv.innerHTML=`
//             <h2>${wilson.nome}</h2>
//             <img src="${wilson.especialidade}"></img>
//             <p>${wilson.especialidade}</p>
//             <p>${wilson.poder}</p>
//         `;
//         conteiner.appendChild(wilsonDiv);
//     });
    
// }

// mostrar_info()




// AXIOS

async function puxar_api() {
    await axios.get("http://localhost:8000/api/v1/wilson/").then((response) => {
        const wilsons = response.data;
        const conteiner = document.getElementById("wilson-conteiner")
        wilsons.forEach(element => {
            const wilsonDiv = document.createElement("div");
            wilsonDiv.classList.add("wilson")
            wilsonDiv.innerHTML = `
            <h2>${element.nome}</h2>
            <img src="${element.especialidade}"></img>
            <p>${element.especialidade}</p>
            <p>${element.poder}</p>
            
            `
            conteiner.append(wilsonDiv)
        })
    })
}

puxar_api()