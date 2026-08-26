//  objetivos: CREATE, READ(1 com ID outros mostrando tudo), UPDADE( ID: rescreve tudo porem não  muda o ID), DELETE (auto explicativo), REGRAS( tem 6 objetos 1. 2. 3. 4. 5. 6. se o cara deletar o 3 tem que ficar 1. 2. 4. 5. 6. e se o cara fizer um novo 1. 2. 4. 5. 6. 7. e apagar o novo logo em sequida 1. 2. 4. 5. 6. e criar um novo a ordem tem que ficar 1. 2. 4. 5. 6. 8.)
    
   
    let acumulador = 1
    let base = {
                    id: 1,
                    nome: "",
                    marca: "",
                    tipo: "",
                    modelo: "",

                }
               

    let informacoes = [

    ]
function busca(X) {
   let  posicao = -1
    for(let i=0;i<informacoes.length;i++){

        if(informacoes[i].id == X ){
            return i
        }
       
}
          
          return posicao

}
    



function CREATE(){
aviso.innerHTML = ""

 let nome =   Nome.value 
 let marca =  Marca.value
 let tipo =   Tipo.value
 let modelo = Modelo.value
 for(i = acumulador ;i <= i+1 ;i++){
informacoes.push({
        id: acumulador,
        nome: nome,
        marca: marca,
        tipo: tipo,
        modelo: modelo
    });
 
    MOSTRAR_TABELA()
 acumulador++
break
}
}
function READ_ALL() {
     aviso.innerHTML = ""

MOSTRAR_TABELA();
   planilha.style.display = "table";

    
}
function READ_ID() {
 aviso.innerHTML = ""


    let valor = parseInt(VERID.value)

    let posicao = busca(valor)

    if (posicao == -1) {

        aviso.innerHTML = "ERRO ID NÃO EXISTE"
        return

    }
    if(posicao != -1){
    let informacao = informacoes[posicao]

    tabela.innerHTML = `
        <tr>
            <td>${informacao.id}</td>
            <td>${informacao.nome}</td>
            <td>${informacao.marca}</td>
            <td>${informacao.tipo}</td>
            <td>${informacao.modelo}</td>
        </tr>
    `

    planilha.style.display = "table"

}
}    

function UPDATE() {
    let  valor = 1
    let novonome = RENome.value
    let novamarca = REMarca.value
    let novotipo = RETipo.value
    let novomodelo = REModelo.value

    posicao = busca(valor)
    
    if (posicao != -1){
        informacoes[posicao] = {
            id:  valor,
            nome: novonome,
            marca: novamarca,
            tipo: novotipo,
            modelo: novomodelo
            
        }

    }


}
function CANCEL() {
pai.style.display = "none";
meio.style.display = "none";

}
function JANELA(){
 aviso.innerHTML = ""
  pai.style.display = "none"
          meio.style.display = "none"

    let valor = parseInt(REID.value)
if(busca(valor) == -1){
        
    aviso.innerHTML = "ERRO ID NÃO EXISTE"
    

        return

    }

    if(busca(valor) != -1){

        selecionado.innerHTML = `Selecionado ID ${valor}`

        pai.style.display = "block"

        meio.style.display = "block"

    }

}

function DELETA(){
     aviso.innerHTML = ""

 let valor = parseInt(IDEL.value)
 if(busca(valor) == -1){
   aviso.innerHTML = "ERRO ID NÃO EXISTE"

 }
 if (busca(valor) != -1) {
    informacoes.splice(busca(valor), 1)
    
 }
console.log(informacoes)
}
function SAIR(){
    planilha.style.display = "none";
}
function MOSTRAR_TABELA() {

    tabela.innerHTML = "";

    for (let i = 0; i < informacoes.length; i++) {

        tabela.innerHTML += `
            <tr>
                <td>${informacoes[i].id}</td>
                <td>${informacoes[i].nome}</td>
                <td>${informacoes[i].marca}</td>
                <td>${informacoes[i].tipo}</td>
                <td>${informacoes[i].modelo}</td>
            </tr>
        `;

    }

}