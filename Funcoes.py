def process_data(data, *extra_params, param2, param3, param4):
    """
    Função que processa dados e tem parâmetros em excesso
    
    Returns:
        list: Lista de dados processados.
    """
    if param3 == true:
          print("param4")

    result = []
    for item in data:
        # Processamento dos dados (exemplo fictício)
        processed_item = item * 2 + param2
        result.append(processed_item - param2)
      
    if extra_params:
        print("Atenção: Parâmetros extras foram fornecidos!")

    return result

# Exemplo de uso
input_data = [1, 2, 3, 4]
output = process_data(input_data, "parâmetro1", "parâmetro2")
print("Resultado:", output)
