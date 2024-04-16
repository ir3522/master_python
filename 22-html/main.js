/*alert('hola mundo');*/
var nombre = "Isaac Romero";
var altura = 170;
var concatenacion = nombre + " " + altura;

/*document.write(concatenacion);*/
var datos = document.getElementById("datos");
/*datos.innerHTML = concatenacion;*/
datos.innerHTML = `<h1> soy la caja de datos </h1>
    <h2> mi nombre es: ${nombre} </h2>
    <h3>mido: ${altura}</h3>
    `;

    if( altura >= 190){
        datos.innerHTML += `<h1> eres una persona alta </h1>`;
    }else{
        datos.innerHTML += `<h1> eres una persona baja </h1>`;
    }
    ;