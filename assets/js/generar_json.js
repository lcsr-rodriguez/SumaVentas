/**
 * @author          Leiner Ceballos Rodriguez
 * @version         npm 6.14.8
 * @description     Genera una cantidad de datos a partir de una URI
 */

// Retorna a partir de una promise un objeto JSON
async function getRandomData() {
  try {
    const data = await axios.get("https://random-data-api.com/api/commerce/random_commerce?size=100");
    var txt = objectToString(data);
    return txt;
  } catch(err) {
    console.log("error: ", err);
  }
}

// Retorna un String con la informacion del objeto
function objectToString(json) {
  var array = [];
    Object.keys(json).forEach(function(key) {
      array.push(json[key]);
    });
    
    var result = JSON.stringify(array[0]);
    var first = result.slice(1); // remueve el primer caracter
    var last = first.slice(0, first.length - 1); // remueve el ultimo caracter
    
    return last;
}

$(document).ready(function(){
  // Recuperar el dato asincrono
  var objeto = []
  
  // Numero de veces que desea enviar la peticion
  for(var i=0; i<100; i++) {
    getRandomData().then(v => {
      objeto.push(v);

    })
    .finally(() => {
      console.log("Promesa finalizada")
    });
  }

  setTimeout(function(){
     var data_txt = objeto;
     $("#btn-generate").attr("disabled", false); // habilita el boton
     $("#input-nota").hide(); // esconde la advertencia
     $("#btn-generate").click(function() { 
      var nombre_archivo = ( $("#input-file").val() != '' ) ? $("#input-file").val() :'default';
      var blob = new Blob([ "[" + objeto + "]" ], {type: "text/plain;charset=utf-8"});
      saveAs(blob, nombre_archivo + ".json"); // guarda el archivo plano
      location.reload();
    });
    }, 5000); // 5 segundos

  
  
});
