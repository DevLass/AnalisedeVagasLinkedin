function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  async function coletarTituloETextoComScrollImediato() {
    const resultados = [];
    const numIteracoes = 20; // Ajuste conforme necessário
    const xpathTextoAposClique = `/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[4]/article/div/div[1]/div/p`;
    const scrollAmount = 200; // Ajuste o valor da rolagem conforme necessário
  
    for (var i = 1; i <= numIteracoes; i++) {
      let xpathTituloDinamico = `/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[` + i + `]/div/div/div[1]/div[1]/div[2]/div[1]/a/span[1]/strong`;
      let elementoTitulo = document.evaluate(xpathTituloDinamico, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
  
      if (elementoTitulo) {
        const textoTitulo = elementoTitulo.textContent;
        elementoTitulo.click();
        console.log('Elemento ' + i + ' clicado. Título: "' + textoTitulo + '"');
  
        // Rola a tela imediatamente após o clique
        window.scrollBy(0, scrollAmount);
        console.log('Tela rolada ' + scrollAmount + ' pixels para baixo.');
        await esperar(5); // Espera um pouco após a rolagem para os elementos carregarem
  
        let elementoTextoAposClique = document.evaluate(xpathTextoAposClique, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        let textoAposClique = elementoTextoAposClique ? elementoTextoAposClique.textContent : '';
  
        resultados.push({ Titulo: textoTitulo, Texto: textoAposClique });
        await esperar(5);
      } else {
        console.log('Elemento ' + i + ' (título) não encontrado.');
        break;
      }
    }
  
    console.log('Processo de coleta concluído.');
    console.table(resultados);
    const jsonString = JSON.stringify(resultados, null, 2);
    console.log('\n--- Resultados em Formato JSON ---');
    console.log(jsonString);
  }
  
  coletarTituloETextoComScrollImediato();