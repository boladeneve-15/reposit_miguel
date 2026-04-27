#include <fstream>
#include <iostream>

int main() {
    std::ofstream arquivo("pagina.html");

    if (!arquivo.is_open()) {
        std::cerr << "Nao foi possivel criar o arquivo pagina.html\n";
        return 1;
    }

    arquivo << "<!DOCTYPE html>\n";
    arquivo << "<html lang=\"pt-BR\">\n";
    arquivo << "<head>\n";
    arquivo << "  <meta charset=\"UTF-8\">\n";
    arquivo << "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n";
    arquivo << "  <title>Pagina feita em C++</title>\n";
    arquivo << "  <style>\n";
    arquivo << "    body { font-family: Arial, sans-serif; background: #f4f7fb; color: #1f2937; "
               "display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }\n";
    arquivo << "    .caixa { background: white; padding: 32px; border-radius: 16px; box-shadow: 0 10px 30px "
               "rgba(0, 0, 0, 0.12); text-align: center; max-width: 480px; }\n";
    arquivo << "    h1 { margin-bottom: 12px; }\n";
    arquivo << "    p { line-height: 1.6; }\n";
    arquivo << "  </style>\n";
    arquivo << "</head>\n";
    arquivo << "<body>\n";
    arquivo << "  <div class=\"caixa\">\n";
    arquivo << "    <h1>Pagina criada com C++</h1>\n";
    arquivo << "    <p>Este arquivo HTML foi gerado por um programa em C++.</p>\n";
    arquivo << "    <p>Compile e execute o programa para recriar esta pagina.</p>\n";
    arquivo << "  </div>\n";
    arquivo << "</body>\n";
    arquivo << "</html>\n";

    arquivo.close();

    std::cout << "Arquivo pagina.html criado com sucesso.\n";
    return 0;
}
