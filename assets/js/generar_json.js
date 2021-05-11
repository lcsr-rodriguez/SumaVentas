/**
 * @author          Leiner Ceballos Rodriguez
 * @version         npm 6.14.8
 * @description     Genera una cantidad de datos a partir de una URI
 */

// Retorna a partir de una promise un objeto JSON
 async function getRandomData() {
  try {
    const data = await axios.get("https://random-data-api.com/api/commerce/random_commerce?size=6");
    return data;
  } catch(err) {
    console.log("error: ", err);
  }
}

console.log( getRandomData() )