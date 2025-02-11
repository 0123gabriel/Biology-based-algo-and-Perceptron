#include <iostream>
using namespace std;

int main() {
    // Sintaxis general: [](argumentos) -> tipo { expresion; }
    // Ejemplo de una función que suma dos números
    auto sumar = [](int x, int y) -> int { return x + y; };

    // Uso de la función
    int resultado = sumar(3, 4);
    cout << "Resultado: " << resultado << endl;

    return 0;
}
