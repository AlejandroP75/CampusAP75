let convertirP = document.getElementById("convertirP");
let convertirL = document.getElementById("convertirL");
let convertirT = document.getElementById("convertirT");
let convertirTi = document.getElementById("convertirTi");

import {peso} from "./peso.js";
import {longitud} from "./longitud.js";
import {tiempo} from "./tiempo.js";
import {temperatura} from "./temperatura.js";

convertirTi.addEventListener("click",tiempo);
convertirT.addEventListener("click",temperatura);
convertirL.addEventListener("click",longitud);
convertirP.addEventListener("click",peso);
